# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLogicalUnification(PythonPackage):
    """Logical unification in Python."""

    homepage = "https://github.com/pythological/unification"
    pypi = "logical-unification/logical_unification-0.4.7.tar.gz"

    license("BSD-3-Clause")

    version("0.4.7", sha256="3d73b263a870827b3f52d89c94f3336afd7fcaecf1e0c67fa18e73025399775c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@80:", type="build")
    depends_on("py-setuptools-scm", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-multipledispatch")
        depends_on("py-toolz")
