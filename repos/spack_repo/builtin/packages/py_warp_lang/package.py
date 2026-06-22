# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class PyWarpLang(PythonPackage, CudaPackage):
    """A Python framework for high-performance simulation and graphics programming"""

    homepage = "https://developer.nvidia.com/warp-python"

    url = "https://github.com/NVIDIA/warp/archive/refs/tags/v1.12.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.14.0", sha256="bacae67709fb87f6cc03cda78f93e466a0a076580eb815294e2629a6aaacfc0d")
    version("1.13.0", sha256="0dc0e64cfe1f8b2465a02fe46d2cbb0557be483775ea0b57ceec9ac099af9c59")
    version("1.12.0", sha256="c5d2628781a2376e8a6e7d7bb169753b0e2537a31d78f2f1a6800498bfb0c1c8")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        depends_on("cuda")
        depends_on("py-setuptools@75.3.2:")
        depends_on("py-wheel")
        depends_on("py-build")
        # To build local llvm
        depends_on("ninja")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("nvidia-libmathdx")

    patch("clang_cpp.patch")

    phases = ["build", "install"]

    resource(
        name="llvm",
        url="https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-21.1.0.tar.gz",
        sha256="fba0618cf8de48ec05880c446edd756a2669157eab9d29949e971c77da10275f",
        destination="external",
        when="@1.14.0",
    )

    def build(self, spec, prefix):
        python = spec["python"].command
        python(
            "build_lib.py",
            "--libmathdx-path",
            f"{spec['nvidia-libmathdx'].prefix}",
            "--cuda-path",
            f"{spec['cuda'].prefix}",
            "--llvm-source-path",
            f"{self.stage.source_path}/external/llvm-project-llvmorg-21.1.0",
            "--build-llvm",
        )
