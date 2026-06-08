# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAccessiblePygments(PythonPackage):
    """This package includes a collection of accessible themes for pygments based on
    different sources."""

    homepage = "https://github.com/Quansight-Labs/accessible-pygments"
    pypi = "accessible-pygments/accessible-pygments-0.0.4.tar.gz"

    license("BSD-3-Clause")

    version("0.0.5", sha256="40918d3e6a2b619ad424cb91e556bd3bd8865443d9f22f1dcdf79e33c8046872")
    version("0.0.4", sha256="e7b57a9b15958e9601c7e9eb07a440c813283545a20973f2574a5f453d0e953e")

    depends_on("python@3.9:", type=("build", "run"), when="@0.0.5:")
    depends_on("py-pygments@1.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build", when="@:0.0.4")
    depends_on("py-hatchling", type="build", when="@0.0.5:")
    depends_on("py-hatch-fancy-pypi-readme", type="build", when="@0.0.5:")
    depends_on("py-hatch-vcs", type="build", when="@0.0.5:")

    def url_for_version(self, version):
        url = (
            "https://pypi.org/packages/source/a/accessible-pygments/accessible{}pygments-{}.tar.gz"
        )
        if version < Version("0.0.5"):
            separator = "-"
        else:
            separator = "_"
        return url.format(separator, version)
