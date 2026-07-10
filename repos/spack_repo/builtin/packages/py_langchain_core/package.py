# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLangchainCore(PythonPackage):
    """Building applications with LLMs through composability."""

    homepage = "https://docs.langchain.com/"
    pypi = "langchain_core/langchain_core-1.4.0.tar.gz"

    license("MIT")

    version("1.4.0", sha256="1dc341eed802ed9c117c0df3923c991e5e9e226571e5725c194eeb5bd93d1a7f")

    depends_on("py-hatchling", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-langsmith@0.3.45:0")
        depends_on("py-tenacity@8.1:9")
        depends_on("py-jsonpatch@1.33:1")
        depends_on("py-pyyaml@5.3:6")
        depends_on("py-typing-extensions@4.7:4")
        depends_on("py-packaging@23.2:")
        depends_on("py-pydantic@2.7.4:2")
        depends_on("py-uuid-utils@0.12:0")
        depends_on("py-langchain-protocol@0.0.14:")

    conflicts("^py-tenacity@8.4.0")
