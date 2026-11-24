# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJaracoFunctools(PythonPackage):
    """Functools like those found in stdlib"""

    homepage = "https://github.com/jaraco/jaraco.functools"
    pypi = "jaraco.functools/jaraco.functools-2.0.tar.gz"

    license("MIT")

    version(
        "4.6.0",
        url="https://files.pythonhosted.org/packages/source/j/jaraco.functools/jaraco_functools-4.6.0.tar.gz",
        sha256="880c577ec9720b3a052d5bc611fb9f2269b3d87902ef42440df443b88e443280",
    )
    version("2.0", sha256="35ba944f52b1a7beee8843a5aa6752d1d5b79893eeb7770ea98be6b637bf9345")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@77:", type="build", when="@4.6:")
    depends_on("py-setuptools-scm@1.15.0:", type="build")
    depends_on("py-setuptools-scm@3.4.1:", type="build", when="@4.6:")
    depends_on("py-coherent-licensed", type="build", when="@4.6:")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@4.6:")
    depends_on("py-more-itertools", type=("build", "run"))
