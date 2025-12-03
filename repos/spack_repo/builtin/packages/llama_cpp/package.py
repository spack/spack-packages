# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack_repo.builtin.packages.ggml.package import GGMLPackageBase

from spack.package import *


class LlamaCpp(GGMLPackageBase):
    """LLM inference in C/C++"""

    homepage = "https://github.com/ggml-org/llama.cpp"
    git = "https://github.com/ggml-org/llama.cpp.git"

    maintainers("rbberger")

    license("MIT")

    version("master", branch="master")
    version("7158", tag="b7158", commit="b3b03a7baf387cfeaf56641bd14c06dbd3d2fcf0")
    version("7086", tag="b7086", commit="7aaeedc098a77e9323044187101db4f6b69988da")

    variant("curl", default=True, description="use curl for model download")
    variant("system_ggml", default=False, description="use external GGML library")

    depends_on("curl", when="+curl")
    depends_on("ggml", when="+system_ggml")

    for v in ("cpu", "blas", "openmp", "cuda", "rocm", "metal", "rpc"):
        depends_on(f"ggml+{v}", when=f"+system_ggml +{v}")
        depends_on(f"ggml~{v}", when=f"+system_ggml ~{v}")

    for _flag in list(CudaPackage.cuda_arch_values):
        depends_on(f"ggml cuda_arch={_flag}", when=f"+cuda+system_ggml cuda_arch={_flag}")

    for _flag in ROCmPackage.amdgpu_targets:
        depends_on(f"ggml amdgpu_target={_flag}", when=f"+rocm+system_ggml amdgpu_target={_flag}")

    def cmake_args(self):
        args = [
            self.define_from_variant("LLAMA_USE_SYSTEM_GGML", "system_ggml"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("LLAMA_USE_CURL", "curl"),
        ]

        if self.spec.satisfies("~system_ggml"):
            args.extend(super().cmake_args())
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if os.path.exists(self.prefix.lib64):
            env.set("LLAMA_CPP_LIB_PATH", self.prefix.lib64)
        else:
            env.set("LLAMA_CPP_LIB_PATH", self.prefix.lib)
