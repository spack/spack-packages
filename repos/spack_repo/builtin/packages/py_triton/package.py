# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyTriton(PythonPackage, CudaPackage, ROCmPackage):
    """A language and compiler for custom Deep Learning operations."""

    homepage = "https://github.com/triton-lang/triton"
    url = "https://github.com/triton-lang/triton/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/triton-lang/triton.git"

    maintainers("thomas-bouvier")

    license("MIT")

    #version("main", branch="main")
    version("3.4.0", sha256="a96e87a911794c907fab30e0c7a3f96ef4e9e8fdc8812cd8bbc6f0457619072f")
    version("3.3.1", sha256="9dc77d9205933bf2fc05eb054f4f1d92acd79a963826174d57fe9cfd58ba367b")
    version("3.2.0", sha256="04eb07e2ff1b87bf4b26e132d696177248bfb9c71cecd4864e561a9c103de9b3")
    version("2.1.0", sha256="4338ca0e80a059aec2671f02bfc9320119b051f378449cf5f56a1273597a3d99")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        # https://github.com/triton-lang/triton/blob/v3.3.1/python/requirements.txt
        depends_on("cmake@3.18:3")
        depends_on("ninja@1.11.1:")
        depends_on("py-setuptools@40.8.0:")
        depends_on("py-pybind11@2.13.1:")
        depends_on("py-lit")

        # By default, the following dependencies are downloaded in the setup.py.
        # We want to manage such dependencies from within Spack.
        # The mapping between the LLVM and Triton is documented in file cmake/llvm-hash.txt.
        # This file pins commit ids, we are using plain LLVM versions instead (the one
        # closest to the commit id).
        #depends_on("llvm@main +mlir +utils", when="@main")
        depends_on("llvm@21.1.0-rc-triton-v3.4.0 +mlir +utils", when="@3.4.0")
        depends_on("llvm@21.1.0-rc-triton-v3.3.1 +mlir +utils", when="@3.3.1")
        depends_on("llvm@20.1.0-rc-triton-v3.2.0 +mlir +utils", when="@3.2.0")
        depends_on("llvm@13 +mlir +utils", when="@2.1.0")
        depends_on("nlohmann-json@3.11.3", when="@3:")
        depends_on("py-pybind11")
        #depends_on("roctracer-dev")
        depends_on("cuda@10:")

    depends_on("py-setuptools@40.8.0:", type="run", when="@3.2.0")
    depends_on("py-filelock", type=("build", "run"))
    depends_on("zlib-api", type="link")
    conflicts("^openssl@3.3.0")

    @run_before("install")
    def create_cuda_include_dir(self):
        """Create a merged include directory with both CUDA and CUPTI headers.

        Triton's Proton component uses CUPTI_INCLUDE_DIR as its only include
        search path, but expects both cupti.h (from extras/CUPTI/include) and
        cuda.h (from include) to be found there. In a standard CUDA toolkit
        these headers live in separate directories, so we create a staging
        directory with symlinks to both.

        This must run as a build phase (not in setup_build_environment) because
        setup_build_environment executes before the stage is finalized, and
        any files created there may be destroyed during restaging.
        """
        cuda = self.spec["cuda"].prefix
        merged_dir = os.path.join(self.stage.path, "cuda-include")
        mkdirp(merged_dir)

        # Collect all include directories to merge.
        # The main CUDA include dir contains cuda.h, cuda_runtime.h, etc.
        # The CUPTI include dir contains cupti.h, cupti_activity.h, etc.
        # CUPTI headers take priority if there are overlaps.
        include_dirs = [
            os.path.join(str(cuda), "include"),
            os.path.join(str(cuda), "extras", "CUPTI", "include"),
        ]

        for include_dir in include_dirs:
            if not os.path.isdir(include_dir):
                tty.warn(f"CUDA include directory not found: {include_dir}")
                continue
            for entry in os.listdir(include_dir):
                src = os.path.join(include_dir, entry)
                dst = os.path.join(merged_dir, entry)
                if os.path.lexists(dst):
                    os.remove(dst)
                symlink(src, dst)

        # Verify that the critical headers are present
        for header in ("cuda.h", "cupti.h"):
            if not os.path.exists(os.path.join(merged_dir, header)):
                raise RuntimeError(
                    f"{header} not found in merged include directory {merged_dir}. "
                    f"Searched: {include_dirs}"
                )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set environment variables used to control the build"""
        if self.spec.satisfies("%clang"):
            env.set("TRITON_BUILD_WITH_CLANG_LLD", "True")
        env.set("TRITON_OFFLINE_BUILD", "True")
        env.set("LLVM_SYSPATH", self.spec["llvm"].prefix)
        env.set("JSON_SYSPATH", self.spec["nlohmann-json"].prefix)
        env.set("PYBIND11_SYSPATH", self.spec["py-pybind11"].prefix)
        #env.set("TRITON_ROCTRACER_INCLUDE_PATH", self.spec["roctracer-dev"].prefix.include)

        cuda = self.spec["cuda"].prefix
        env.set("TRITON_PTXAS_PATH", cuda.bin.ptxas)
        env.set("TRITON_CUOBJDUMP_PATH", cuda.bin.cuobjdump)
        env.set("TRITON_NVDISASM_PATH", cuda.bin.nvdisasm)
        env.set("TRITON_CUDACRT_PATH", cuda.join("include"))
        env.set("TRITON_CUDART_PATH", cuda.join("include"))

        # Point to the merged include directory that will be created by
        # create_cuda_include_dir (a @run_before("install") phase).
        # The env var is set here so it's available to the build subprocess;
        # the directory itself is created later, after staging is complete.
        env.set("TRITON_CUPTI_INCLUDE_PATH", os.path.join(self.stage.path, "cuda-include"))
        env.set("TRITON_CUPTI_LIB_PATH", os.path.join(str(cuda), "extras", "CUPTI", "lib64"))

        # Force Spack's compilers.  Triton's setup.py runs CMake under the
        # hood and LLVM's exported CMake config can override the compiler to
        # the clang that LLVM was built with.  TRITON_APPEND_CMAKE_ARGS is
        # appended last to the cmake invocation (see setup.py) and therefore
        # takes precedence.
        env.set("TRITON_APPEND_CMAKE_ARGS",
                f"-DCMAKE_C_COMPILER={self.compiler.cc} "
                f"-DCMAKE_CXX_COMPILER={self.compiler.cxx} "
                f"-DCMAKE_LINKER_TYPE=DEFAULT "
                f"-DZLIB_ROOT={self.spec['zlib-api'].prefix}")

    @property
    def build_directory(self):
        return "." if self.spec.satisfies("@3.4.0:") else "python"
