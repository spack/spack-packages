# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonCalamine(PythonPackage):
    """Python binding for Rust's library for reading excel and odf file - calamine."""

    homepage = "https://github.com/dimastbk/python-calamine"
    pypi = "python_calamine/python_calamine-0.1.7.tar.gz"

    license("MIT")

    version("0.6.1", sha256="5974989919aa0bb55a136c1822d6f8b967d13c0fd0f245e3293abb4e63ab0f4b")
    version("0.1.7", sha256="57199dc84522001bdefd0e87e6c50c5a88bf3425dbc3d8fb52c0dec77c218ba2")

    depends_on("py-maturin@1", type="build")
    depends_on("rust", type="build")
