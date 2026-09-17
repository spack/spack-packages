# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySphinxcontribProgramoutput(PythonPackage):
    """A Sphinx extension to literally insert the output of arbitrary commands
    into documents, helping you to keep your command examples up to date."""

    homepage = "https://sphinxcontrib-programoutput.readthedocs.org/"
    pypi = "sphinxcontrib_programoutput/sphinxcontrib_programoutput-0.20.tar.gz"
    git = "https://github.com/OpenNTI/sphinxcontrib-programoutput.git"

    license("BSD-2-Clause")

    version("0.20", sha256="5c4282c1c7fc9b5a23febe16ae038b6392d7ce068d186ad4870ba22e74db0711")
    version("0.19", sha256="787ca068b7e1205ed492ea20a23a8e599c3b4edb8c43bacf564e5ec7c30c7dad")
    version("0.18", sha256="09e68b6411d937a80b6085f4fdeaa42e0dc5555480385938465f410589d2eed8")
    version("0.15", sha256="80dd5b4eab780a13ff2c23500cac3dbf0e04ef9976b409ef25a47c263ef8ab94")
    version("0.10", sha256="fdee94fcebb0d8fddfccac5c4fa560f6177d5340c4349ee447c890bea8857094")

    with default_args(type="build"):
        depends_on("py-setuptools@61:", when="@0.20:")
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.20:")
        depends_on("python@3.8:", when="@0.18:")
        depends_on("python@2.7:2.8,3.5:")

        depends_on("py-docutils", when="@0.20:")

        depends_on("py-sphinx@5:", when="@0.18:")
        depends_on("py-sphinx@1.7.0:")

    def url_for_version(self, version):
        if version >= Version("0.18"):
            return f"https://pypi.io/packages/source/s/sphinxcontrib-programoutput/sphinxcontrib_programoutput-{version}.tar.gz"
        else:
            return f"https://pypi.io/packages/source/s/sphinxcontrib_programoutput/sphinxcontrib-programoutput-{version}.tar.gz"
