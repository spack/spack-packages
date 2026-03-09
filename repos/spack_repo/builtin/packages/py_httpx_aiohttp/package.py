# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHttpxAiohttp(PythonPackage):
    """httpx-aiohttp - provides transports for httpx to work on top of aiohttp, handling all high-level features like authentication, retries, and cookies through httpx, while delegating low-level socket-level HTTP messaging to aiohttp"""

    homepage = "https://karpetrosyan.github.io/httpx-aiohttp/"
    pypi = "httpx_aiohttp/httpx_aiohttp-0.1.12.tar.gz"

    license("BSD-3-Clause")

    version("0.1.12", sha256="c3ab0d0d53a3ea806f69431ddf541921117a36a087c8af56056de3c097cffa38")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-aiohttp@3.10.0:3", type=("build", "run"))
    depends_on("py-httpx@0.27.0:", type=("build", "run"))
