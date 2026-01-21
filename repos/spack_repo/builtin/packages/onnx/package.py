# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Onnx(CMakePackage):
    """Open Neural Network Exchange (ONNX).

    ONNX provides an open source format for AI models, both deep learning and
    traditional ML. It defines an extensible computation graph model, as well
    as definitions of built-in operators and standard data types."""

    homepage = "https://github.com/onnx/onnx"
    url = "https://github.com/onnx/onnx/archive/refs/tags/v1.9.0.tar.gz"
    git = "https://github.com/onnx/onnx.git"

    license("Apache-2.0", checked_by="wdconinc")

    maintainers("wdconinc")

    version("main", branch="main")
    version("master", branch="master", deprecated=True)
    version("1.19.1", sha256="ce9d2569a61d64e8a3d05b92194f60ffb7c868dbb754a71f5b4d992273a9413d")
    version("1.19.0", sha256="2c2ac5a078b0350a0723fac606be8cd9e9e8cbd4c99bab1bffe2623b188fd236")
    version("1.18.0", sha256="b466af96fd8d9f485d1bb14f9bbdd2dfb8421bc5544583f014088fb941a1d21e")
    version("1.17.0", sha256="8d5e983c36037003615e5a02d36b18fc286541bf52de1a78f6cf9f32005a820e")
    version("1.16.2", sha256="84fc1c3d6133417f8a13af6643ed50983c91dacde5ffba16cc8bb39b22c2acbb")
    version("1.16.1", sha256="0e6aa2c0a59bb2d90858ad0040ea1807117cc2f05b97702170f18e6cd6b66fb3")
    version("1.16.0", sha256="0ce153e26ce2c00afca01c331a447d86fbf21b166b640551fe04258b4acfc6a4")
    version("1.15.0", sha256="c757132e018dd0dd171499ef74fca88b74c5430a20781ec53da19eb7f937ef68")
    version("1.14.1", sha256="e296f8867951fa6e71417a18f2e550a730550f8829bd35e947b4df5e3e777aa1")
    version("1.14.0", sha256="1b02ad523f79d83f9678c749d5a3f63f0bcd0934550d5e0d7b895f9a29320003")
    version(
        "1.13.1", sha256="090d3e10ec662a98a2a72f1bf053f793efc645824f0d4b779e0ce47468a0890e"
    )  # py-torch@2:
    version("1.13.0", sha256="66eb61fc0ff4b6189816eb8e4da52e1e6775a1c29f372cbd08b694aa5b4ca978")
    version("1.12.0", sha256="052ad3d5dad358a33606e0fc89483f8150bb0655c99b12a43aa58b5b7f0cc507")
    version(
        "1.11.0", sha256="a20f2d9df805b16ac75ab4da0a230d3d1c304127d719e5c66a4e6df514e7f6c0"
    )  # py-torch@1.12:
    version("1.10.2", sha256="520b3aa34272cc215e2eb41385f58adf01750d88858d4722563edca8410c5dc9")
    version(
        "1.10.1_2021-10-08", commit="85546f8c44e627f8ff1181725d03cc49f675e44f"
    )  # py-torch@1.11
    version(
        "1.10.1", sha256="cb2fe3e0c9bba128a5790a565d81be30f4b5571eaca5418fb19df8d2d0f11ce2"
    )  # py-torch@1.10
    version("1.10.0", sha256="705a27ee076713b8c755911913c9ffa8f96b95fc3a8568ed0b8e1dd954d67147")
    version("1.9.0", sha256="61d459a5f30604cabec352574119a6685dfd43bfa757cfbff52be9471d5b8ea0")
    version(
        "1.8.0_2020-11-03", commit="54c38e6eaf557b844e70cebc00f39ced3321e9ad"
    )  # py-torch@1.8:1.9
    version(
        "1.7.0_2020-05-31", commit="a82c6a7010e2e332d8f74ad5b0c726fd47c85376"
    )  # py-torch@1.6:1.7
    version("1.6.0_2020-02-16", commit="9fdae4c68960a2d44cd1cc871c74a6a9d469fa1f")  # py-torch@1.5
    version("1.6.0_2019-11-06", commit="fea8568cac61a482ed208748fdc0e1a8e47f62f5")  # py-torch@1.4

    depends_on("c", type="build", when="@:1.18")
    depends_on("cxx", type="build")

    generator("ninja")
    depends_on("cmake@3.1:", type="build")
    depends_on("cmake@3.14:", type="build", when="@1.17:")
    depends_on("cmake@3.26:", type="build", when="@1.20:")
    depends_on("python", type="build")
    depends_on("protobuf")

    # Allow conversion from OpSchema to OpSchemaRegisterOnce (needed for onnxruntime)
    # Ref: https://github.com/onnx/onnx/pull/7390
    patch("OpSchemaRegisterOnce.patch", when="@1.18.0:1.19")

    def patch(self):
        if self.spec.satisfies("@1.13:1.14 ^protobuf@22:"):
            # CMAKE_CXX_STANDARD is overridden in CMakeLists.txt until 1.14
            cxxstd = self.spec["abseil-cpp"].variants["cxxstd"].value
            filter_file("CMAKE_CXX_STANDARD 11", f"CMAKE_CXX_STANDARD {cxxstd}", "CMakeLists.txt")

    def cmake_args(self):
        # https://github.com/pytorch/pytorch/blob/main/cmake/Dependencies.cmake
        args = [
            self.define("BUILD_SHARED_LIBS", False),
            self.define("ONNXIFI_ENABLE_EXT", True),
            # Try to get ONNX to use the same version of python as the spec is using
            self.define("PY_VERSION", self.spec["python"].version.up_to(2)),
            self.define("ONNX_BUILD_TESTS", self.run_tests),
            self.define(
                "ONNX_USE_PROTOBUF_SHARED_LIBS", self.spec["protobuf"].variants["shared"].value
            ),
        ]
        if self.spec.satisfies("@1.15: ^protobuf@22:"):
            # CMAKE_CXX_STANDARD can be set on command line as of 1.15
            cxxstd = self.spec["abseil-cpp"].variants["cxxstd"].value
            args.append(self.define("CMAKE_CXX_STANDARD", cxxstd))
        return args
