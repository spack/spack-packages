# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphericartTorch(PythonPackage):
    """Library for the calculation of spherical harmonics in Cartesian coordinates"""

    homepage = "https://sphericart.readthedocs.io/en/latest/"
    pypi = "sphericart_torch/sphericart_torch-0.0.0.tar.gz"

    maintainers("RMeli", "luthaf", "HaoZeke", "rubber-duck-debug")

    version("1.0.3", sha256="c3874bdb51d3e25f88622128336b61bd09023341b8c453a17c6bec29ab1ec964")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # pyproject.toml
    depends_on("py-wheel@0.36:", type="build")
    depends_on("py-setuptools@77:", type="build")
    depends_on("cmake@3.30:", type="build")

    # setup.py
    depends_on("py-torch@2.1:", type=("build", "run"))

    depends_on("py-sphericart")
