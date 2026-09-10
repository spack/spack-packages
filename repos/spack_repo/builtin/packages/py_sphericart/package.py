# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphericart(PythonPackage):
    """Library for the efficient calculation of spherical harmonics
    and their derivatives in Cartesian coordinates."""

    homepage = "https://sphericart.readthedocs.io/en/latest/index.html"
    pypi = "sphericart/sphericart-1.0.3.tar.gz"
    git = "https://github.com/lab-cosmo/sphericart.git"

    maintainers("RMeli", "luthaf", "HaoZeke", "rubber-duck-debug")

    version("1.0.5", sha256="b1e424d85f2460bf1884f0e42355af7c846e23c4a8789a0aca545e8117edbc6e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # pyproject.toml
    with default_args(type="build"):
        depends_on("py-wheel@0.36:")
        depends_on("py-setuptools@44:")
        depends_on("cmake@3.30:")

    depends_on("py-numpy", type=("build", "run"))

    def setup_build_environment(self, env):
        # Prevent sphericart to accidentally pick up CUDA
        env.unset("CUDA_HOME")
