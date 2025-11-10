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

    version("1.0.5", sha256="b1e424d85f2460bf1884f0e42355af7c846e23c4a8789a0aca545e8117edbc6e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # pyproject.toml
    depends_on("py-wheel@0.36:", type="build")
    depends_on("py-setuptools@77:", type="build")
    depends_on("cmake@3.30:", type="build")
    depends_on("py-numpy", type=("build", "run"))

    # setup.py
    depends_on("py-torch@2.1:2.9", type=("build", "run"))

    def setup_build_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        else:
            env.unset("CUDA_HOME")
