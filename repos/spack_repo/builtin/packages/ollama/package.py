# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import go
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Ollama(GoPackage, CudaPackage):
    """Run Llama 2, Code Llama, and other models. Customize and create your own."""

    homepage = "https://ollama.com"
    git = "https://github.com/ollama/ollama.git"

    maintainers("teaguesterling", "brettviren")

    # A shell script is run by `go generate` which assumes source is in a git
    # repo.  So we must use git VCS and not tarballs and defeat source caching.
    with default_args(no_cache=True):
        version("0.20.7", commit="8d0dcf4b6daf8d7833c8b55108e5b45063795e57")
        version("0.13.1", commit="5317202c38437867bc6c9ed21ffc5c949ab6794c")
        version("0.12.11", commit="c1149875234a51aa1e5e60b74f3807f5982c60fa")
        version("0.11.11", commit="92b96d54efd6b49322b7cf046f9a0dc16b00cd0a")
        version("0.10.1", commit="ff89ba90bc97e9f58b8378a664b904bbc94e6f26")
        version("0.9.6", commit="43107b15b9bcff51ef1c5391c273fd1a747f6d0a")
        version("0.8.0", commit="aa25aff10d1ccc6dd4e85952678d63946bdf89dc")
        version("0.7.1", commit="884d26093c80491a3fe07f606fc04851dc317199")
        version("0.6.8", commit="6a74bba7e7e19bf5f5aeacb039a1537afa3522a5")
        version("0.5.13", commit="7a01ad76143973199bd6965c13476d2d04f10f75")
        version("0.4.7", commit="5f8051180e3b9aeafc153f6b5056e7358a939c88")
        version("0.4.2", commit="d875e99e4639dc07af90b2e3ea0d175e2e692efb")
    # Submodule llm/llama.cpp
    with default_args(submodules=True, no_cache=True):
        version("0.3.9", commit="a1cef4d0a5f31280ea82b350605775931a6163cb")
        version("0.1.31", commit="dc011d16b9ff160c0be3829fc39a43054f0315d0")
        # This is the last verified non-preview version as of 20240413
        version("0.1.30", commit="756c2575535641f1b96d94b4214941b90f4c30c7")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    license("MIT", checked_by="teaguesterling")

    depends_on("cmake@3.24:", type="build")
    depends_on("go", type="build")
    depends_on("go@1.22.0:", type="build", when="@0.1.29:")
    depends_on("go@1.22.5:", type="build", when="@0.3.6:")
    depends_on("go@1.22.8:", type="build", when="@0.4.0:")
    depends_on("go@1.23.4:", type="build", when="@0.5.2:")
    depends_on("go@1.24.0:", type="build", when="@0.5.13:")
    depends_on("go@1.24.1:", type="build", when="@0.12.10:")
    depends_on("git", type="build")


class GoBuilder(go.GoBuilder):
    phases = ("generate", "build", "install")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+cuda"):
            # These variables are consumed by gen_linux.sh which is called by
            # "go generate".
            cuda_prefix = self.spec["cuda"].prefix
            env.set("CUDACXX", cuda_prefix.bin.nvcc)
            env.set("CUDA_LIB_DIR", cuda_prefix.lib)
            env.set("CMAKE_CUDA_ARCHITECTURES", self.spec.variants["cuda_arch"].value)

    @property
    def generate_args(self):
        """Arguments for ``go generate``."""
        return ["./..."]

    def generate(self, pkg, spec, prefix):
        """Runs ``go generate`` in the source directory"""
        with working_dir(self.build_directory):
            go("generate", *self.generate_args)
