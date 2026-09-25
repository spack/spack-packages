# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMinikanren(PythonPackage):
    """Relational programming in Python."""

    homepage = "https://github.com/pythological/kanren"
    pypi = "minikanren/minikanren-1.0.5.tar.gz"

    license("BSD-3-Clause")

    version("1.0.5", sha256="c030e3e9a3fa5f372f84b66966776a8dc63b16b98768b78be0401982b892e00d")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm+toml", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-cons@0.4:")
        depends_on("py-etuples@0.3.1:")
        depends_on("py-logical-unification@0.4.1:")
        depends_on("py-multipledispatch")
        depends_on("py-toolz")
        depends_on("py-typing-extensions")
