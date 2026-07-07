# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "0.7.1": {
        "Linux-x86_64": (
            "946571d9ea164f948e402dd97a14541cb90fbec800336cfa7ae644af5937632f",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.1.4_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "f283c31b6badf4a5277014295705eac8e6e28f27de30d746719ea1cef7a750b8",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.7.1.4_cuda12-archive.tar.xz",
        ),
    },
    "0.7.0": {
        "Linux-x86_64": (
            "c98d5ef87e8b6a356b21a678715033b19620ce58b5fa64c97e25e6d3e76e42dc",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.7.0.20_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "ce3de5e6a0cee00fd1fc355881308ef0c692c6e14b6a5625aa35a7f9df98b846",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.7.0.20_cuda12-archive.tar.xz",
        ),
    },
    "0.6.0": {
        "Linux-x86_64": (
            "159ce1d4e3e4bba13b0bd15cf943e44b869c53b7a94f9bac980768c927f02e75",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.6.0.5_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "e6f5d5122d735f9dbfd42c9eaba067a557a5613ee4a6001806935de11aff4b09",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.6.0.5_cuda12-archive.tar.xz",
        ),
    },
    "0.5.0": {
        "Linux-x86_64": (
            "5245d2ba26a590839e2f1dd074f87e39ee5cc201c3b29245b35c7060d59c37a5",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-x86_64/libcudss-linux-x86_64-0.5.0.16_cuda12-archive.tar.xz",
        ),
        "Linux-aarch64": (
            "5d07496e90fc0afb334a7e434c86c6083b1e8cf56dc65d70a01bd811e54096d7",
            "https://developer.download.nvidia.com/compute/cudss/redist/libcudss/linux-aarch64/libcudss-linux-aarch64-0.5.0.16_cuda12-archive.tar.xz",
        ),
    },
}


class Cudss(Package):
    """NVIDIA cuDSS is a GPU-accelerated Direct Sparse Solver library
    for solving linear systems with very sparse matrices"""

    homepage = "https://developer.nvidia.com/cudss"

    maintainers("ddement")

    skip_version_audit = ["platform=darwin", "platform=windows"]

    for ver, packages in _versions.items():
        pkg = packages.get(f"{platform.system()}-{platform.machine()}")
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1])

    depends_on("cuda@12:")

    def install(self, spec, prefix):
        install_tree(".", prefix)
