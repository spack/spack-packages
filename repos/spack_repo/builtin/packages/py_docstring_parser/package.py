# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDocstringParser(PythonPackage):
    """Parse Python docstrings in reST, Google and Numpydoc format."""

    homepage = "https://github.com/rr-/docstring_parser"
    pypi = "docstring-parser/docstring_parser-0.15.tar.gz"

    license("MIT")

    version("0.17.0", sha256="583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912")
    version("0.15", sha256="48ddc093e8b1865899956fcc03b03e66bb7240c310fac5af81814580c55bf682")

    depends_on("py-hatchling", when="@0.17:", type="build")

    # Historical dependencies
    # https://github.com/rr-/docstring_parser/pull/91
    depends_on("python@:3.13", when="@:0.16", type=("build", "run"))
    depends_on("py-poetry-core@1:", when="@:0.16", type="build")
