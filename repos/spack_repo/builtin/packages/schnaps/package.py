# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *
from spack_repo.builtin.build_systems.cmake import CMakePackage


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

    # Fetch the full repo (commit graph + all tags) for every version so
    # cmake/git_version.cmake's `git describe --tags` can stamp the version number
    # into the exe
    get_full_repo = True

    maintainers("d-reynolds")

    license("GPL-3.0-or-later", checked_by="d-reynolds")

    version("main", branch="main")
    version("develop", branch="develop")

    # -- Versions comment block used by maintenance script, do not remove ------
    # BEGIN VERSIONS
    version(
        "1.1.1",
        tag="v1.1.1",
    )
    version(
        "1.1.0",
        tag="v1.1.0",
    )
    # END VERSIONS

    # -- Language toolchain (Spack v0.22+ compiler-as-dependency model) --------
    # SCHNAPS is Fortran; project(SCHNAPS) also enables C and C++ (used by the
    # NoahMP/RTE-RRTMGP subprojects and the SNOWPACK C++ std-lib link).
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # SCHNAPS's CMake hard-errors on any compiler that is not GNU (gfortran) or
    # NVHPC (nvfortran).
    conflicts("%intel", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts(
        "%oneapi", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)"
    )
    conflicts("%clang", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")
    conflicts(
        "%apple-clang", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)"
    )
    conflicts("%cce", msg="SCHNAPS supports only GNU (gfortran) or NVHPC (nvfortran)")

    # GPU (OpenACC) build. Requires the NVHPC/nvfortran compiler; uses the NVHPC SDK's
    # own bundled CUDA / cuFFT / NCCL (do NOT add standalone cuda/nccl deps).
    variant(
        "gpu",
        default=False,
        description="Build for GPU: OpenACC + NCCL (requires %nvhpc)",
    )

    # Optional explicit GPU compute-capability targeting; maps to -DGPU_CC.
    # The default 'none' keeps the portable cc80,cc90,cc100,cc120 fat binary
    # the build's NATIVE=OFF path selects.
    variant(
        "cuda_arch",
        values=any_combination_of("native", "70", "80", "86", "89", "90", "100", "120"),
        description="GPU compute capability target(s); none = portable cc80,cc90,cc100,cc120 fat binary",
    )

    # -- Build tooling ---------------------------------------------------------
    depends_on("cmake@3.20:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("git", type="build")

    # -- Runtime / link dependencies ------------------------------------------
    depends_on("mpi")
    depends_on("fftw@3:", when="~gpu")

    # Parallel NetCDF stack. SCHNAPS reads/writes NetCDF in parallel and probes
    # `nc-config --has-parallel`; it needs both the classic (PnetCDF) and
    # NetCDF-4 (HDF5) parallel paths.
    depends_on("netcdf-fortran")
    depends_on("netcdf-c@4.10: +mpi +parallel-netcdf +blosc")
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
    # SCHNAPS's CMakeLists / snowpack.cmake pull five sources from the
    # network via FetchContent / ExternalProject.
    #
    # NOTE: pinned to concrete commits and shared across releases via `when="@1.0.1:"`.
    # bump_spack_recipe.py guards these against SCHNAPS's CMakeLists.txt /
    # cmake/snowpack.cmake pins each time the bump-spack workflow runs
    resource(
        name="rte-rrtmgp",
        git="https://github.com/earth-system-radiation/rte-rrtmgp.git",
        commit="77ff83ccf645e5bc404c138ca4e7a6e3abf5d963",  # tag v1.9.2
        destination="_spack_deps",
        placement="rte-rrtmgp",
        when="@1.0.1:",
    )
    resource(
        name="rrtmgp-data",
        git="https://github.com/earth-system-radiation/rrtmgp-data.git",
        commit="eff0433faf9cbac3ad14fbf608bef0c26ebc4c79",  # tag v1.9
        destination="_spack_deps",
        placement="rrtmgp-data",
        when="@1.0.1:",
    )
    resource(
        name="noahmp",
        git="https://codeberg.org/SCHNAPS-Model/noahmp.git",
        commit="a3c314771e7b7a3e46a80983bd6cee9d9092a362",  # branch OpenACC
        destination="_spack_deps",
        placement="noahmp",
        when="@1.0.1:",
    )
    resource(
        name="icar_supporting_files",
        git="https://github.com/NCAR/icar_supporting_files.git",
        commit="8b20ace82edbf0e3bc335986a2af87eeab044bb0",
        destination="_spack_deps",
        placement="icar_supporting_files",
        when="@1.0.1:",
    )
    resource(
        name="snowpack",
        git="https://code.wsl.ch/snow-models/snowpack.git",
        commit="2a099259447c1973ef1fbd7c78000136a697b916",  # branch fortran-bindings
        destination="_spack_deps",
        placement="snowpack",
        when="@1.0.1:",
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
            self.define("ASSERTIONS", True),
            self.define("NATIVE", False),
            # Point CMake FetchContent at the pre-staged (offline) sources.
            # The variable suffix is the upper-cased FetchContent content name.
            self.define(
                "FETCHCONTENT_SOURCE_DIR_RTE-RRTMGP", join_path(deps, "rte-rrtmgp")
            ),
            self.define(
                "FETCHCONTENT_SOURCE_DIR_RRTMGP-DATA", join_path(deps, "rrtmgp-data")
            ),
            self.define("FETCHCONTENT_SOURCE_DIR_NOAHMP", join_path(deps, "noahmp")),
            self.define(
                "FETCHCONTENT_SOURCE_DIR_ICAR_SUPPORTING_FILES",
                join_path(deps, "icar_supporting_files"),
            ),
            # Native-Fortran SNOWPACK port: a populated SNOWPACK_DIR makes
            # snowpack_fetch_sources() skip the clone and just glob
            # ${SNOWPACK_DIR}/fortran/snowpack_*.F90 into the build.
            self.define("SNOWPACK_DIR", join_path(deps, "snowpack")),
        ]

        archs = spec.variants["cuda_arch"].value
        if archs != ("none",):
            if "native" in archs and len(archs) > 1:
                raise InstallError(
                    "cuda_arch=native cannot be combined with numeric values"
                )
            cc = ",".join("ccnative" if a == "native" else f"cc{a}" for a in archs)
            args.append(self.define("GPU_CC", cc))

        return args

    def setup_build_environment(self, env):
        # fftw (CPU only) / netcdf-c / netcdf-fortran are found through CMAKE_PREFIX_PATH,
        # which Spack already populates from the build spec.

        # GPU: use NVHPC's bundled CUDA / cuFFT / NCCL (mirrors a manual
        # `module load nvhpc` build). Pass NVHPC_ROOT through so SCHNAPS's finders
        # locate cuFFT ($NVHPC_ROOT/math_libs) and NCCL ($NVHPC_ROOT/comm_libs/nccl).
        # Requires the nvhpc module to be loaded when you run `spack install`
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
    #                                rrtmgp_support/. Loaded from the run's WORKING
    #                                directory under fixed names (not namelist options) —
    #                                link or copy this dir's contents into the case dir.
