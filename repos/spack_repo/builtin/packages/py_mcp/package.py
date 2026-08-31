# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMcp(PythonPackage):
    """The official Python SDK for the Model Context Protocol (MCP)."""

    homepage = "https://github.com/modelcontextprotocol/python-sdk"
    pypi = "mcp/mcp-1.28.1.tar.gz"

    license("MIT", checked_by="aprozo")

    version("1.28.1", sha256="d51e36a5f5644faea4f85ea649bfffa6bc6c26770d42798ad6a3de3d2ba69683")

    variant("cli", default=False, description="Command-line tooling (mcp CLI)")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-anyio@4.5:", type=("build", "run"))
    depends_on("py-httpx@0.27.1:1", type=("build", "run"))
    depends_on("py-httpx-sse@0.4:", type=("build", "run"))
    depends_on("py-jsonschema@4.20:", type=("build", "run"))
    depends_on("py-pydantic@2.11:2", type=("build", "run"))
    depends_on("py-pydantic@2.12:2", when="^python@3.14:", type=("build", "run"))
    depends_on("py-pydantic-settings@2.5.2:", type=("build", "run"))
    depends_on("py-pyjwt@2.10.1:+crypto", type=("build", "run"))
    depends_on("py-python-multipart@0.0.9:", type=("build", "run"))
    depends_on("py-sse-starlette@1.6.1:", type=("build", "run"))
    depends_on("py-starlette@0.27:", type=("build", "run"))
    depends_on("py-starlette@0.48:", when="^python@3.14:", type=("build", "run"))
    depends_on("py-typing-extensions@4.9:", type=("build", "run"))
    depends_on("py-typing-inspection@0.4.1:", type=("build", "run"))
    depends_on("py-uvicorn@0.31.1:", type=("build", "run"))

    with when("+cli"):
        depends_on("py-python-dotenv@1:", type=("build", "run"))
        depends_on("py-typer@0.16:", type=("build", "run"))
