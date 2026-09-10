# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Glpk(AutotoolsPackage, GNUMirrorPackage):
    """The GLPK (GNU Linear Programming Kit) package is intended for solving
    large-scale linear programming (LP), mixed integer programming
    (MIP), and other related problems. It is a set of routines written
    in ANSI C and organized in the form of a callable library.
    """

    homepage = "https://www.gnu.org/software/glpk"
    gnu_mirror_path = "glpk/glpk-4.65.tar.gz"

    license("GPL-3.0-only")

    version("5.0", sha256="4a1013eebb50f728fc601bdd833b0b2870333c3b3e5a816eeba921d95bec6f15")
    version("4.65", sha256="4281e29b628864dfe48d393a7bedd781e5b475387c20d8b0158f329994721a10")
    version("4.61", sha256="9866de41777782d4ce21da11b88573b66bb7858574f89c28be6967ac22dfaba9")
    version("4.57", sha256="7323b2a7cc1f13e45fc845f0fdca74f4daea2af716f5ad2d4d55b41e8394275c")

    variant("gmp", default=False, description="Activates support for GMP library")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("gmp", when="+gmp")

    # Do not define bool, true, or false for C23 compatibility
    patch(
        "https://salsa.debian.org/science-team/glpk/-/raw/2dd3b283654555100edde4d72fbe1b1a4883292a/debian/patches/gcc-15.patch",
        sha256="f9a1fc747a8cf9a484e517fbc105d3e8e50ac588430614267444271d3411f0ac",
    )

    def configure_args(self):
        options = []

        if self.spec.satisfies("+gmp"):
            options.append("--with-gmp")

        return options
