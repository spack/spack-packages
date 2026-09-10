# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyfive(PythonPackage):
    """A pure python HDF5 reader"""

    homepage = "https://github.com/NCAS-CMS/pyfive"
    git = "https://github.com/NCAS-CMS/pyfive.git"
    pypi = "pyfive/pyfive-1.1.1.tar.gz"

    maintainers("LydDeb")

    license("BSD-3-Clause", checked_by="LydDeb")

    version("1.1.1", sha256="a43e852947b9bc4703bc174d4e9cec77d61c2324d35961bbae9914aa69821ce5")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@80:")
        depends_on("py-setuptools-scm@8:")
    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:")
        # Not in pyproject.toml but necessary to import the 'pyfive' module.
        # This dependence appears in high_level.py on line 13
        depends_on("py-typing-extensions")
