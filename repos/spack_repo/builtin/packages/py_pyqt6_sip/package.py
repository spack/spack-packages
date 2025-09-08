# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyqt6Sip(PythonPackage):
    """The sip module support for PyQt6."""

    homepage = "https://www.riverbankcomputing.com/software/sip/"
    pypi = "PyQt6-sip/pyqt6_sip-13.10.2.tar.gz"

    license("GPL-2.0-or-later")

    version("13.10.2", sha256="464ad156bf526500ce6bd05cac7a82280af6309974d816739b4a9a627156fafe")
    version("13.6.0", sha256="2486e1588071943d4f6657ba09096dc9fffd2322ad2c30041e78ea3f037b5778")
    version("13.5.1", sha256="d1e9141752966669576d04b37ba0b122abbc41cc9c35493751028d7d91c4dd49")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools@75.8.1:", type="build", when="@13.10.2:")
    depends_on("py-setuptools@30.3:", type="build")

    def url_for_version(self, version):
        if version >= Version("13.9.1"):
            name = "pyqt6_sip"
        else:
            name = "PyQt6_sip"
        return (
            f"https://files.pythonhosted.org/packages/source/P/PyQt6-sip/{name}-{version}.tar.gz"
        )
