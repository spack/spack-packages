# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrameClient(PythonPackage):
    """Internal client side implementation of trame"""

    homepage = "https://github.com/Kitware/trame-client"
    pypi = "trame-client/trame_client-3.11.2.tar.gz"

    maintainers("johnwparent")

    license("Apache-2.0", checked_by="johnwparent")

    version("3.11.3", sha256="ea75073c04c871a96ad51634ff7fc0b36242f62aab7ddfaac55e961c9ea46f90")
    version("3.11.2", sha256="98b3f09d0fbdb09cd29eac61c945a76dcad4a08cfb4843abce5a148fd6fc7316")
    version("2.17.1", sha256="0841e569d0792c7fc218a502663c814ad69e318d2885cec82a7fe1d07fdf0bf4")

    depends_on("python@3.9:", type=("build", "run"), when="@3.11.2:")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-trame-common@0.2:", type=("build", "run"), when="@3.11.2")

    def url_for_version(self, version):
        sep = "_" if version >= Version("3.5.1") else "-"
        return f"https://files.pythonhosted.org/packages/source/t/trame{sep}client/trame{sep}client-{version}.tar.gz"
