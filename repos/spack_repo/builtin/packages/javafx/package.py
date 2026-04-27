# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "21.0.8": {
        "linux": {
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/21.0.8/openjfx-21.0.8_linux-x64_bin-sdk.zip",
                "203530224e01b5a4b65e8c78f2569e5c491115b3523c0678b5b813b28402b562",
            )
        },
        "darwin": {
            "arm64": (
                "https://download2.gluonhq.com/openjfx/21.0.8/openjfx-21.0.8_osx-aarch64_bin-sdk.zip",
                "261c429c6f55adccab13a937781c18e07d71b9c16355c6b420962443e5f9e85a",
            ),
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/21.0.8/openjfx-21.0.8_osx-x64_bin-sdk.zip",
                "35ae9f9a4b1a3a3d40102ca519c2f4e04e63b8368fab8d57323a8c07ba2ad0a5",
            ),
        },
    },
    "20.0.1": {
        "linux": {
            "aarch64": (
                "https://download2.gluonhq.com/openjfx/20.0.1/openjfx-20.0.1_linux-aarch64_bin-sdk.zip",
                "ded4555c2fa097b3c0307ed3b338956ea1052d1693864c7594ec7ebb7e9486e2",
            ),
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/20.0.1/openjfx-20.0.1_linux-x64_bin-sdk.zip",
                "882082b01a7f46792074cbe58e90136b81413438de184a941e051b836cbe90a2",
            ),
        },
        "darwin": {
            "arm64": (
                "https://download2.gluonhq.com/openjfx/20.0.1/openjfx-20.0.1_osx-aarch64_bin-sdk.zip",
                "baebdbbe283c17df62fc4c0bdc2bde4415f2253f99ba41437f9336e2272c255e",
            ),
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/20.0.1/openjfx-20.0.1_osx-x64_bin-sdk.zip",
                "aa01f301bc611997f60ac86c2d9a7d7d1f652fd7092745720ae49cf7bb2935e4",
            ),
        },
    },
    "17.0.16": {
        "linux": {
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/17.0.16/openjfx-17.0.16_linux-x64_bin-sdk.zip",
                "0460f70d19da9791abdbfe4ae8280e540500fad95fdeb8b833de6e05cbaadcb9",
            )
        },
        "darwin": {
            "arm64": (
                "https://download2.gluonhq.com/openjfx/17.0.16/openjfx-17.0.16_osx-aarch64_bin-sdk.zip",
                "8f1bf9d0ceacfba71232a219dba8ef6e4923c811bdf87381c2f6946e6695225f",
            ),
            "x86_64": (
                "https://download2.gluonhq.com/openjfx/17.0.16/openjfx-17.0.16_osx-x64_bin-sdk.zip",
                "3034b2ad1e0a5f4bd29984b036a2e5111a6d1c3004317972061e9f7912e70b5c",
            ),
        },
    },
}


class Javafx(Package):
    """JavaFX allows you to create Java applications with a
    modern, hardware-accelerated user interface that is
    highly portable.
    """

    homepage = "https://openjfx.io/"
    for i in _versions:
        try:
            url, sha256 = _versions[i][platform.system().lower()][platform.machine()]
            version(i, url=url, sha256=sha256)
        except KeyError:
            continue

    skip_version_audit = ["platform=windows"]

    maintainers("snehring")

    extends("openjdk")

    depends_on("openjdk@17:", when="@20:21")
    depends_on("openjdk@11:", when="@17")

    conflicts("target=ppc64le:", msg="JavaFX is not available for ppc64le")
    conflicts("target=ppc64:", msg="JavaFX is not available for ppc64")
    conflicts("target=riscv64:", msg="JavaFX is not available for riscv64")
    conflicts("target=x86", msg="JavaFX is not available for x86")

    def install(self, spec, prefix):
        install_tree("legal", prefix.legal)
        install_tree("lib", prefix.lib)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("JAVAFX_HOME", self.prefix.lib)
