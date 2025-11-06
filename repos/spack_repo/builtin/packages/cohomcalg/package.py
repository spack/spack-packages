# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Cohomcalg(MakefilePackage):
    """cohomCalg is a C++ software package for computing the
    dimensions of line bundle-valued sheaf cohomology groups on toric
    varieties. It implements efficient algorithms from algebraic
    geometry to support applications in both mathematics and
    theoretical physics."""

    homepage = "https://github.com/BenjaminJurke/cohomCalg"
    git = "https://github.com/BenjaminJurke/cohomCalg"

    maintainers("d-torrance")

    license("GPL-3.0-or-later", checked_by="d-torrance")

    version("0.32", tag="v0.32", commit="c663c8e37cceab3cc0b2bcc57d35cb895930ab1f")

    depends_on("cxx", type="build")

    patch("fix-literal-suffix.patch")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("bin/cohomcalg", prefix.bin)
