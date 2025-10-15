# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyMagicgui(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://pyapp-kit.github.io/magicgui/"
    pypi = "magicgui/magicgui-0.10.1.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("0.10.1", sha256="422cd0c0b5fea2fb37f3d3ea9b5591a160919baeae16061efea6f74c9b8fcfd1")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-docstring-parser@0.7:", type=("build", "run"))
    depends_on("py-psygnal@0.8.0:", type=("build", "run"))
    depends_on("py-qtpy@2.4.0:", type=("build", "run"))
    depends_on("py-superqt@0.7.2: +iconify", type=("build", "run"))
    depends_on("py-typing-extensions@4.6:", type=("build", "run"))
