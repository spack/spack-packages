# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLanggraphSdk(PythonPackage):
    """SDK for interacting with LangGraph API."""

    homepage = "https://docs.langchain.com/oss/python/langgraph/overview"
    pypi = "langgraph_sdk/langgraph_sdk-0.4.0.tar.gz"

    license("MIT")

    version("0.4.0", sha256="fd84612d215d6dca11cdfc8c0835df2910c7e51a0b0150b950fc7a928c76a2eb")
    version("0.3.15", sha256="29e805003d2c6e296823dd71992610976fd0428cefaa8b3304fd91f2247037de")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-httpx@0.25.2:", type=("build", "run"))
    depends_on("py-orjson@3.11.5:", type=("build", "run"))
    depends_on("py-langchain-protocol@0.0.15:", type=("build", "run"), when="@0.4:")
    depends_on("py-langchain-core@1.4:1", type=("build", "run"), when="@0.4:")
    depends_on("py-websockets@14:15", type=("build", "run"), when="@0.4:")
