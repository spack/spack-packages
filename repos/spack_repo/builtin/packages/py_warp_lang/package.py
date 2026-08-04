# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWarpLang(PythonPackage, CudaPackage):
    """A Python framework for high-performance simulation and graphics programming"""

    homepage = "https://developer.nvidia.com/warp-python"

    url = "https://github.com/NVIDIA/warp/archive/refs/tags/v1.12.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.14.0", sha256="bacae67709fb87f6cc03cda78f93e466a0a076580eb815294e2629a6aaacfc0d")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cuda", when="+cuda")
        depends_on("py-setuptools@75.3.2:")
        depends_on("py-wheel")
        depends_on("py-build")
        # To build local llvm
        depends_on("cmake@3.20:")
        depends_on("ninja")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("nvidia-libmathdx")

    patch("clang_cpp.patch")

    resource(
        name="llvm",
        url="https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-21.1.0.tar.gz",
        sha256="fba0618cf8de48ec05880c446edd756a2669157eab9d29949e971c77da10275f",
        destination="external",
        when="@1.14.0",
    )

    @run_before("install")
    def build_lib(self):
        spec = self.spec
        python = spec["python"].command
        build_command = ["build_lib.py"]
        build_command += ["--libmathdx-path", f"{spec['nvidia-libmathdx'].prefix}"]
        if spec.satisfies("+cuda"):
            build_command += ["--cuda-path", f"{spec['cuda'].prefix}"]
        build_command += [
            "--llvm-source-path",
            f"{self.stage.source_path}/external/llvm-project-llvmorg-21.1.0",
            "--build-llvm",
        ]
        python(*build_command)
