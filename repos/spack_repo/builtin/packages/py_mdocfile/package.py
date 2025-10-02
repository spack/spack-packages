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

    version("0.2.2", sha256="74d2dbe55ffda288f61cfac82aaf0052e1365a65c5acc1ed93e3c86e1457e5b0")

    depends_on("python@3.9:")
    depends_on("py-hatchling", type="build")

    depends_on("py-pydantic@2:")
    depends_on("py-pandas")

