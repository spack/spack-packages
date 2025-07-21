# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rocmlir(CMakePackage):
    """This is the repository for a MLIR-based convolution and GEMM kernel generator
    targetting AMD hardware. This generator is mainly used from MIOpen and MIGraphX,
    but it can be used on a standalone basis."""

    homepage = "https://github.com/ROCm/rocMLIR"
    git = "https://github.com/ROCm/rocMLIR.git"
    url = "https://github.com/ROCm/rocMLIR/archive/refs/tags/rocm-6.2.1.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "afzpatel", "renjithravindrankannath")

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

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated
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
