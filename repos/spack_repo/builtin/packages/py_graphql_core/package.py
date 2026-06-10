# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGraphqlCore(PythonPackage):
    """GraphQL-core 3 is a Python 3.6+ port of GraphQL.js, the
    JavaScript reference implementation for GraphQL, a query language
    for APIs created by Facebook."""

    homepage = "https://github.com/graphql-python/graphql-core"
    pypi = "graphql-core/graphql-core-3.1.5.tar.gz"

    maintainers("climbfuji")

    license("MIT")

    version(
        "3.2.7",
        sha256="27b6904bdd3b43f2a0556dad5d579bdfdeab1f38e8e8788e555bdcb586a6f62c",
        url="https://files.pythonhosted.org/packages/source/g/graphql-core/graphql_core-3.2.7.tar.gz",
    )
    version("3.1.2", sha256="c056424cbdaa0ff67446e4379772f43746bad50a44ec23d643b9bdcd052f5b3a")
    version("3.0.5", sha256="51f7dab06b5035515b23984f6fcb677ed909b56c672152699cca32e03624992e")
    version("2.3.2", sha256="aac46a9ac524c9855910c14c48fc5d60474def7f99fd10245e76608eba7af746")

    depends_on("python@3.6:3", type=("build", "run"))
    depends_on("py-poetry-core@1:2", when="@3.2:", type="build")
    depends_on("py-poetry-core@1", when="@3:3.1", type="build")
    depends_on("py-setuptools@59:80", when="@3", type="build")
    depends_on("py-setuptools", when="@2", type="build")
    depends_on("py-six@1.10.0:", type=("build", "run"), when="@2.3.2")
    depends_on("py-promise@2.3:2", type=("build", "run"), when="@2.3.2")
    depends_on("py-rx@1.6:1", type=("build", "run"), when="@2.3.2")
