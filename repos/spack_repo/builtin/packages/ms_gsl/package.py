# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MsGsl(CMakePackage):
    """Microsoft's implementation of the Guidelines Support Library (GSL)
    specified by the C++ Core Guidelines."""

    homepage = "https://github.com/Microsoft/GSL"
    url = "https://github.com/Microsoft/GSL/archive/v2.0.0.tar.gz"
    git = "https://github.com/Microsoft/GSL.git"

    maintainers("johnwparent")

    license("MIT")

    version("main", branch="main")
    version("5.0.1", sha256="733a87a7eea56db075ee060735ba7616a27c1c55955f264d5473bf9e83294ad0")
    version("5.0.0", sha256="e646da6ac00a885cfae33dc935e52bb42bd1d05e41b8437cbc25ca3d74930f35")
    version("4.2.2", sha256="59e2a0a0ea22e8bcf9db2dc4d4bd21212ac6595748295fc27a7e02cf75eac4b5")
    version("4.2.1", sha256="d959f1cb8bbb9c94f033ae5db60eaf5f416be1baa744493c32585adca066fe1f")
    version("4.2.0", sha256="2c717545a073649126cb99ebd493fa2ae23120077968795d2c69cbab821e4ac6")
    version("4.1.0", sha256="0a227fc9c8e0bf25115f401b9a46c2a68cd28f299d24ab195284eb3f1d7794bd")
    version("4.0.0", sha256="f0e32cb10654fea91ad56bde89170d78cfbf4363ee0b01d8f097de2ba49f6ce9")
    version("3.1.0", sha256="d3234d7f94cea4389e3ca70619b82e8fb4c2f33bb3a070799f1e18eef500a083")
    version("2.1.0", sha256="ef73814657b073e1be86c8f7353718771bf4149b482b6cb54f99e79b23ff899d")
    version("2.0.0", sha256="6cce6fb16b651e62711a4f58e484931013c33979b795d1b1f7646f640cfa9c8e")
    version("1.0.0", sha256="9694b04cd78e5b1a769868f19fdd9eea2002de3d4c3a81a1b769209364543c36")

    # Upstream dropped GSL_CXX_STANDARD in 4.1 in favor of
    # target_compile_features(GSL INTERFACE cxx_std_14).
    variant(
        "cxxstd",
        default="14",
        values=("14", "17"),
        multi=False,
        when="@:4.0",
        description="Use the specified C++ standard when building.",
    )

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.1.3:", type="build")
    depends_on("cmake@3.14:", type="build", when="@4.1:")

    def cmake_args(self):
        args = [self.define("GSL_TEST", self.run_tests)]
        if self.spec.satisfies("@:4.0"):
            args.append(self.define_from_variant("GSL_CXX_STANDARD", "cxxstd"))
        return args
