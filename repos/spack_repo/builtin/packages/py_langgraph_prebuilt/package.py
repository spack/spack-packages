# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLanggraphPrebuilt(PythonPackage):
    """Library with high-level APIs for creating and executing LangGraph agents and tools."""

    homepage = "https://docs.langchain.com/oss/python/langgraph/overview"
    pypi = "langgraph_prebuilt/langgraph_prebuilt-1.1.0.tar.gz"

    license("MIT")

    version("1.1.0", sha256="3c579cf6eed2d17f9c157c2d0fcaddcd8688524e7022d3b22b37a3bf4589d528")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-langgraph-checkpoint@2.1.0:4", type=("build", "run"))
    depends_on("py-langchain-core@1.3.1:", type=("build", "run"))
