# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMdocfile(PythonPackage):
    """mdocfile is Python package for working with SerialEM mdoc files."""

    homepage = "https://github.com/teamtomo/mdocfile/"
    pypi = "mdocfile/mdocfile-0.2.2.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.2.3", sha256="7cb9a4e14719fe76524a064209b0acc7ca9272781ae04ed03dceac7b23151c64")
    version("0.2.2", sha256="74d2dbe55ffda288f61cfac82aaf0052e1365a65c5acc1ed93e3c86e1457e5b0")
    version("0.0.8", sha256="61e352b569128fdeaff9f639e6aa3d46c8f8c3b8fe36627461ba0153f46f103d")

    depends_on("python@3.9:")
    depends_on("py-hatchling", type="build", when="@0.1.0:")
    depends_on("py-hatch-vcs", type="build", when="@0.1.0:")
    depends_on("py-setuptools", type="build", when="@:0.0.8")
    depends_on("py-setuptools-scm", type="build", when="@:0.0.8")

    depends_on("py-pydantic@2:", when="@0.1.0:")
    depends_on("py-pydantic")
    depends_on("py-pandas")
