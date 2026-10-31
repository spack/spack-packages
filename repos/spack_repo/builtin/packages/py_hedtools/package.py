# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHedtools(PythonPackage):
    """HED validation, summary, and analysis tools for annotating events and
    experimental metadata."""

    homepage = "https://www.hedtags.org/"
    pypi = "hedtools/hedtools-1.2.0.tar.gz"
    git = "https://github.com/hed-standard/hed-python.git"

    license("MIT")

    version("1.2.0", sha256="ee61e259f30f0c33e37c4aa946a97f5fb6fac392653cde021cfc333c5faf48d1")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        depends_on("py-click@8:")
        depends_on("py-click-option-group@0.5.0:")
        depends_on("py-defusedxml@0.7.1:")
        depends_on("py-inflect@7.5.0:")
        depends_on("py-numpy@2.0.2:")
        depends_on("py-openpyxl@3.1.5:")
        depends_on("py-pandas@2.2.3:3")
        depends_on("py-portalocker@3.1.1:")
        depends_on("py-semantic-version@2.10.0:")
        depends_on("py-typeguard@4.5.2:")
