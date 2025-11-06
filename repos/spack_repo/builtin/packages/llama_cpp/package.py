# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class LlamaCpp(CMakePackage, CudaPackage):
    """LLM inference in C/C++."""

    homepage = "https://github.com/ggml-org/llama.cpp"
    url = "https://github.com/ggml-org/llama.cpp"
    git = "https://github.com/ggml-org/llama.cpp"

    license("MIT", checked_by="aweits")

    variant("rpc", default=True, description="enable RPC in ggml")

    depends_on("cuda")
    depends_on("curl")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    version("master")
    version("2025-11-03", commit="c5023daf607c578d6344c628eb7da18ac3d92d32")
    version("2025-08-29", commit="009b709d6efd24820ac67765ed339a72dc797814")

    def patch(self):
        filter_file(
            "target_compile_features(${TARGET} PRIVATE cxx_std_17)",
            "target_compile_features(${TARGET} PRIVATE cxx_std_17)\n"
            "if(LLAMA_TOOLS_INSTALL)\n"
            "install(TARGETS ${TARGET} RUNTIME)\n"
            "endif()\n",
            "tools/rpc/CMakeLists.txt",
            string=True,
        )

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+cuda"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            args.append("-DGGML_CUDA=1")
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", ";".join(cuda_arch)))
        if self.spec.satisfies("+rpc"):
            args.append("-DGGML_RPC=1")

        return args
