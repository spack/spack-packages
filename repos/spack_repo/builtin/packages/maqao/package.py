# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

# Declaring versions depending on architecture
_versions = {
    "2025.1.0": {
        "x86_64": (
            "e28f4c3ad8f15aaf455b46d6c46f6451fa8aef51ffee134bb766f98570941c8c",
            "https://www.maqao.org/maqao_archive/maqao.x86_64.2025.1.0.tar.xz",
        ),
        "aarch64": (
            "993d610a3625c7ff605233a388981d87a2f42741a900c29e5de1e47ae69e5b67",
            "https://www.maqao.org/maqao_archive/maqao.aarch64.2025.1.0.tar.xz",
        ),
    }
}


class Maqao(Package):
    """MAQAO performance analysis framework"""

    homepage = "https://www.maqao.org"

    maintainers("cvalensi")

    license("LGPL-2.1-or-later", checked_by="cvalensi")

    # Loading version corresponding to the architecture
    for ver, package in _versions.items():
        archpack = package.get(f"{platform.machine()}")
        if archpack:
            version(ver, sha256=archpack[0], url=archpack[1], extension="tar.xz")

    def install(self, spec, prefix):
        # Checking platform is Linux
        if spec.platform != "linux":
            raise InstallError(
                "Unsupported platform: {0}. Supported platforms: linux".format(spec.platform)
            )
        # Checking architecture is either x86_64 or aarch64
        arch = spec.target.family
        if arch not in ["x86_64", "aarch64"]:
            raise InstallError(
                "Unsupported architecture: {0}. Supported architectures: x86_64, aarch64".format(
                    arch
                )
            )
        # Installing from archive
        tar = which("tar")
        tar("xJf", self.stage.archive_file)
        install_tree(".", prefix)
