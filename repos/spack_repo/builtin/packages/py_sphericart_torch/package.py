# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphericartTorch(PythonPackage, CudaPackage):
    """Library for the calculation of spherical harmonics in Cartesian coordinates"""

    homepage = "https://sphericart.readthedocs.io/en/latest/"
    pypi = "sphericart_torch/sphericart_torch-0.0.0.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke", "rubber-duck-debug")

    version("2.0.3", sha256="38f77367896ef1c7f347278ca8b65b1b973937b27458cfc75f2e66122744f91b")
    version("2.0.2", sha256="8cf7413b30d134591baf5b1b1bac20fe107b44a9afb0600ec849a664308ab4ae")
    version("2.0.1", sha256="f622f4c575e5b91b3b65641d25b59ea36e96fbc81c872d2e0ffbb50e00f40821")
    version("2.0.0", sha256="b9b2cd3038402b62b93dd38f708d12faf7645db88685940a045af4a0e4468783")
    version("1.0.9", sha256="35ed803da2a4e09c5c6eb378e25942f9be86a85085132b9b797e478622915059")
    version("1.0.8", sha256="332c550cd23e584a46e9a954327e97882b9efde7648c8fc1bafc335266ee4bc1")
    version("1.0.7", sha256="05381e042294eb6befcad6df4d8a8a9d913e410f2c91b9da79bdb44e86754ed7")
    version("1.0.6", sha256="e601371962f5f97afd3a39e5eefa6daf06d4653e6b0104d37932954223960ccf")
    version("1.0.5", sha256="d58c372395236b339837ee35b19933fca0c9803dcecabb213bedc51178e764a3")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # pyproject.toml
    with default_args(type="build"):
        depends_on("py-wheel@0.36:")
        depends_on("py-setuptools@77:")
        depends_on("cmake@3.30:")
    depends_on("py-numpy", type=("build", "run"))

    # setup.py
    depends_on("py-torch@2.6:", type=("build", "run"))

    def setup_build_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        else:
            env.unset("CUDA_HOME")
