# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHttpxAiohttp(PythonPackage):
    """httpx-aiohttp - provides transports for httpx to work on top of aiohttp, handling all
    high-level features like authentication, retries, and cookies through httpx, while delegating
    low-level socket-level HTTP messaging to aiohttp"""

    homepage = "https://karpetrosyan.github.io/httpx-aiohttp/"
    pypi = "httpx_aiohttp/httpx_aiohttp-0.1.12.tar.gz"

    license("BSD-3-Clause")

    version("0.1.12", sha256="81feec51fd82c0ecfa0e9aaf1b1a6c2591260d5e2bcbeb7eb0277a78e610df2c")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-aiohttp@3.10.0:3", type=("build", "run"))
    depends_on("py-httpx@0.27.0:", type=("build", "run"))
