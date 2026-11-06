# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Bun(Package):
    """Bun is an all-in-one JavaScript runtime, bundler, transpiler and package manager."""

    homepage = "https://bun.com/"
    url = "https://github.com/oven-sh/bun/releases/download/bun-v1.3.14/bun-linux-x64.zip"
    supplier = "Organization: Oven"

    maintainers("aprozo")

    license("MIT AND LGPL-2.1-only", checked_by="aprozo")

    skip_version_audit = ["platform=windows"]

    sanity_check_is_file = ["bin/bun"]

    bun_versions = {
        "1.4.4": {
            "linux": {
                "x86_64": "bf8ccbfb2b0b80159e0f9a6d15c55317add8077534dbc6130a3edb52fccb395c",
                "aarch64": "baa6bb36f51d6e58561e02bbea825038a9df454f673d6d776e8bbf86f8c7850e",
            },
            "darwin": {
                "x86_64": "50a3491f73abc2fe81673171a85762d3bc2cc1680ccecadd983de99adf77977e",
                "arm64": "c240d7f0ccb90c263a849fcdb09b7ee62630d921348ed6aafda86b9d577bc510",
            },
        },
        "1.3.14": {
            "linux": {
                "x86_64": "951ee2aee855f08595aeec6225226a298d3fea83a3dcd6465c09cbccdf7e848f",
                "aarch64": "a27ffb63a8310375836e0d6f668ae17fa8d8d18b88c37c821c65331973a19a3b",
            },
            "darwin": {
                "x86_64": "4183df3374623e5bab315c547cfa0974533cd457d86b73b639f7a87974cd6633",
                "arm64": "d8b96221828ad6f97ac7ac0ab7e95872341af763001e8803e8267652c2652620",
            },
            "deprecated": True,
        },
    }

    zip_name = {
        "linux": {"x86_64": "linux-x64", "aarch64": "linux-aarch64"},
        "darwin": {"x86_64": "darwin-x64", "arm64": "darwin-aarch64"},
    }

    system = platform.system().lower()
    machine = platform.machine().lower()

    for ver in bun_versions:
        if system in bun_versions[ver] and machine in bun_versions[ver][system]:
            version(
                ver,
                sha256=bun_versions[ver][system][machine],
                deprecated=bun_versions[ver].get("deprecated", False),
            )

    def url_for_version(self, version):
        target = self.zip_name.get(self.system, {}).get(self.machine)

        if target is None:
            return None

        return f"https://github.com/oven-sh/bun/releases/download/bun-v{version}/bun-{target}.zip"

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("bun", prefix.bin)
        set_executable(prefix.bin.bun)
        symlink("bun", join_path(prefix.bin, "bunx"))
