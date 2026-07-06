# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Schnaps(CMakePackage):
    """SCHNAPS (Snow Cover and High-resolutioN Atmospheric Processes System).

    SCHNAPS is an MPI + OpenACC atmospheric model developed with a focus on
    computational efficiency and on resolving the processes relevant for
    simulating seasonal snowpack. It shares physics parameterizations with
    traditional weather models such as WRF but uses massively simplified
    dynamics, enabling run times up to two to three orders of magnitude faster
    than WRF. SCHNAPS provides two-way online coupling between the SNOWPACK snow
    model and the atmosphere, allowing explicit simulation of drifting and
    blowing snow. It grew out of the HICAR / ICAR model lineage.
    """

    homepage = "https://schnaps-model.codeberg.page/SCHNAPS/"
    git = "https://codeberg.org/SCHNAPS-Model/SCHNAPS.git"

    maintainers("d-reynolds")

    license("GPL-3.0-or-later", checked_by="d-reynolds")

    # Pin to the exact commit behind the release tag. v1.0.1 is
    # the first release with offline-build support — pinned dependency commits,
    # plus the FETCHCONTENT_SOURCE_DIR overrides this recipe relies on
    version(
        "1.0.1",
        tag="v1.0.1",
        commit="47384dff0206c81600b9377b9a56238c9e7610aa",
    )

    # -- Language toolchain (Spack v0.22+ compiler-as-dependency model) --------
    # SCHNAPS is Fortran; project(SCHNAPS) also enables C and C++ (used by the
    # NoahMP/RTE-RRTMGP subprojects and the SNOWPACK C++ std-lib link).
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # SCHNAPS's CMake hard-errors on any compiler that is not GNU (gfortran) or
    # NVHPC (nvfortran). This recipe currently packages the CPU (GNU) build only.
    conflicts("%intel", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts("%oneapi", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts("%clang", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts("%apple-clang", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts("%cce", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")

    # -- Variants --------------------------------------------------------------
    variant("assertions", default=True, description="Check logical assertions at runtime")
    variant(
        "native",
        default=True,
        description="Tune for the build host CPU (-march=native); disable for portable binaries",
    )
    # GPU (OpenACC) build. Requires the NVHPC/nvfortran compiler; uses the NVHPC SDK's
    # own bundled CUDA / cuFFT / NCCL (do NOT add standalone cuda/nccl deps — see below).
    variant("gpu", default=False, description="Build for GPU: OpenACC + NCCL (requires %nvhpc)")

    # -- Build tooling ---------------------------------------------------------
    depends_on("cmake@3.20:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("git", type="build")

    # -- Runtime / link dependencies ------------------------------------------
    depends_on("mpi")
    depends_on("fftw@3:")

    # Parallel NetCDF stack. SCHNAPS reads/writes NetCDF in parallel and probes
    # `nc-config --has-parallel`; it needs both the classic (PnetCDF) and
    # NetCDF-4 (HDF5) parallel paths.
    depends_on("netcdf-fortran")
    depends_on("netcdf-c +mpi +parallel-netcdf")
    depends_on("hdf5 +mpi")
    depends_on("parallel-netcdf")

    # -- GPU (OpenACC) toolchain -----------
    # SCHNAPS's CMake hard-errors on GPU builds without nvfortran.
    requires(
        "%nvhpc",
        when="+gpu",
        msg="SCHNAPS GPU (OpenACC) builds require the NVHPC / nvfortran compiler",
    )
    # cuFFT (linear-wind FFT) and NCCL (multi-GPU halo exchange) come from the
    # NVHPC SDK's OWN bundle — SCHNAPS's finders search $NVHPC_ROOT/math_libs and
    # $NVHPC_ROOT/comm_libs/nccl, and nvfortran targets NVHPC's integrated CUDA.

    # GPU MPI REQUIREMENT (verified on GPU hardware, NVHPC 26.3): the MPI must be
    # built with nvfortran — SCHNAPS `use mpi_f08`, and Fortran .mod files are
    # compiler-specific, so nvfortran cannot consume a gfortran-built mpi_f08.mod.
    # register NVHPC's bundled HPC-X OpenMPI as a Spack external (`mpif90 -show` reveals it)

    # -- Vendored dependencies that upstream CMake fetches at configure time ---
    # SCHNAPS's CMakeLists / FindSNOWPACK.cmake pull five sources from the
    # network via FetchContent / ExternalProject.
    #
    # NOTE: Dependencies are pinned to concrete commits below for
    # reproducibility; refresh them when SCHNAPS bumps its versions.
    resource(
        name="rte-rrtmgp",
        git="https://github.com/earth-system-radiation/rte-rrtmgp.git",
        commit="77ff83ccf645e5bc404c138ca4e7a6e3abf5d963",  # tag v1.9.2
        destination="_spack_deps",
        placement="rte-rrtmgp",
        when="@1.0.1",
    )
    resource(
        name="rrtmgp-data",
        git="https://github.com/earth-system-radiation/rrtmgp-data.git",
        commit="eff0433faf9cbac3ad14fbf608bef0c26ebc4c79",  # tag v1.9
        destination="_spack_deps",
        placement="rrtmgp-data",
        when="@1.0.1",
    )
    resource(
        name="noahmp",
        git="https://codeberg.org/SCHNAPS-Model/noahmp.git",
        commit="35f6f6f4e0df6548e2511dda3c2540e11bd2acbf",  # branch OpenACC
        destination="_spack_deps",
        placement="noahmp",
        when="@1.0.1",
    )
    resource(
        name="icar_supporting_files",
        git="https://github.com/NCAR/icar_supporting_files.git",
        commit="8b20ace82edbf0e3bc335986a2af87eeab044bb0",
        destination="_spack_deps",
        placement="icar_supporting_files",
        when="@1.0.1",
    )
    resource(
        name="snowpack",
        git="https://code.wsl.ch/snow-models/snowpack.git",
        commit="4c6dc6df3f9a8135fba82b72399c0b0f765e3a6a",  # branch fortran-bindings
        destination="_spack_deps",
        placement="snowpack",
        when="@1.0.1",
    )

    @property
    def _deps_dir(self):
        return join_path(self.stage.source_path, "_spack_deps")

    def cmake_args(self):
        spec = self.spec
        deps = self._deps_dir

        args = [
            self.define("MODE", "release"),
            self.define_from_variant("OPENACC", "gpu"),
            self.define_from_variant("NCCL", "gpu"),
            self.define("FSM", False),
            self.define("SNOWPACK_CPP", False),
            self.define_from_variant("ASSERTIONS", "assertions"),
            self.define_from_variant("NATIVE", "native"),
            # Point CMake FetchContent at the pre-staged (offline) sources.
            # The variable suffix is the upper-cased FetchContent content name.
            self.define(
                "FETCHCONTENT_SOURCE_DIR_RTE-RRTMGP", join_path(deps, "rte-rrtmgp")
            ),
            self.define(
                "FETCHCONTENT_SOURCE_DIR_RRTMGP_DATA", join_path(deps, "rrtmgp-data")
            ),
            self.define("FETCHCONTENT_SOURCE_DIR_NOAH_MP", join_path(deps, "noahmp")),
            self.define(
                "FETCHCONTENT_SOURCE_DIR_ICAR_SUPPORTING_FILES",
                join_path(deps, "icar_supporting_files"),
            ),
            # Native-Fortran SNOWPACK port: a non-empty SNOWPACK_DIR makes the
            # CMakeLists skip find_package(SNOWPACK) and just glob
            # ${SNOWPACK_DIR}/fortran/snowpack_*.F90 into the build.
            self.define("SNOWPACK_DIR", join_path(deps, "snowpack")),
            self.define("FFTW_DIR", spec["fftw"].prefix),
            # netcdf-c and netcdf-fortran are separate prefixes in Spack; the
            # finder locates each half from its own dir.
            self.define("NETCDF_C_DIR", spec["netcdf-c"].prefix),
            self.define("NETCDF_FORTRAN_DIR", spec["netcdf-fortran"].prefix),
        ]
        return args

    def setup_build_environment(self, env):
        env.set("NETCDF_C_DIR", self.spec["netcdf-c"].prefix)
        env.set("NETCDF_FORTRAN_DIR", self.spec["netcdf-fortran"].prefix)

        # GPU: use NVHPC's bundled CUDA / cuFFT / NCCL (mirrors a manual
        # `module load nvhpc` build). Pass NVHPC_ROOT through so SCHNAPS's finders
        # locate cuFFT ($NVHPC_ROOT/math_libs) and NCCL ($NVHPC_ROOT/comm_libs/nccl).
        # Deliberately do NOT set CUDA_HOME — nvfortran must use its integrated CUDA,
        # or its GPU codegen (and CMake's OpenACC probe) fails. Requires the nvhpc
        # module to be loaded when you run `spack install` (which you do for %nvhpc).
        if self.spec.satisfies("+gpu"):
            nvhpc_root = os.environ.get("NVHPC_ROOT")
            if nvhpc_root:
                env.set("NVHPC_ROOT", nvhpc_root)

    # No install() override needed: SCHNAPS's CMake honors CMAKE_INSTALL_PREFIX, so the
    # standard CMakePackage install phase places:
    #   <prefix>/bin/SCHNAPS         (CPU build) — or SCHNAPS_gpu for a +gpu build
    #                                (nvfortran+OpenACC builds get the _gpu suffix).
    #   <prefix>/share/schnaps/run/  runtime support data the model REQUIRES at run time:
    #                                NoahmpTable.TBL, mp_support/, rrtmg_support/,
    #                                rrtmgp_support/. Not found relative to the exe — a
    #                                run's namelist must point at this dir (or copy it
    #                                next to the case).
