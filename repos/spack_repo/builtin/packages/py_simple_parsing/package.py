# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySimpleParsing(PythonPackage):
    """A small utility to simplify and clean up argument parsing scripts."""

    homepage = "https://github.com/lebrice/SimpleParsing"
    pypi = "simple_parsing/simple_parsing-0.1.9.tar.gz"

    license("MIT")

    version("0.1.9", sha256="0ff184ebaa6606420989ddbcb5650b21c62e2a59ec5388bc76c3343bda872cde")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-uv-dynamic-versioning")

    with default_args(type=("build", "run")):
        # imports dataclasses._MISSING_TYPE, which python 3.15 removed
        depends_on("python@3.9:3.14")
        depends_on("py-docstring-parser@0.15:0")
        depends_on("py-typing-extensions@4.5.0:")
