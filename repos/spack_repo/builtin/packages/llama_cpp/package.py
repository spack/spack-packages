# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LlamaCpp(CMakePackage):
    """LLM inference in C/C++"""

    homepage = "https://github.com/ggml-org/llama.cpp"
    git = "https://github.com/ggml-org/llama.cpp.git"

    maintainers("rbberger")

    license("MIT")

    version("master", branch="master")
    version("6999", tag="b6999", commit="cb1adf885105da7ce23db746b4202f4e987aa3e8")

    variant("shared", default=True, description="build shared libraries")
    variant("curl", default=True, description="use curl for model download")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("git", type="build")

    depends_on("curl", when="+curl")
    depends_on("ggml")

    def cmake_args(self):
        args = [
            self.define("LLAMA_USE_SYSTEM_GGML", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("LLAMA_USE_CURL", "curl"),
        ]
        return args
