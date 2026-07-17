# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySseStarlette(PythonPackage):
    """SSE plugin for Starlette / FastAPI, serving Server-Sent Events."""

    homepage = "https://github.com/sysid/sse-starlette"
    pypi = "sse-starlette/sse_starlette-2.1.3.tar.gz"

    maintainers("aprozo")

    license("BSD-3-Clause", checked_by="aprozo")

    version("2.1.3", sha256="9cd27eb35319e1414e3d2558ee7414487f9529ce3b3cf9b21434fd110e017169")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    depends_on("py-anyio", type=("build", "run"))
    depends_on("py-starlette", type=("build", "run"))
    depends_on("py-uvicorn", type=("build", "run"))
