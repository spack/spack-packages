# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Gfan(MakefilePackage):
    """Gfan computes Gröbner fans and tropical varieties of polynomial
    ideals, with tools for universal Gröbner bases, tropical curves,
    hypersurfaces, and related structures in tropical geometry."""

    homepage = "https://users-math.au.dk/jensen/software/gfan/gfan.html"
    url = "https://users-math.au.dk/jensen/software/gfan/gfan0.6.2.tar.gz"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("0.8beta", sha256="fa7884e5f317c50f8fb4f37bcf5d419f0fd5f7b90d6037349d1957ea73cebbee")
    version("0.6.2", sha256="a674d5e5dc43634397de0d55dd5da3c32bd358d05f72b73a50e62c1a1686f10a")

    depends_on("cxx", type="build")

    depends_on("cddlib+gmp")
    depends_on("gmp")
    depends_on("tbb", when="@0.8beta:")

    patch("compile-on-more-systems-0.8beta.patch", when="@0.8beta")
    patch(
        "https://raw.githubusercontent.com/Macaulay2/M2/aa0a8e3/M2/libraries/gfan/patch-0.6.2",
        sha256="52eb59458f14644c00fa3281a2d1cf26143a31dab32293a5c69f222ffce6c3b1",
        when="@0.6.2",
    )

    @property
    def build_targets(self):
        targets = [
            f"CXX={spack_cxx}",
            "CDDDEFINE_PREFIX=-DNOCDDPREFIX",
            f"CDD_INCLUDEOPTIONS=-I{self.spec['cddlib'].prefix.include}/cddlib",
            "CDD_LINKOPTIONS=-lcddgmp",
            "GMP_INCLUDEOPTIONS=",
            "GMP_LINKOPTIONS=-lgmp",
        ]
        if self.spec.satisfies("@0.8beta:"):
            targets.append("TBB_INCLUDEOPTIONS=")
            if self.spec.satisfies("platform=darwin"):
                targets.append("PLATFORM_LINKOPTIONS=-ltbb")
            else:
                targets.append("PLATFORM_LINKOPTIONS=-rdynamic -ltbb")
        return targets

    @property
    def install_targets(self):
        return ["install", f"PREFIX={self.spec.prefix}"]
