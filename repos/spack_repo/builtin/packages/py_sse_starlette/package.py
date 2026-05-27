# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySseStarlette(PythonPackage):
    """Production ready Server-Sent Events implementation for Starlette
    and FastAPI following the W3C SSE specification."""

    homepage = "https://github.com/sysid/sse-starlette"
    pypi = "sse_starlette/sse_starlette-3.3.3.tar.gz"

    version("3.3.3", sha256="72a95d7575fd5129bd0ae15275ac6432bb35ac542fdebb82889c24bb9f3f4049")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-starlette@0.49.1:", type=("build", "run"))
    depends_on("py-anyio@4.7:", type=("build", "run"))
