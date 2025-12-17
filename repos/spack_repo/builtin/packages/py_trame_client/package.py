# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrameClient(PythonPackage):
    """Internal client side implementation of trame"""

    homepage = "https://github.com/Kitware/trame-client"
    pypi = "trame-client/trame-client-2.17.1.tar.gz"

    maintainers("johnwparent")

    license("Apache-2.0", checked_by="johnwparent")

    version("3.11.2", sha256="98b3f09d0fbdb09cd29eac61c945a76dcad4a08cfb4843abce5a148fd6fc7316")
    version("2.17.1", sha256="0841e569d0792c7fc218a502663c814ad69e318d2885cec82a7fe1d07fdf0bf4")

    depends_on("python@3.9:", type=("build", "run"), when="@3.11.2")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-trame-common@0.2.0:", type=("build", "run"), when="@3.11.2")

    def url_for_version(self, version):
        url = (
            "https://files.pythonhosted.org/packages/source/t/trame-client/{name}-{version}.tar.gz"
        )
        if self.spec.satisfies("@3.5.1:"):
            name = "trame_client"
        else:
            name = "trame-client"
        return url.format(name=name, version=version)
