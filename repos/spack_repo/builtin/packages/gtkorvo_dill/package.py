# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GtkorvoDill(CMakePackage):
    """DILL provides instruction-level code generation,
    register allocation and simple optimizations for generating
    executable code directly into memory regions for immediate use.
    """

    homepage = "https://github.com/GTkorvo/dill"
    url = "https://github.com/GTkorvo/dill/archive/v2.1.tar.gz"
    git = "https://github.com/GTkorvo/dill.git"

    maintainers("eisenhauer", "vicentebolea")

    version("develop", branch="master")
    version("3.3.0", sha256="b29b68ce0cb778ccee614db12405cb72e817b74e914ca909a39e6a4a62fdd9a5")
    version("3.2.0", sha256="80d7e80a7b4d532e71de860f0b138bdf63db350b4517f08c5a596a4c84a501a4")

    with default_args(deprecated=True):
        version("2.4.1", sha256="93c9e3c8e24ab91786639273a89934c2f384638b03aa0dd0f40e58cdf5a8f0f7")
        version("2.4", sha256="ed7745d13e8c6a556f324dcc0e48a807fc993bdd5bb1daa94c1df116cb7e81fa")
        version("2.1", sha256="7671e1f3c25ac6a4ec2320cec2c342a2f668efb170e3dba186718ed17d2cf084")

    variant("shared", default=True, when="@3.2:", description="Build shared libraries")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # Ref: https://github.com/GTkorvo/dill/commit/dac6dfcc7fdaceeb4c157f9ecdf5ecc28f20477f
    patch("2.4-fix-clear_cache.patch", when="@2.4")
    patch("2.1-fix-clear_cache.patch", when="@2.1")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@3.2:"):
            args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))
        elif self.spec.satisfies("@2.4"):
            args.append("-DBUILD_SHARED_LIBS=OFF")
        else:
            args.append("-DENABLE_BUILD_STATIC=STATIC")

        args.append(self.define("ENABLE_TESTING", self.run_tests))
        args.append("-DCMAKE_POSITION_INDEPENDENT_CODE=TRUE")

        return args
