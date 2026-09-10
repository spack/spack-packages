# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestDoctestplus(PythonPackage):
    """Pytest plugin with advanced doctest features."""

    homepage = "https://github.com/astropy/pytest-doctestplus"
    pypi = "pytest-doctestplus/pytest-doctestplus-0.8.0.tar.gz"

    license("BSD-3-Clause")

    version("1.4.0", sha256="df83832b1d11288572df2ee4c7cccdb421d812b8038a658bb514c9c62bdbd626")
    version("1.3.0", sha256="709ad23ea98da9a835ace0a4365c85371c376e000f2860f30de6df3a6f00728a")
    version("0.13.0", sha256="f884e2231fe5378cc8e5d1a272d19b01ebd352df0591a5add55ff50adac2d2d0")
    version("0.9.0", sha256="6fe747418461d7b202824a3486ba8f4fa17a9bd0b1eddc743ba1d6d87f03391a")

    depends_on("py-setuptools-scm", type="build")
    depends_on("py-setuptools@30.3.0:", type=("build", "run"))
    depends_on("python@3.9:", when="@1.4.0:", type=("build", "run"))
    depends_on("python@3.8:", when="@1.1.0:", type=("build", "run"))
    depends_on("python@3.7:", when="@0.10.0:", type=("build", "run"))
    depends_on("python@3.6:", when="@0.9.0:", type=("build", "run"))

    depends_on("py-pytest@4.6:", type=("build", "run"))
    depends_on("py-packaging@17:", when="@0.10:", type=("build", "run"))

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/p/{0}/{0}-{1}.tar.gz"
        if version >= Version("1.3.0"):
            name = "pytest_doctestplus"
        else:
            name = "pytest-doctestplus"
        return url.format(name, version)
