# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYtDlp(PythonPackage):
    """A feature-rich command-line audio/video downloader."""

    homepage = "https://github.com/yt-dlp/yt-dlp"
    pypi = "yt_dlp/yt_dlp-2025.11.12.tar.gz"

    license("Unlicense")

    version(
        "2025.11.12", sha256="5f0795a6b8fc57a5c23332d67d6c6acf819a0b46b91a6324bae29414fa97f052"
    )

    variant("default", default=True, description="Install networking dependencies")

    depends_on("py-hatchling@1.27:")

    with default_args(type=("build", "run")):
        with when("+default"):
            depends_on("py-brotli")
            depends_on("py-certifi")
            depends_on("py-mutagen")
            depends_on("py-pycryptodomex")
            depends_on("py-requests@2.32.2:2")
            depends_on("py-urllib3@2.0.2:2")
            depends_on("py-websockets@13:")
            depends_on("py-yt-dlp-ejs@0.3.1")
