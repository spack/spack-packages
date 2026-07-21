# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyvers(PythonPackage):
    """A Python library for managing multiple versions of dependencies"""

    homepage = "https://github.com/vmoens/pyvers"
    pypi = "pyvers/pyvers-0.2.2.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.2.2", sha256="205026bcd0b4c09198cb3a32f243fd179ef012882ce16d93dcb755320acd56f7")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-poetry-core@2")
