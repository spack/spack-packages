# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJaracoContext(PythonPackage):
    """Useful decorators and context managers."""

    homepage = "https://github.com/jaraco/jaraco.context"
    pypi = "jaraco_context/jaraco_context-6.0.1.tar.gz"

    license("MIT")

    version("6.1.2", sha256="f1a6c9d391e661cc5b8d39861ff077a7dc24dc23833ccee564b234b81c82dfe3")
    version("6.0.1", sha256="9bae4ea555cf0b14938dc0aee7c9f32ed303aa20a3b73e7dc80111628792d1b3")

    with default_args(type="build"):
        depends_on("py-setuptools@77:", when="@6.0.2:")
        depends_on("py-setuptools@61.2:")
        depends_on("py-setuptools-scm+toml@3.4.1:")
        depends_on("py-coherent-licensed", when="@6.0.2:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@6.1.2:")
        depends_on("python@3.8:")

        depends_on("py-backports-tarfile", when="^python@:3.11")
