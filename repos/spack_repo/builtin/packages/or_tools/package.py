# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class OrTools(CMakePackage):
    """This project hosts operations research tools developed at
    Google and made available as open source under the Apache 2.0
    License."""

    homepage = "https://developers.google.com/optimization/"
    url = "https://github.com/google/or-tools/archive/v7.8.tar.gz"
    maintainers("hyoklee")

    license("Apache-2.0")

    version("9.14", sha256="9019facf316b54ee72bb58827efc875df4cfbb328fbf2b367615bf2226dd94ca")
    version("7.8", sha256="d93a9502b18af51902abd130ff5f23768fcf47e266e6d1f34b3586387aa2de68")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated
    variant("coin", default=False, description="Enable COIN-OR solvers.")

    depends_on("cmake", type="build")
    depends_on("gflags")
    depends_on("glog")
    depends_on("protobuf@31.1 +shared", when="@9.14:")
    depends_on("abseil-cpp")
    depends_on("eigen", when="@9.14:")
    depends_on("cbc")
    depends_on("cgl")
    depends_on("clp")
    depends_on("osi")
    depends_on("re2", when="@9.14:")

    depends_on("coinutils", when="+coin")
    depends_on("cmake@3.14:", type="build", when="@7.8:")
    depends_on("gflags@2.2.2:", when="@7.8:")
    depends_on("glog@0.4.0:", when="@7.8:")
    depends_on("protobuf@3.12.2:", when="@7.8:")
    depends_on("abseil-cpp@20200225.2:", when="@7.8:")
    depends_on("cbc@2.10.5:", when="@7.8:")
    depends_on("cgl@0.60.3:", when="@7.8:")
    depends_on("clp@1.17.4:", when="@7.8:")
    depends_on("osi@0.108.6:", when="@7.8:")
    depends_on("coinutils@2.11.4:", when="@7.8: +coin")


    def cmake_args(self):
        cmake_args = []
        cmake_args.append(self.define("BUILD_DEPS", False))
        cmake_args.append(self.define("BUILD_PYTHON", False))
        cmake_args.append(self.define_from_variant("USE_COINOR", "coin"))
        cmake_args.append(self.define("USE_HIGHS", False))
        cmake_args.append(self.define("BUILD_HIGHS", False))
        cmake_args.append(self.define("USE_SOPLEX", False))
        cmake_args.append(self.define("BUILD_SOPLEX", False))
        cmake_args.append(self.define("USE_SCIP", False))
        cmake_args.append(self.define("BUILD_SCIP", False))
        cmake_args.append(self.define("BUILD_TESTING", False))

        # Match the C++ standard used by abseil
        cxxstd = self.spec["abseil-cpp"].variants["cxxstd"].value
        cmake_args.append(self.define("CMAKE_CXX_STANDARD", cxxstd))
        return cmake_args
