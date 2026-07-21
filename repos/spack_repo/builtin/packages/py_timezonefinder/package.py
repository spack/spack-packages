# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTimezonefinder(PythonPackage):
    """python package for finding the timezone of any point on earth (coordinates) offline"""

    homepage = "https://timezonefinder.michelfe.it/gui"
    git = "https://github.com/jannikmi/timezonefinder.git"
    pypi = "timezonefinder/timezonefinder-8.2.4.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("8.2.4", sha256="d80fae37adf1497729cc3e69826c22f3b2fec16db07932bf389b6ae545400b42")

    depends_on("c", type="build")

    depends_on("python@3.11:3", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:")
        depends_on("py-h3@4:")
        depends_on("py-cffi@1.15.1:2")
        depends_on("py-flatbuffers@25.2.10:")

    # py-setuptools@61: supports PEP 621 which recommends the following syntax
    # license = { text = "Apache-2.0" }
    @when("^py-setuptools@61:")
    def patch(self):
        pyproject = "pyproject.toml"
        filter_file(r'^license\s*=\s*"([^"]+)"', r'license = { text = "\1" }', pyproject)
