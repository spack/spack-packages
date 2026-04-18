# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Rsync(AutotoolsPackage):
    """An open source utility that provides fast incremental file transfer."""

    homepage = "https://rsync.samba.org"
    url = "https://download.samba.org/pub/rsync/src/rsync-3.3.0.tar.gz"

    license("GPL-3.0-or-later")

    version("3.4.1", sha256="2924bcb3a1ed8b551fc101f740b9f0fe0a202b115027647cf69850d65fd88c52")
    version("3.4.0", sha256="8e942f95a44226a012fe822faffa6c7fc38c34047add3a0c941e9bc8b8b93aa4")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("zlib-api")
    depends_on("popt")
    depends_on("openssl", when="@3.2:")
    depends_on("xxhash", when="@3.2:")
    depends_on("zstd", when="@3.2:")
    depends_on("lz4", when="@3.2:")

    conflicts("%nvhpc")

    executables = ["^rsync$"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"rsync\s+version\s+(\S+)", output)
        return match.group(1) if match else None

    def configure_args(self):
        return ["--with-included-zlib=no"]
