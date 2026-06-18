# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLanggraph(PythonPackage):
    """Building stateful, multi-actor applications with LLMs."""

    homepage = "https://docs.langchain.com/oss/python/langgraph/overview"
    pypi = "langgraph/langgraph-1.2.2.tar.gz"

    license("MIT")

    version("1.2.2", sha256="f54a98458976b3ff0774683867df125fb52d8dbedeb2441d0b0656a51331cee5")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-langchain-core@1.4:1", type=("build", "run"))
    depends_on("py-langgraph-checkpoint@4.1:4", type=("build", "run"))
    depends_on("py-langgraph-sdk@0.3", type=("build", "run"))
    depends_on("py-langgraph-prebuilt@1.1", type=("build", "run"))
    depends_on("py-xxhash@3.5:", type=("build", "run"))
    depends_on("py-pydantic@2.7.4:", type=("build", "run"))
