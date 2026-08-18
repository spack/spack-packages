# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class WhisperCpp(CMakePackage, CudaPackage):
    """High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model"""

    homepage = "https://github.com/ggml-org/whisper.cpp"
    url = "https://github.com/ggml-org/whisper.cpp/archive/refs/tags/v1.8.2.tar.gz"
    git = "https://github.com/ggml-org/whisper.cpp"

    license("MIT", checked_by="aweits")

    variant("sdl2", default=False, description="sdl2/streaming support")

    depends_on("cuda")
    depends_on("curl")
    depends_on("sdl2", when="+sdl2")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    version("master")
    version("1.8.2", sha256="bcee25589bb8052d9e155369f6759a05729a2022d2a8085c1aa4345108523077")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+cuda"):
            args.append("-DGGML_CUDA=1")
        if self.spec.satisfies("+sdl2"):
            args.append("-DWHISPER_SDL2=ON")
        return args
