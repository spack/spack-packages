# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIhm(PythonPackage):
    """Package for handling IHM mmCIF and BinaryCIF files."""

    homepage = "https://github.com/ihmwg/python-ihm"
    git = "https://github.com/ihmwg/python-ihm.git"
    pypi = "ihm/ihm-2.7.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("2.9", sha256="2efc460217c66b4d359c1eb7509ffa417568c2e59e04c0e2609995db99fc937f")
    version("2.7", sha256="a3b9eba5545de1e07a15d110e9e6b70369807798d8f2c45908323db2b6fde82c")

    depends_on("c", type="build")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-msgpack", type=("build", "run"))
