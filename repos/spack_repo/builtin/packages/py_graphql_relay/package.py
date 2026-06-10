# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGraphqlRelay(PythonPackage):
    """Relay library for graphql-core."""

    homepage = "https://github.com/graphql-python/graphql-relay-py"
    pypi = "graphql-relay/graphql-relay-2.0.1.tar.gz"

    maintainers("LydDeb", "climbfuji")

    license("MIT")

    version("3.2.0", sha256="1ff1c51298356e481a0be009ccdff249832ce53f30559c1338f22a0e0d17250c")
    version("2.0.1", sha256="870b6b5304123a38a0b215a79eace021acce5a466bf40cd39fa18cb8528afabb")

    depends_on("python@3.6:3", type=("build", "run"))
    depends_on("py-poetry-core@1", when="@3", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-graphql-core@2.2:2", type=("build", "run"), when="@2")
    depends_on("py-graphql-core@3.2", type=("build", "run"), when="@3")
    depends_on("py-typing-extensions@4.1:4", type=("build", "run"), when="@3 ^python@:3.7")
    depends_on("py-six@1.12:", type=("build", "run"), when="@2")
    depends_on("py-promise@2.2:2", type=("build", "run"), when="@2")
