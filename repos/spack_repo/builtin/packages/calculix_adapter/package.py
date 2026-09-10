# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class CalculixAdapter(MakefilePackage):
    """The preCICE adapter for the CalculiX finite-element solver. It builds the
    ccx_preCICE executable, which couples CalculiX to other solvers (e.g. an
    OpenFOAM fluid solver) through the preCICE coupling library for
    fluid-structure interaction."""

    homepage = "https://precice.org/adapter-calculix-overview.html"
    url = "https://github.com/precice/calculix-adapter/archive/refs/tags/v2.20.1.tar.gz"

    license("GPL-3.0-or-later")

    maintainers("failed33")

    version("2.20.1", sha256="3372e0d66321c2173899e1db4841c6c4f3c16ffb99067c36dba04e8a34e35d39")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("pkgconfig", type="build")

    # The adapter version tracks the CalculiX release it wraps.
    depends_on("calculix@2.20", when="@2.20.1")
    depends_on("spooles")
    depends_on("yaml-cpp")
    # Serial ARPACK (as CalculiX uses it); MPI here comes from preCICE, not ARPACK.
    depends_on("arpack-ng~mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("mpi")

    # The adapter resolves preCICE through pkg-config (libprecice >= 1.4).
    # NOTE: preCICE participants must share a preCICE version to couple over
    # sockets, so a coupled FSI deployment pins this to match the partner solver
    # (e.g. `spack install calculix-adapter ^precice@3.1.2` to match an OpenFOAM
    # adapter that links preCICE 3.1.2). See README for the version-match trap.
    depends_on("precice@2:")

    build_directory = "."

    @property
    def build_targets(self):
        spec = self.spec
        spooles = spec["spooles"].prefix
        ccx_src = join_path(spec["calculix"].prefix, "share", "CalculiX", "ccx_2.20", "src")

        fflags = "-fallow-argument-mismatch" if spec.satisfies("%gcc@10:") else ""

        # The final link is done by the MPI Fortran wrapper, which (unlike the
        # Spack compiler wrapper) injects no rpaths, and preCICE arrives via
        # pkg-config which emits none either. rpath the shared dependencies so
        # ccx_preCICE runs without a module load / LD_LIBRARY_PATH.
        rpaths = " ".join(
            "-Wl,-rpath,{0}".format(d)
            for d in [
                spec["precice"].libs.directories[0],
                spec["yaml-cpp"].libs.directories[0],
                spec["arpack-ng"].libs.directories[0],
                spec["lapack"].libs.directories[0],
                spec["blas"].libs.directories[0],
            ]
        )
        arpack_libs = "{0} {1} {2}".format(
            spec["arpack-ng"].libs.ld_flags,
            spec["lapack"].libs.ld_flags,
            spec["blas"].libs.ld_flags,
        )
        return [
            # CalculiX/preCICE link against MPI (via libprecice); use the MPI
            # compiler wrappers, matching the adapter Makefile defaults. The
            # adapter has no ADDITIONAL_CFLAGS hook, so embed the legacy-C
            # down-grade flags in CC (it compiles CalculiX's 1999-era C too).
            "CC={0} -Wno-error=int-conversion "
            "-Wno-error=implicit-function-declaration -Wno-error=implicit-int".format(
                spec["mpi"].mpicc
            ),
            "FC=" + spec["mpi"].mpifc,
            "CCX=" + ccx_src,
            "SPOOLES_INCLUDE=-I" + spooles.include,
            "SPOOLES_LIBS=-Wl,--start-group {0} -Wl,--end-group".format(
                join_path(spooles.lib, "libspooles.a")
            ),
            "ARPACK_LIBS={0} {1}".format(arpack_libs, rpaths),
            "YAML_INCLUDE=-I" + spec["yaml-cpp"].prefix.include,
            "YAML_LIBS=" + spec["yaml-cpp"].libs.ld_flags,
            "ADDITIONAL_FFLAGS=" + fflags,
        ]

    def edit(self, spec, prefix):
        # Upstream uses -DARCH="Linux"; the embedded quotes mangle the
        # preprocessor token, so normalise it (matches our validated build).
        filter_file('-DARCH="Linux"', "-DARCH=Linux", "Makefile", string=True)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("bin", "ccx_preCICE"), prefix.bin)
