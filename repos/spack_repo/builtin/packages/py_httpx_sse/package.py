# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHttpxSse(PythonPackage):
    """Consume Server-Sent Events (SSE) with HTTPX."""

    homepage = "https://github.com/florimondmanca/httpx-sse"
    pypi = "httpx-sse/httpx-sse-0.4.0.tar.gz"

    maintainers("aprozo")

    license("MIT", checked_by="aprozo")

    version("0.4.0", sha256="1e81a3a3070ce322add1d3529ed42eb5f70817f45ed6ec915ab753f961139721")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-httpx", type=("build", "run"))
