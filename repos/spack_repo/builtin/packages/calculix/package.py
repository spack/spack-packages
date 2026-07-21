# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Calculix(MakefilePackage):
    """CalculiX (CCX) is a free finite-element program for three-dimensional
    structural and thermal analysis. It reads an Abaqus-like input format and
    relies on the SPOOLES sparse solver and the ARPACK eigensolver."""

    homepage = "http://www.calculix.de/"
    url = "http://www.dhondt.de/ccx_2.20.src.tar.bz2"

    license("GPL-2.0-or-later")

    maintainers("failed33")

    version("2.20", sha256="63bf6ea09e7edcae93e0145b1bb0579ea7ae82e046f6075a27c8145b72761bcf")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("spooles")
    # CalculiX is serial/OpenMP and links the serial ARPACK eigensolver; ~mpi
    # keeps the whole MPI stack out of a standalone CalculiX build.
    depends_on("arpack-ng~mpi")
    depends_on("blas")
    depends_on("lapack")

    # Spack strips the archive's single top-level CalculiX/ dir, so the source
    # root is already inside it.
    build_directory = "ccx_2.20/src"

    @property
    def build_targets(self):
        spec = self.spec
        # Legacy C in CalculiX/SPOOLES: keep modern gcc (>= 14) and clang from
        # promoting int-conversion etc. to hard errors (no-ops on gcc 11).
        legacy = (
            "-Wno-error=int-conversion -Wno-error=implicit-function-declaration "
            "-Wno-error=implicit-int"
        )
        cflags = (
            "-Wall -O2 -fopenmp {1} -I{0} -DARCH=Linux -DSPOOLES -DARPACK "
            "-DMATRIXSTORAGE -DNETWORKOUT".format(spec["spooles"].prefix.include, legacy)
        )
        fflags = "-Wall -O2 -fopenmp"
        if spec.satisfies("%gcc@10:"):
            # gfortran 10+ rejects CalculiX's legacy argument-mismatch patterns.
            fflags += " -fallow-argument-mismatch"
        libs = "{0} {1} {2} -lpthread -lm -lc".format(
            spec["arpack-ng"].libs.ld_flags,
            spec["lapack"].libs.ld_flags,
            spec["blas"].libs.ld_flags,
        )
        return [
            "CC=" + spack_cc,
            "FC=" + spack_fc,
            "CFLAGS=" + cflags,
            "FFLAGS=" + fflags,
            "LIBS=" + libs,
        ]

    def edit(self, spec, prefix):
        spooles_a = join_path(spec["spooles"].prefix.lib, "libspooles.a")

        # An overridden edit()/install() runs from the stage root, not the
        # build_directory, so patch the Makefile inside the CalculiX source dir.
        with working_dir(self.build_directory):
            # $(LIBS) is overridden on the make command line to ARPACK/LAPACK/BLAS
            # linker flags; drop it from the ccx_2.20 prerequisites so Make does
            # not try to build "-lpthread" and friends as files.
            # NB: no trailing \s* — filter_file is line-based with the newline
            # included, so \s*$ would eat it and fuse this line into its recipe.
            filter_file(
                r"^ccx_2\.20:.*\$\(LIBS\)$",
                "ccx_2.20: $(OCCXMAIN) ccx_2.20.a",
                "Makefile",
            )

            # SPOOLES is no longer carried in $(LIBS); link its static archive
            # explicitly, wrapping the archives in --start-group so the cyclic
            # C/Fortran symbol references between them resolve.
            filter_file(
                "$(OCCXMAIN) ccx_2.20.a $(LIBS) -fopenmp",
                "$(OCCXMAIN) -Wl,--start-group ccx_2.20.a {0} -Wl,--end-group "
                "$(LIBS) -fopenmp".format(spooles_a),
                "Makefile",
                string=True,
            )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with working_dir(self.build_directory):
            install("ccx_2.20", join_path(prefix.bin, "ccx"))

            # Publish the CalculiX sources, headers and Makefile.inc so that the
            # calculix-adapter package can compile ccx_preCICE against them
            # ($(CCX) in the adapter Makefile points here).
            install_tree(".", join_path(prefix, "share", "CalculiX", "ccx_2.20", "src"))
