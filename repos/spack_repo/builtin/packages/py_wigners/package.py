# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWigners(PythonPackage):
    """Computes Wigner 3j coefficients and Clebsch-Gordan coefficients"""

    homepage = "https://github.com/Luthaf/wigners"
    pypi = "wigners/wigners-0.3.1.tar.gz"

    maintainers("luthaf", "RMeli", "HaoZeke")

    license("Apache-2.0 OR MIT", checked_by="RMeli")

    version("0.3.1", sha256="90882e69208a830140a244645e39d4c3a84b8db1a4feb926ba29d0cc374ac149")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging", type="build")

    depends_on("py-numpy", type=("build", "run"))

    # setup.py
    depends_on("rust")
