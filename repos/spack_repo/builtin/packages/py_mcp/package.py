# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMcp(PythonPackage):
    """The official Python SDK for Model Context Protocol servers and clients."""

    homepage = "https://github.com/modelcontextprotocol/python-sdk"
    pypi = "mcp/mcp-1.26.0.tar.gz"

    license("MIT", checked_by="thomas-bouvier")

    version("1.26.0", sha256="db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-anyio@4.9:", type=("build", "run"))
    depends_on("py-httpx@0.27.1:", type=("build", "run"))
    depends_on("py-httpx-sse@0.4:", type=("build", "run"))  # to be added
    depends_on("py-pydantic@2.12.0:", type=("build", "run"))
    depends_on("py-starlette@0.48:", when="^python@3.14:", type=("build", "run"))  # to be updated
    depends_on("py-starlette@0.27:", when="^python@:3.13", type=("build", "run"))
    depends_on("py-python-multipart@0.0.9:", type=("build", "run"))
    depends_on("py-sse-starlette@3:", type=("build", "run"))  # to be added
    depends_on("py-pydantic-settings@2.5.2:", type=("build", "run"))
    depends_on("py-uvicorn@0.31.1:", type=("build", "run"))
    depends_on("py-jsonschema@4.20:", type=("build", "run"))
    depends_on("py-pyjwt@2.10.1: +crypto", type=("build", "run"))  # to be updated
    depends_on("py-typing-extensions@4.13.0:", type=("build", "run"))
    depends_on("py-typing-inspection@0.4.1:", type=("build", "run"))
