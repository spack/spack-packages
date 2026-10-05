# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Rsync(AutotoolsPackage):
    """Rsync is a fast and versatile file copying tool. It can copy locally, to/from another
    host over a remote shell, or to/from a remote rsync daemon. It offers a large number of
    options that control every aspect of its behavior and permit flexible specification of
    the set of files to be copied. It uses a delta-transfer algorithm to reduce the amount of
    data sent over the network by sending only the differences between the source files and
    the existing files in the destination. Rsync is widely used for backups and mirroring and
    as an improved copy command for everyday use."""

    homepage = "https://rsync.samba.org"
    url = "https://download.samba.org/pub/rsync/src/rsync-3.4.2.tar.gz"

    maintainers("drkrynstrng")

    license("GPL-3.0-or-later")

    executables = ["^rsync$"]

    version("3.5.1", sha256="c55f9c9dc10fb8bec397b399a0fdded53cc9a2d8e30891bb0d63724d25c37bef")
    version("3.5.0", sha256="c7ffd1ef653e99540f661e47cb00b7f9cad1ee6b972399b16f93d672656e0d33")
    version("3.4.4", sha256="bd88cf82fa653da32314fb229136407c5c90f80d1758d8f4b091767877d8fa96")
    version("3.4.3", sha256="c72e63ca3021cbc80ba86ec30102773f4c5631fbc492b52e773b3958f82a53d3")
    version("3.4.2", sha256="ff10aa2c151cd4b2dbbe6135126dbc854046113d2dfb49572a348233267eb315")
    version("3.4.1", sha256="2924bcb3a1ed8b551fc101f740b9f0fe0a202b115027647cf69850d65fd88c52")
    version("3.4.0", sha256="8e942f95a44226a012fe822faffa6c7fc38c34047add3a0c941e9bc8b8b93aa4")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("awk", type="build")
    depends_on("zlib-api")
    depends_on("popt")
    depends_on("openssl", when="@3.2:")
    depends_on("xxhash", when="@3.2:")
    depends_on("zstd", when="@3.2:")
    depends_on("lz4", when="@3.2:")
    depends_on("libidn2", when="@3.5.1:")

    conflicts("%nvhpc")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"rsync\s+version\s+(\S+)", output)
        return match.group(1) if match else None

    def configure_args(self):
        return ["--with-included-zlib=no"]
