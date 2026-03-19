# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHttpxSse(PythonPackage):
    """Consume Server-Sent Event (SSE) messages with HTTPX"""

    homepage = "https://github.com/florimondmanca/httpx-sse"
    pypi = "httpx_sse/httpx_sse-0.4.3.tar.gz"

    version("0.4.3", sha256="9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
