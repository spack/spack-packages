# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

BLAKE2b256 = {
    "3.11.2": "aea5febe01d66c7524882c5f4f3e75affbf112896b660a8a53ddc505eeaa57f7",
    "2.17.1": "a2c7a968cc21feeac7ec8603304a217bad04fe40101bb3786f99454d5e808706",
}


class PyTrameClient(PythonPackage):
    """Internal client side implementation of trame"""

    homepage = "https://github.com/Kitware/trame-client"
    pypi = "trame-client/trame_client-3.11.2.tar.gz"

    maintainers("johnwparent")

    license("Apache-2.0", checked_by="johnwparent")

    version("3.11.2", sha256="98b3f09d0fbdb09cd29eac61c945a76dcad4a08cfb4843abce5a148fd6fc7316")
    version("2.17.1", sha256="0841e569d0792c7fc218a502663c814ad69e318d2885cec82a7fe1d07fdf0bf4")

    depends_on("python@3.9:", type=("build", "run"), when="@3.11.2")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-trame-common@0.2.0:", type=("build", "run"), when="@3.11.2")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/{first}/{second}/{last}/{name}-{version}.tar.gz"
        first = BLAKE2b256[version.string][:2]
        second = BLAKE2b256[version.string][2:4]
        last = BLAKE2b256[version.string][4:]
        if version >= Version("3.5.1"):
            name = "trame_client"
        else:
            name = "trame-client"
        return url.format(name=name, version=version, first=first, second=second, last=last)
