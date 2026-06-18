# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLanggraphCheckpoint(PythonPackage):
    """Library with base interfaces for LangGraph checkpoint savers."""

    homepage = "https://docs.langchain.com/oss/python/langgraph/overview"
    pypi = "langgraph_checkpoint/langgraph_checkpoint-4.1.1.tar.gz"

    license("MIT")

    version("4.1.1", sha256="6c2bdb530c91f91d7d9c1bd100925d0fc4f498d418c17f3587d1526279482a25")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-langchain-core@0.2.38:", type=("build", "run"))
    depends_on("py-ormsgpack@1.12:", type=("build", "run"))
