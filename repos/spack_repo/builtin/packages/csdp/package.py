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

    def edit(self, spec, prefix):
        mkdirp(prefix.bin)
        makefile = FileFilter("Makefile")
        makefile.filter("/usr/local/bin", prefix.bin)
        makefile.filter(r"^export LIBS.*$", "")  # use flag_handler instead

    def flag_handler(self, name: str, flags: List[str]):
        if name == "ldflags":
            flags.extend(
                [
                    f"-L{self.stage.source_path}/lib -lsdp",
                    self.spec["lapack"].libs.ld_flags,
                    self.spec["blas"].libs.ld_flags,
                    "-lm",
                ]
            )
        return (flags, None, None)
