# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Deno(Package):
    """A modern runtime for JavaScript and TypeScript."""

    homepage = "https://docs.deno.com/"
    url = "https://dl.deno.land/release/v2.4.2/deno-x86_64-unknown-linux-gnu.zip"

    # installation is reproducing what the install script does:
    # https://github.com/denoland/deno_install/blob/master/install.sh

    skip_version_audit = ["platform=windows"]

    deno_versions = {
        "2.4.2": {
            "linux": {
                "x86_64": {
                    "sha256": "d84778633215b7cb93cf7690860d6241f632b087bd2a19de12cd410e6b2e157a",
                    "target": "x86_64-unknown-linux-gnu",
                },
                "aarch64": {
                    "sha256": "4a3218e3ca99f2abbc41d20691bca7942d18ebcb01db6b4389cbb91eabf1055f",
                    "target": "aarch64-unknown-linux-gnu",
                },
            },
            "darwin": {
                "x86_64": {
                    "sha256": "fa47eb72b8d1f3499a7fb3e6c7bbcd3b1e6407112bb03fafd40aa8038a54b93e",
                    "target": "x86_64-apple-darwin",
                },
                "arm64": {
                    "sha256": "732f3ce50dc64a63972ca4efb48679299c01663ce918f710d695a68ce5f4c936",
                    "target": "aarch64-apple-darwin",
                },
            },
            # for some reason windows does not work
            # "windows": {
            #     "x86_64": {
            #         "sha256": "5a8c816f6e720378a74c2567679ba2a799c815b8c2ffc06b0e71da6c2a9bf189",
            #         "target": "x86_64-pc-windows-msvc",
            #     }
            # },
        }
    }

    license("MIT")

    system = platform.system().lower()
    machine = platform.machine().lower()

    for ver in deno_versions:
        if system in deno_versions[ver] and machine in deno_versions[ver][system]:
            version(ver, sha256=deno_versions[ver][system][machine]["sha256"])

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("deno", prefix.bin)

    def url_for_version(self, version):
        ver = version.string

        if (
            self.system not in self.deno_versions[ver]
            and self.machine not in self.deno_versions[ver][self.system]
        ):
            return None

        target = self.deno_versions[ver][self.system][self.machine]["target"]

        return f"https://dl.deno.land/release/{version}/deno-{target}.zip"
