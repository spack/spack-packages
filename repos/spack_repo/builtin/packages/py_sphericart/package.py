# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class PySphericart(PythonPackage, CudaPackage):
    """Library for the efficient calculation of spherical harmonics
    and their derivatives in Cartesian coordinates."""

    homepage = "https://sphericart.readthedocs.io/en/latest/index.html"
    pypi = "sphericart/sphericart-1.0.3.tar.gz"
    git = "https://github.com/lab-cosmo/sphericart.git"

    maintainers("RMeli", "luthaf", "HaoZeke", "rubber-duck-debug")

    version("1.0.3", sha256="007b21f075d5ba331519fe5cec6acf28d5bd458a970a158973d51047795afd12")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("py-wheel@0.36:", type="build")
    depends_on("py-setuptools@44:", type="build")

    depends_on("py-numpy", type=("build", "run"))

    def setup_build_environment(self, env):
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_HOME", self.spec["cuda"].prefix)
        else:
            env.unset("CUDA_HOME")
