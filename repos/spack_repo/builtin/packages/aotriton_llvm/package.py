# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class AotritonLlvm(CMakePackage, CudaPackage, CompilerPackage):

    homepage = "https://github.com/llvm/llvm-project"
    url = "https://github.com/llvm/llvm-project/archive/llvmorg-7.1.0.tar.gz"
    git = "https://github.com/llvm/llvm-project"
    # url = "https://oaitriton.blob.core.windows.net/public/llvm-builds/llvm-86b69c31-ubuntu-x64.tar.gz"

    version("main", branch="main")
    version("20.1.0", commit="86b69c31642e98f8357df62c09d118ad1da4e16a")
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

    root_cmakelists_dir = "llvm"

    def _standard_flag(self, *, language, standard):
        flags = {
            "cxx": {"11": "-std=c++11", "14": "-std=c++14", "17": "-std=c++17"},
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
