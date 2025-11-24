# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonDocx(PythonPackage):
    """python-docx is a Python library for reading, creating, and
    updating Microsoft Word 2007+ (.docx) files."""

    homepage = "https://github.com/python-openxml/python-docx"
    pypi = "python_docx/python_docx-1.2.0.tar.gz"

    version("1.2.0", sha256="7bc9d7b7d8a69c9c02ca09216118c86552704edc23bac179283f2e38f86220ce")

    license("MIT")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61.0.0:", type="build")

    depends_on("py-lxml@3.1.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.9.0:", type=("build", "run"))
