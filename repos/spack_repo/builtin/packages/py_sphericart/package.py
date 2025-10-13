# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphericart(PythonPackage):
    """Library for the efficient calculation of spherical harmonics
    and their derivatives in Cartesian coordinates."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://sphericart.readthedocs.io/en/latest/index.html"
    pypi = "sphericart/sphericart-1.0.3.tar.gz"

    maintainers("RMeli", "luthaf")

    version("1.0.3", sha256="007b21f075d5ba331519fe5cec6acf28d5bd458a970a158973d51047795afd12")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("py-wheel@0.36:", type="build")
    depends_on("py-setuptools@44:", type="build")

    depends_on("py-numpy", type=("build", "run"))
