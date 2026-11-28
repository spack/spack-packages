# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCudaCore(PythonPackage):
    """Pythonic access to NVIDIA's CUDA Runtime and other core functionalities"""

    homepage = "https://github.com/NVIDIA/cuda-python"
    git = "https://github.com/NVIDIA/cuda-python"
    url = "https://github.com/NVIDIA/cuda-python/archive/refs/tags/cuda-core-v0.5.1.tar.gz"

    version("0.5.1", sha256="c58f780e6b996bda0d2e64d0e21afa9d1193739ba290b1ec1323822551a589d5")

    license("Apache-2.0")

    depends_on("py-cython@3.2:3.2", type="build")
    depends_on("py-setuptools@77.0.0:", type="build")
    depends_on("py-pyclibrary", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pywin32", when="platform=windows", type=("build", "run"))
    depends_on("py-cuda-bindings", type=("build", "run"))
    depends_on("py-numpy", type="run")

    build_directory = "cuda_core"

    def setup_build_environment(self, env):
        bindings_version = str(self.spec["py-cuda-bindings"].version)
        cuda_major = bindings_version.split(".")[0]
        cuda_prefix = self.spec["cuda"].prefix

        env.set("CUDA_CORE_BUILD_MAJOR", cuda_major)
        env.append_path("LIBRARY_PATH", cuda_prefix.lib64)
