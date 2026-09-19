# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySseStarlette(PythonPackage):
    """SSE plugin for Starlette / FastAPI, serving Server-Sent Events."""

    homepage = "https://github.com/sysid/sse-starlette"
    pypi = "sse-starlette/sse_starlette-3.4.8.tar.gz"

    license("BSD-3-Clause", checked_by="aprozo")

    version("3.4.8", sha256="ed89ffbb75cbf78a5fe2f2109cd584792ee7f9dfac96f791db546df8f15f3f9c")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-anyio@4.7:", type=("build", "run"))
    depends_on("py-starlette@0.49.1:", type=("build", "run"))
