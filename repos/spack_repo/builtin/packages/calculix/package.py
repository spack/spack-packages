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
    url = "https://www.dhondt.de/ccx_2.20.src.tar.bz2"

    license("GPL-2.0-or-later")

    maintainers("failed33")

    version("2.24", sha256="99fb4f9b0ec19b100a914c3a097ea1e7f0c22f715b96338acc4a66b63306a2e2")
    version("2.23", sha256="9c88385c10fb04f5dc6c4e98027a51bebdd8aee3920e05190d6c1dd08357d6e7")
    version("2.20", sha256="63bf6ea09e7edcae93e0145b1bb0579ea7ae82e046f6075a27c8145b72761bcf")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("spooles")
    # CalculiX is serial/OpenMP and links the serial ARPACK eigensolver; ~mpi
    # keeps the whole MPI stack out of a standalone CalculiX build.
    depends_on("arpack-ng~mpi")
    depends_on("blas")
    depends_on("lapack")
    requires("^openblas~ilp64", when="^[virtuals=blas,lapack] openblas")

    # Spack strips the archive's single top-level CalculiX/ dir, so the source
    # root is already inside it.
    @property
    def executable(self):
        return f"ccx_{self.version}"

    @property
    def build_directory(self):
        return join_path(self.executable, "src")

    @property
    def build_targets(self):
        spec = self.spec
        # Legacy C in CalculiX/SPOOLES: keep modern gcc (>= 14) and clang from
        # promoting int-conversion etc. to hard errors (no-ops on gcc 11).
        legacy = (
            "-Wno-error=int-conversion -Wno-error=implicit-function-declaration "
            "-Wno-error=implicit-int -Wno-error=incompatible-pointer-types"
        )
        cflags = (
            f"-Wall -O2 -fopenmp {legacy} -I{spec['spooles'].prefix.include} "
            "-DARCH=Linux -DSPOOLES -DARPACK -DMATRIXSTORAGE -DNETWORKOUT"
        )
        fflags = "-Wall -O2 -fopenmp -cpp"
        if spec.satisfies("%gcc@10:"):
            # gfortran 10+ rejects CalculiX's legacy argument-mismatch patterns.
            fflags += " -fallow-argument-mismatch"
        libs = "{} {} {} -lpthread -lm -lc".format(
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

        with working_dir(self.build_directory):
            # LIBS contains linker flags. Do not treat them as prerequisites.
            filter_file(
                rf"^{self.executable.replace('.', r'[.]')}:.*\$\(LIBS\)$",
                f"{self.executable}: $(OCCXMAIN) {self.executable}.a",
                "Makefile",
            )

            # Avoid stamping build time into the shipped sources and executable.
            if spec.satisfies("@2.24:"):
                filter_file('__DATE__ " " __TIME__', '"unknown"', "buildinfo.c", string=True)
            else:
                filter_file(
                    f"./date.pl; $(CC) $(CFLAGS) -c {self.executable}.c; ",
                    "",
                    "Makefile",
                    string=True,
                )
            filter_file(
                rf"\$\(OCCXMAIN\) {self.executable.replace('.', r'[.]')}\.a +\$\(LIBS\) -fopenmp",
                f"$(OCCXMAIN) -Wl,--start-group {self.executable}.a {spooles_a} "
                "-Wl,--end-group $(LIBS) -fopenmp",
                "Makefile",
            )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with working_dir(self.build_directory):
            install(self.executable, join_path(prefix.bin, "ccx"))
            # Keep the installed sources for consumers of the existing package layout.
            install_tree(
                ".",
                join_path(prefix, "share", "CalculiX", self.build_directory),
                ignore=lambda filename: (
                    filename == self.executable or filename.endswith((".o", ".a"))
                ),
            )
