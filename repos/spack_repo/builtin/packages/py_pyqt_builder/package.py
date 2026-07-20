# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyqtBuilder(PythonPackage):
    """The PEP 517 compliant PyQt build system."""

    homepage = "https://www.riverbankcomputing.com/hg/PyQt-builder/"
    pypi = "PyQt-builder/pyqt_builder-1.18.2.tar.gz"

    license("GPL-2.0-or-later")

    version("1.19.1", sha256="6af6646ba29668751b039bfdced51642cb510e300796b58a4d68b7f956a024d8")
    version("1.19.0", sha256="79540e001c476bc050180db00fffcb1e9fa74544d95c148e48ad6117e49d6ea2")
    version("1.18.2", sha256="56dfea461484a87a8f0c8b0229190defc436d7ec5de71102e20b35e5639180bc")
    version("1.15.1", sha256="a2bd3cfbf952e959141dfe55b44b451aa945ca8916d1b773850bb2f9c0fa2985")
    version("1.12.2", sha256="f62bb688d70e0afd88c413a8d994bda824e6cebd12b612902d1945c5a67edcd7")

    depends_on("py-setuptools@77:", when="@1.18.2:", type="build")
    depends_on("py-setuptools@30.3:", type="build")
    depends_on("py-setuptools-scm@8:", when="@1.16:", type="build")
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-sip@6.7:6", when="@1.15:", type=("build", "run"))
    depends_on("py-sip@6.3:6", type=("build", "run"))

    def url_for_version(self, version):
        if version >= Version("1.16.1"):
            name = "pyqt_builder"
        else:
            name = "PyQt-builder"
        return f"https://files.pythonhosted.org/packages/source/P/PyQt-builder/{name}-{version}.tar.gz"
