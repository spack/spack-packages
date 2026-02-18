# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Munge(AutotoolsPackage):
    """MUNGE Uid 'N' Gid Emporium"""

    homepage = "https://dun.github.io/munge/"
    url = "https://github.com/dun/munge/releases/download/munge-0.5.14/munge-0.5.14.tar.xz"
    maintainers("ChristianTackeGSI")

    license("LGPL-3.0-only")

    version("0.5.18", sha256="39c3ec6ef5604bfa206e8aa10fc05d5119040f6de4a554bc0fb98ca1aed838dc")
    version("0.5.15", sha256="3f979df117a34c74db8fe2835521044bdeb08e3b7d0f168ca97c3547f51da9ba")
    version("0.5.14", sha256="6606a218f18090fa1f702e3f6fb608073eb6aafed534cf7dd81b67b2e0d30640")
    version("0.5.13", sha256="99753dfd06a4f063c36f3fb0eb1964f394feb649937d94c4734d85b7964144da")
    version("0.5.12", sha256="e972e3c3e947995a99e023f5758047db16cfe2f0c2c9ca76399dc1511fa71be8")
    version(
        "0.5.11",
        sha256="8e075614f81cb0a6df21a0aafdc825498611a04429d0876f074fc828739351a5",
        url="https://github.com/dun/munge/releases/download/munge-0.5.11/munge-0.5.11.tar.bz2",
    )

    variant(
        "localstatedir",
        default="PREFIX/var",
        values=any,
        description="Set local state path (possibly to /var)",
    )

    depends_on("c", type="build")

    depends_on("openssl")
    depends_on("libgcrypt")
    depends_on("bzip2")

    # Below two patches fix CVE-2026-25506 in older versions of Munge
    # Fix out-of-bounds read in credential decoding
    patch(
        "https://github.com/dun/munge/commit/5bd6d4db92dabdbed3aaf01ebd5f0d98944326bb.patch?full_index=1",
        sha256="3145b60b1bf94fcca9b361d59140ea12b1a8b3e09d88181d7d73335580ca7a6f",
        when="@:0.5.17",
    )
    # Fix buffer overflow allowing key leakage and credential forgery
    patch(
        "https://github.com/dun/munge/commit/bf40cc27c4ce8451d4b062c9de0b67ec40894812.patch?full_index=1",
        sha256="05b4d63ea71d27db27eb7201fb907abf50dd2384b729be0f0a78c381ac4f6ccc",
        when="@:0.5.17",
    )

    def configure_args(self):
        args = []
        localstatedir = self.spec.variants["localstatedir"].value
        if localstatedir != "PREFIX/var":
            args.append("--localstatedir={0}".format(localstatedir))
        return args

    def install(self, spec, prefix):
        os.makedirs(os.path.join(prefix, "lib/systemd/system"))
        super().install(spec, prefix)
