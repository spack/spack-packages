# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GtkorvoAtl(CMakePackage):
    """Libatl provides a library for the creation and manipulation of
    lists of name/value pairs using an efficient binary representation.
    """

    homepage = "https://github.com/GTkorvo/atl"
    url = "https://github.com/GTkorvo/atl/archive/v2.1.tar.gz"
    git = "https://github.com/GTkorvo/atl.git"

    maintainers("eisenhauer", "vicentebolea")

    version("master", branch="master")
    version("2.3.0", sha256="8f5746bc2362fd7fe3aa1814f1704449972570f903b2391a7ae6e4efa4cd60be")

    with default_args(deprecated=True):
        version("2.2.1", sha256="7ff2dca93702ed56e3bbfd8eb52da3bb5f0e7bef5006f3ca29aaa468cab89037")
        version("2.2", sha256="d88b6eaa3926e499317973bfb2ae469c584bb064da198217ea5fede6d919e160")
        version("2.1", sha256="379b493ba867b76d76eabfe5bfeec85239606e821509c31e8eb93c2dc238e4a8")

    variant("shared", default=True, when="@2.3:", description="Build shared libraries")

    depends_on("c", type="build")  # generated

    depends_on("gtkorvo-cercs-env", when="@:2.2.1")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@2.3:"):
            args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        elif self.spec.satisfies("@2.2"):
            args.append("-DBUILD_SHARED_LIBS=OFF")
        else:
            args.append("-DENABLE_BUILD_STATIC=STATIC")

        args.append(self.define("ENABLE_TESTING", self.run_tests))
        args.append("-DCMAKE_POSITION_INDEPENDENT_CODE=TRUE")

        return args
