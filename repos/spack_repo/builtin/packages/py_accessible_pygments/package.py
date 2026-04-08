# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAccessiblePygments(PythonPackage):
    """This package includes a collection of accessible themes for pygments based on
    different sources."""

    homepage = "https://github.com/Quansight-Labs/accessible-pygments"
    pypi = "accessible-pygments/accessible_pygments-0.0.5.tar.gz"

    license("BSD-3-Clause")

    version("0.0.5", sha256="40918d3e6a2b619ad424cb91e556bd3bd8865443d9f22f1dcdf79e33c8046872")
    version("0.0.4", sha256="e7b57a9b15958e9601c7e9eb07a440c813283545a20973f2574a5f453d0e953e")

    depends_on("py-pygments@1.5:", type=("build", "run"))

    # New build dependencies
    with default_args(type=("build"), when="@0.0.5:"):
        depends_on("py-hatchling")
        depends_on("py-hatch-fancy-pypi-readme")
    # Old build dependencies
    depends_on("py-setuptools", type=("build"), when="@:0.0.4")

    def url_for_version(self, version):
        base = "https://files.pythonhosted.org/packages/source"
        name = self.pypi.partition("/")[0]
        if version >= Version("0.0.5"):
            modname = name.replace("-", "_")
        else:
            modname = name
        return f"{base}/{name[0]}/{name}/{modname}-{version}.tar.gz"
