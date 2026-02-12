# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class AotritonLlvm(CMakePackage, CudaPackage, CompilerPackage):
    """Package for aotriton-llvm: A custom LLVM build for AoTriton."""

    homepage = "https://github.com/llvm/llvm-project"
    git = "https://github.com/llvm/llvm-project"
    url = "https://github.com/llvm/llvm-project/archive/llvmorg-7.1.0.tar.gz"
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("Apache-2.0")

    version("main", commit="b5cc222d7429fe6f18c787f633d5262fac2e676f")
    version("0.10", commit="3c709802d31b5bc5ed3af8284b40593ff39b9eec")
    version("0.9", commit="86b69c31642e98f8357df62c09d118ad1da4e16a")
    version("0.8", commit="bd9145c8c21334e099d51b3e66f49d51d24931ee")
    generator("ninja")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("cmake@3.13.4:", type="build")
    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("ncurses+termlib", type="link")
    depends_on("libxml2", type="link")
    depends_on("py-pybind11")
    depends_on("pkgconfig", type="build")
    depends_on("py-nanobind", when="@0.10")

    root_cmakelists_dir = "llvm"

    def _standard_flag(self, *, language, standard):
        flags = {
            "cxx": {
                "11": "-std=c++11",
                "14": "-std=c++14",
                "17": "-std=c++17",
                "20": "-std=c++20",
            },
            "c": {"99": "-std=c99", "11": "-std=c1x"},
        }
        return flags[language][standard]

    def cmake_args(self):
        llvm_projects = ["llvm", "mlir"]
        args = [
            self.define("LLVM_ENABLE_Z3_SOLVER", "OFF"),
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("LLVM_REQUIRES_RTTI", True),
            self.define("LLVM_ENABLE_LIBXML2", False),
            self.define("LLVM_ENABLE_RTTI", "ON"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("CMAKE_CXX_STANDARD", 17),
            self.define("LLVM_BUILD_UTILS", "ON"),
            self.define("LLVM_TARGETS_TO_BUILD", "host;NVPTX;AMDGPU"),
            self.define("MLIR_ENABLE_BINDINGS_PYTHON", "ON"),
            self.define("LLVM_ENABLE_TERMINFO", "OFF"),
        ]
        args.append(self.define("LLVM_ENABLE_PROJECTS", llvm_projects))
        return args
