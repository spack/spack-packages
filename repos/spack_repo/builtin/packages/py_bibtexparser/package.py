# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBibtexparser(PythonPackage):
    """Python 3 library to parse bibtex files."""

    homepage = "https://github.com/sciunto-org/python-bibtexparser"
    pypi = "bibtexparser/bibtexparser-1.4.1.tar.gz"

    version("1.4.1", sha256="e00e29e24676c4808e0b4333b37bb55cca9cbb7871a56f63058509281588d789")

    depends_on("py-setuptools", type="build")
    depends_on("py-pyparsing@2.0.3:", type=("build", "run"))
