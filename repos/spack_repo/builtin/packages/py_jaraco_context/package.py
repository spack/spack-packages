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

    version("6.0.1", sha256="9bae4ea555cf0b14938dc0aee7c9f32ed303aa20a3b73e7dc80111628792d1b3")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")
    depends_on("py-setuptools-scm+toml@3.4.1:", type="build")

    depends_on("py-backports-tarfile", type=("build", "run"), when="^python@:3.11")
