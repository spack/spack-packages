# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Rocmlir(CMakePackage):
    """This is the repository for a MLIR-based convolution and GEMM kernel generator
    targetting AMD hardware. This generator is mainly used from MIOpen and MIGraphX,
    but it can be used on a standalone basis."""

    homepage = "https://github.com/ROCm/rocMLIR"
    git = "https://github.com/ROCm/rocMLIR.git"
    url = "https://github.com/ROCm/rocMLIR/archive/refs/tags/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "afzpatel", "renjithravindrankannath")

    version("7.2.0", sha256="7349cf8ccf7bb612e24168b4be2e7312f243e1603907613edf6d2ec8e71f7801")
    version("7.1.1", sha256="e5fb89f55b6d5abf1be85cc35a68bc496d908fdf9b9c51ad44ac3cbf67aa35ee")
    version(
        "7.1.0",
        url="https://github.com/ROCm/rocMLIR/archive/refs/tags/rocm-7.1.tar.gz",
        sha256="2e57ff0b098ebe67fca02ef65cb2e1a44f3aaa6d23456d747c4c8c0df24f9d50",
    )
    version("7.0.2", sha256="01e4b5c3f22c23595816a8c16e3ec67d39c7c5f63ecfa2d8a641ef65a9b79d50")
    version(
        "7.0.0",
        url="https://github.com/ROCm/rocMLIR/archive/refs/tags/rocm-7.0.1.tar.gz",
        sha256="84ac7addddb184599d8aa3cc9fd3ff62f177f73a8e484fb7bbed11330dc87288",
    )
    version("6.4.3", sha256="5f48cdbb35738223d18f92fd4624a270e20afcc3f67aaae75b76b09b9a3865e6")
    version("6.4.2", sha256="9ad8e64a01902771255371fdd08de7e574bbe71c00245837173d42f54a7599e9")
    version("6.4.1", sha256="15cb80da488f88274afff358e6706f54139d1003a9ddcc918afc58af4ebc5c6a")
    version("6.4.0", sha256="e377ad70fd5a5723427edf9464dde8e7892dabd1f783123d39a2fa2faf87079f")
    version("6.3.3", sha256="87242b811536132a02ce79fe430c70485f9b1477de22d8376e7e923a9c9ad98b")
    version("6.3.2", sha256="5911e880a66faecb08d242efa3e5eb6f8ce32cb21ea09dec36f4aef111c395fb")
    version("6.3.1", sha256="b9e0ea8cfb83c20553b1ec1556752958afaa421a8d7326b1da748395ba7b75ac")
    version("6.3.0", sha256="8dd167250e138fac0609f4ed06fc6a4dca5edad346166a291f20b4dad99bbd0b")
    version("6.2.4", sha256="3283685431fd59e20a6ac5737df22c7c7421901779a2a0b6dbd6c1ab1f1b5adb")
    version("6.2.1", sha256="eff594c6b6b97ac21bf268da49fcd016584cfe28c8ff64b0a20b8a9144dca683")
    version("6.2.0", sha256="889e021edab19657947716e0056176ca0298602a21c4b77e7e7b00467fdaa175")
    version("6.1.2", sha256="9bde02b898896301a30e7007e384b9de9cf8feac04f44c91a3b625e74788fda6")
    version("6.1.1", sha256="0847fd2325fb287538442cf09daf7fa76e7926a40eafd27049e0b5320371c1b5")
    version("6.1.0", sha256="dd800783f1ce66ce7c560d5193d053ddf3797abae5ec9375c9842243f5a8ca0b")
    version("6.0.2", sha256="6ed039e8045169bb64c10fb063c2e1753b8d52d6d56c60e001c929082be1f20b")
    version("6.0.0", sha256="128915abdceaf5cef26a717d154f2b2f9466f6904f4490f158038878cedbf618")

    variant(
        "build_type",
        default="Release",
        values=("Release", "Debug", "RelWithDebInfo"),
        description="CMake build type",
    )

    def patch(self):
        filter_file(
            "${ROCM_PATH}/bin",
            self.spec["rocminfo"].prefix.bin,
            "external/llvm-project/mlir/lib/ExecutionEngine/CMakeLists.txt",
            string=True,
        )

    generator("ninja")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("ncurses+termlib", type="link")
    depends_on("bzip2")
    depends_on("sqlite")
    depends_on("half")
    depends_on("pkgconfig", type="build")

    for ver in [
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", type="build", when=f"@{ver}")
        depends_on(f"rocminfo@{ver}", type="build", when=f"@{ver}")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define(
                "CMAKE_CXX_COMPILER", "{0}/bin/clang++".format(spec["llvm-amdgpu"].prefix)
            ),
            self.define("CMAKE_C_COMPILER", "{0}/bin/clang".format(spec["llvm-amdgpu"].prefix)),
            self.define("HIP_PATH", spec["hip"].prefix),
            self.define("BUILD_FAT_LIBROCKCOMPILER", "ON"),
        ]
        return args
