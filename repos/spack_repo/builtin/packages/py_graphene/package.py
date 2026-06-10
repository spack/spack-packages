# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGraphene(PythonPackage):
    """GraphQL Framework for Python."""

    homepage = "https://github.com/graphql-python/graphene"
    pypi = "graphene/graphene-3.3.tar.gz"

    maintainers("LydDeb", "climbfuji")

    license("MIT")

    version("3.4.3", sha256="2a3786948ce75fe7e078443d37f609cbe5bb36ad8d6b828740ad3b95ed1a0aaa")
    version("2.1.9", sha256="b9f2850e064eebfee9a3ef4a1f8aa0742848d97652173ab44c82cc8a62b9ed93", deprecated=True)

    depends_on("py-setuptools", type="build")
    depends_on("py-graphql-core@3.1:3.2", type=("build", "run"), when="@3")
    depends_on("py-graphql-core@2.1:2", type=("build", "run"), when="@2")
    depends_on("py-graphql-relay@3.1:3.2", type=("build", "run"), when="@3")
    depends_on("py-graphql-relay@2", type=("build", "run"), when="@2")
    depends_on("py-python-dateutil@2.7:2", type=("build", "run"), when="@3")
    depends_on("py-typing-extensions@4.7.1:4", type=("build", "run"), when="@3")
    depends_on("py-aniso8601@3:7", type=("build", "run"), when="@2")
    depends_on("py-six@1.10.0:1", type=("build", "run"), when="@2")
