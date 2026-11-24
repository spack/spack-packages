# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAiowebdav2(PythonPackage):
    """Async Python 3 client for WebDAV."""

    homepage = "https://github.com/jpbede/aiowebdav2"
    pypi = "aiowebdav2/aiowebdav2-0.6.2.tar.gz"
    git = "https://github.com/jpbede/aiowebdav2.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("0.6.2", sha256="4ac816ec82d2b5ca012e188e066f8d430be663593e908743e1290a4b41964d93")

    depends_on("python@3.11:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatchling")

    with default_args(type=("build", "run")):
        depends_on("py-aiohttp@3.8:")
        depends_on("py-aiofiles@0.7:")
        depends_on("py-lxml@5.3:")
        depends_on("py-python-dateutil@2.9.0.post0:")
        depends_on("py-yarl@1.18.3:")
