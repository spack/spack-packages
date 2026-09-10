# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Trng(CMakePackage):
    """Tina's Random Number Generator Library"""

    homepage = "https://www.numbercrunch.de/trng/"
    git = "https://github.com/rabauke/trng4.git"

    maintainers("chapman39")

    version("4.28.1", commit="cc1b170b050b541ac481415b175394670c2a4e85", submodules=True)
    version("4.24", commit="a22a32b9a285d1293b74b17b34f81af5dcec6311")
    version("4.23.1", commit="610f7836610e9e01788f8461fbe83b67544ded7c")
    version("4.23", commit="22a30c493eff4cb547185fa48275683751df18e0")
    version("4.22", commit="d5f48c88f23af98a004ed26b4053971ace130ae6")
    version("4.21", commit="9156b3aecf7543b6ef7b43c8e8719b1ebf5b1ca1")
    version("4.20", commit="e14edeb978b2bc88fd3a03b5ee6b40b284ca44e3")
    version("4.19", commit="5e130e97a8019941d58c59dfa221d9d4ba30a00c")
    version("4.18", commit="5663e53af675c0810e20c4ba3c53940e25a3e334")
    version("4.17", commit="1c8cbb0ecdc59983d5ec29c514058fdffae1effa")
    version("4.16", commit="8191fd2729b88deebe094766b8e9144a7fb032f5")

    variant("tests", default=True, description="Build TRNG tests")
    variant("examples", default=True, description="Build TRNG examples", when="@4.28:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.10:", type="build")
    depends_on("cmake@3.30:", type="build", when="@4.28:")

    depends_on("boost")

    patch("0001-Add-inline-to-comparison-operators-in-uniform_int_di.patch", when="@4.23:4.24")
    patch("0002-urng-libcxx19-yarn.patch", when="@4.23:4.24 %clang platform=darwin")

    def cmake_args(self):
        args = []

        if self.spec.satisfies("@4.28:"):
            args.append(self.define_from_variant("TRNG_ENABLE_EXAMPLES", "examples"))
            args.append(self.define_from_variant("TRNG_ENABLE_TESTS", "tests"))
        else:
            args.append(self.define("BUILD_TESTING", self.spec.satisfies("+tests")))

        boost = self.spec["boost"]
        args.append(self.define("Boost_DIR", boost.prefix.lib.cmake.Boost))

        return args
