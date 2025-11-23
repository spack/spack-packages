# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LlamaCpp(CMakePackage):
    """LLM inference in C/C++"""

    homepage = "https://github.com/ggml-org/llama.cpp"
    git = "https://github.com/ggml-org/llama.cpp.git"

    maintainers("rbberger")

    license("MIT")

    version("master", branch="master")
    version("7086" tag="b7086", commit="7aaeedc098a77e9323044187101db4f6b69988da")
    version("6999", tag="b6999", commit="cb1adf885105da7ce23db746b4202f4e987aa3e8")

    variant("shared", default=True, description="build shared libraries")
    variant("curl", default=True, description="use curl for model download")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("git", type="build")

    depends_on("curl", when="+curl")
    depends_on("ggml")

    depends_on("ggml@0.9.4-20251117:", when="@7086:")

    # Fixes RPC tool install https://github.com/ggml-org/llama.cpp/pull/17149
    patch(
        "https://github.com/ggml-org/llama.cpp/commit/d2d626938aa7b0137df6a808e0637151806a9d5a.patch?full_index=1",
        sha256="ad664f362da58313f5230c2c895da0201b3c2ba120c6d7072563b30f387f8fe3",
        when="@:7019 ^ggml+rpc",
    )

    def cmake_args(self):
        args = [
            self.define("LLAMA_USE_SYSTEM_GGML", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("LLAMA_USE_CURL", "curl"),
        ]
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if os.path.exists(self.prefix.lib64):
            env.set("LLAMA_CPP_LIB_PATH", self.prefix.lib64)
        else:
            env.set("LLAMA_CPP_LIB_PATH", self.prefix.lib)
