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
    depends_on("py-torch@2.1:2.9", type=("build", "run"))

    def setup_build_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        else:
            env.unset("CUDA_HOME")
