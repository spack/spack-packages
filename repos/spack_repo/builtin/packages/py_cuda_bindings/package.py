# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCudaBindings(PythonPackage):
    """NVIDIA’s CUDA Python provides Cython bindings and Python wrappers for the
    driver and runtime API for existing toolkits and libraries to simplify
    GPU-based accelerated processing."""

    homepage = "https://github.com/NVIDIA/cuda-python"
    git = "https://github.com/NVIDIA/cuda-python"
    url = (
        "https://github.com/NVIDIA/cuda-python/releases/download/v12.9.1/cuda-python-v12.9.1.tar.gz"
    )

    version("13.4.4", sha256="d8820a3377ee3a4508c41bf0914a513e3d77b67bc72582d2c1dc6ebc63bcb545")
    version("13.4.3", sha256="a5d776ed2d81ebf43b1b5d8c00d0e75644779e84c1d13b551cf1af98a049a73a")
    version("13.4.2", sha256="b271f2e787212c139e8b867c930ffeab006a00b5eb8e57c9f554889241f849e4")
    version("13.4.1", sha256="0c7bc472dcffc0eedc2973302d9919ce336487ad8078c175c2db115c6330e2fd")
    version("12.9.9", sha256="1ef9eb47ec1106c8c618f960ccefa9f547faa401b13ee65547e97f9b74c06233")
    version("12.9.8", sha256="87f46e7f23cbd6e3434bbbf02a0a1e39c3f849dcc62254d8e502aa80e2ffb86d")
    version("12.9.1", sha256="9c6c2da8ed59851acbb261b5fac80885d9dd2396a8bea0eba67908b811d7bb50")
    version("12.9.0", sha256="1fa57a9fad278256cbb3b6cf347d2b258a7f83bba2759257e54c9fabd0b07ce1")
    version("12.8.0", sha256="6cc8db1e65a1f995e289b64f9b9bff4362321d36ecf9b54eb192d0781475fbca")
    version("11.8.7", sha256="613ec6d0cde3db4d48074010ed6015ff60462f14c5fa7d8fe82fe7a7ecd5d1ac")

    depends_on("cuda@13.4", when="@13.4")
    depends_on("cuda@12.9", when="@12.9")
    depends_on("cuda@12.8", when="@12.8.0")
    depends_on("cuda@11.8", when="@11.8.7")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@77.0.0:", when="@12.9.0", type="build")
    depends_on("py-cython", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-pyclibrary", type=("build", "run"))
    depends_on("py-pywin32", when="platform=windows", type=("build", "run"))

    depends_on("py-cuda-pathfinder@1.1:1", when="@12.9.1:")

    build_directory = "cuda_bindings"

    def setup_build_environment(self, env):
        cuda_version = self.spec["cuda"].version
        if cuda_version >= Version("12.9"):
            env.append_path("LIBRARY_PATH", self.spec["cuda"].prefix.lib64)
