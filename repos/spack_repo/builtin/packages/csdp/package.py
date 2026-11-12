# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Csdp(MakefilePackage):
    """CSDP is a library of routines that implements a predictor corrector
    variant of the semidefinite programming algorithm of Helmberg, Rendl,
    Vanderbei, and Wolkowicz"""

    homepage = "https://projects.coin-or.org/Csdp"
    url = "https://www.coin-or.org/download/source/Csdp/Csdp-6.1.1.tgz"

    license("CPL-1.0", when="@:6.2.0", checked_by="d-torrance")
    # license has been updated in git for future releases to EPL-2.0

    version("6.2.0", sha256="7f202a15f33483ee205dcfbd0573fdbd74911604bb739a04f8baa35f8a055c5b")
    version("6.1.1", sha256="0558a46ac534e846bf866b76a9a44e8a854d84558efa50988ffc092f99a138b9")

    depends_on("c", type="build")

    depends_on("blas")
    depends_on("lapack")

    with when("@6.2.0"):
        variant("openmp", default=True, description="Build with OpenMP Support")
        depends_on("llvm-openmp", when="+openmp %apple-clang")

        # include <stdio.h> to avoid declaring printf implicitly
        patch(
            "https://salsa.debian.org/math-team/csdp/-/raw/d95bdd34978926971e8b3fcf6622f3086d3b2401/debian/patches/include-stdio.patch",
            sha256="fcd9b1ba04d20a6f150fc56a918f9bcd6ee1681203a9a0bc2aace385694fd54f",
        )
        # more configurable makefile
        patch(
            "https://salsa.debian.org/math-team/csdp/-/raw/d95bdd34978926971e8b3fcf6622f3086d3b2401/debian/patches/makefile.patch",
            sha256="8d51be78e50708085a8749fcac1b23a5dd24d404cee32a388d7c0c40ba474d5c",
        )

    @property
    def build_targets(self):
        if self.spec.satisfies("@6.2.0"):
            blas_libs = (self.spec["lapack"].libs + self.spec["blas"].libs).ld_flags
            if self.spec.satisfies("+openmp"):
                openmp_cflags = self.spec["c"].package.openmp_flag
                if self.spec.satisfies("%apple-clang"):
                    openmp_cflags += f" {self.spec['llvm-openmp'].headers.include_flags}"
                    openmp_libs = self.spec["llvm-openmp"].libs.ld_flags
                else:
                    openmp_libs = ""
            else:
                openmp_cflags = ""
                openmp_libs = ""
            return [
                f"BLAS_LIBS={blas_libs}",
                f"OPENMP_CFLAGS={openmp_cflags}",
                f"OPENMP_LIBS={openmp_libs}",
            ]
        else:
            return []

    @property
    def install_targets(self):
        if self.spec.satisfies("@6.2.0"):
            return ["install", f"prefix={self.prefix}"]
        else:
            return ["install"]

    @when("@6.1.1")
    def edit(self, spec, prefix):
        mkdirp(prefix.bin)
        makefile = FileFilter("Makefile")
        makefile.filter("/usr/local/bin", prefix.bin)
        makefile.filter(r"^export LIBS.*$", "")  # use flag_handler instead

    def flag_handler(self, name: str, flags: List[str]):
        if name == "ldflags" and self.spec.satisfies("@6.1.1"):
            flags.extend(
                [
                    f"-L{self.stage.source_path}/lib -lsdp",
                    self.spec["lapack"].libs.ld_flags,
                    self.spec["blas"].libs.ld_flags,
                    "-lm",
                ]
            )
        return (flags, None, None)
