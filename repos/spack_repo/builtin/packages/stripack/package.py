# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Stripack(MakefilePackage):
    """STRIPACK:
    Delaunay Triangulation rewritten in Fortran 90 by John Burkardt at
    https://people.sc.fsu.edu/~jburkardt/f_src/stripack/stripack.html

    The original Fortran 77 package STRIPACK is available from netlib as algorithm number 772 at
    https://www.netlib.org/toms/772.gz
    Dr. Renka's articles were published in the ACM Transactions on Mathematical Software, Vol. 23,
    No 3, September 1997.
    https://dl.acm.org/doi/10.1145/275323.275329
    """

    homepage = "https://people.sc.fsu.edu/~jburkardt/f_src/stripack/stripack.html"

    maintainers("cessenat")

    license("MIT")

    version(
        "develop",
        sha256="26c074bc46fb8549d7a42ec713636798297d7327c8f3ce0ba2d3348a501ffa7c",
        expand=False,
        url="https://people.sc.fsu.edu/~jburkardt/f_src/stripack/stripack.f90",
    )

    depends_on("fortran", type="build")

    build_targets = ["all"]

    @run_before("build")
    def run_mkmake(self):
        config = [
            "BUILDIR ?= " + join_path(self.build_directory, "build"),
            "DYLIB=" + dso_suffix,
            "F90=" + spack_fc,
            "LD=" + spack_fc,
            ".SUFFIXES: .f .f90 .F90",
            "$(BUILDIR)/%.o: %.f90",
            "\t$(F90) $(FFLAGS) -c $< -o $@",
            "all: $(BUILDIR)/stripack.o",
            "\t$(LD) -shared $(LDFLAGS) -o $(BUILDIR)/libstripack.$(DYLIB)"
            + " $(BUILDIR)/stripack.o $(LIBS)",
        ]
        with open("Makefile", "w") as fh:
            fh.write("\n".join(config))
        mkdirp(join_path(self.build_directory, "build"))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # This is smartly used by VisIt
        env.set(
            "VISIT_FFP_STRIPACK_PATH", join_path(self.spec.prefix.lib, "libstripack." + dso_suffix)
        )

    def flag_handler(self, name, flags):
        if name != "fflags":
            return flags, None, None

        spec = self.spec

        # The original Fortran 77 version has to be built in double precision mode.
        if spec.satisfies("%fortran=gcc") or spec.satisfies("%fortran=llvm"):
            flags.extend(["-fdefault-real-8", "-fdefault-double-8"])
        elif spec.satisfies("%fortran=xl"):
            flags.append("-qrealsize=8")
        elif spec.satisfies("%fortran=fj"):
            flags.append("-CcdRR8")
        elif any(
            spec.satisfies(f"%fortran={compiler}")
            for compiler in ("intel", "oneapi", "aocc", "nvhpc")
        ):
            flags.append("-r8")

        flags.append(spec["fortran"].package.pic_flag)
        return flags, None, None

    def install(self, spec, prefix):
        mkdirp(prefix.lib)
        install(join_path(self.build_directory, "build", "libstripack." + dso_suffix), prefix.lib)
