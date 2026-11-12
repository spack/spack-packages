# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLangchainProtocol(PythonPackage):
    """Python bindings for the LangChain agent streaming protocol."""

    homepage = "https://github.com/langchain-ai/agent-protocol/tree/main/streaming"
    pypi = "langchain_protocol/langchain_protocol-0.0.16.tar.gz"

    license("MIT")

    version("0.0.16", sha256="806c7cdd951b1c4f692fa40fce60821ff0f221d4360e27673ddf2c2b99c2b7ff")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-typing-extensions@4.13:4", type=("build", "run"))
