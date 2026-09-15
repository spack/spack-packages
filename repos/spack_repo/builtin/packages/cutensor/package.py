# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "2.8.0.6-13": {
        "Linux-x86_64": "2a1a37e4c030b779748ea2f4cda3c283ea5613f7ed9f24d03adf524c7455f98e",
        "Linux-aarch64": "cbe3069e9776c2b4421f5d13c01011352a16929caad3b1eaf74839ee91e6768e",
    },
    "2.8.0.6-12": {
        "Linux-x86_64": "a265120c0e64723e9f43aa03ca51af55126d0f8266c256e003ced8340f7fa966",
        "Linux-aarch64": "b9c391c8e9c4752f03b37b8c57058ac513a477f5388d708743ed46222355f849",
    },
    "2.0.1.2": {
        "Linux-x86_64": "ededa12ca622baad706ea0a500a358ea51146535466afabd96e558265dc586a2",
        "Linux-ppc64le": "7176083a4dad44cb0176771be6efb3775748ad30a39292bf7b4584510f1dd811",
        "Linux-aarch64": "4214a0f7b44747c738f2b643be06b2b24826bd1bae6af27f29f3c6dec131bdeb",
    },
    "1.5.0.3": {
        "Linux-x86_64": "4fdebe94f0ba3933a422cff3dd05a0ef7a18552ca274dd12564056993f55471d",
        "Linux-ppc64le": "ad736acc94e88673b04a3156d7d3a408937cac32d083acdfbd8435582cbe15db",
        "Linux-aarch64": "5b9ac479b1dadaf40464ff3076e45f2ec92581c07df1258a155b5bcd142f6090",
    },
}


class Cutensor(Package):
    """NVIDIA cuTENSOR Library is a GPU-accelerated tensor linear algebra
    library providing tensor contraction, reduction and elementwise
    operations."""

    homepage = "https://developer.nvidia.com/cutensor"

    maintainers("bvanessen")
    url = "cutensor"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    for ver, packages in _versions.items():
        pkg = packages.get(f"{platform.system()}-{platform.machine()}")
        if pkg:
            version(ver, sha256=pkg)

            ver_split = ver.split("-")
            if len(ver_split) == 2:
                _, cuda_ver = ver_split
                depends_on(f"cuda@{cuda_ver}", when=f"@{ver}")

    # Default CUDA dependencie
    depends_on("cuda@11:" if platform.machine() == "aarch64" else "cuda@10:")

    def url_for_version(self, version):
        # Get the system and machine arch for building the file path
        sys = "{0}-{1}".format(platform.system(), platform.machine())
        # Munge it to match Nvidia's naming scheme
        sys_key = sys.lower()
        sys_key = sys_key.replace("aarch64", "sbsa")

        # After version 2.2.0, Nvidia started distributing separated packages
        # depending on the CUDA version
        if version >= Version("2.3"):
            cutensor_ver, cuda_ver = str(version).split("-")
            filename = f"libcutensor-{sys_key}-{cutensor_ver}_cuda{cuda_ver}-archive.tar.xz"
        else:
            filename = f"libcutensor-{sys_key}-{version}-archive.tar.xz"

        return f"https://developer.download.nvidia.com/compute/cutensor/redist/libcutensor/{sys_key}/{filename}"

    def install(self, spec, prefix):
        install_tree(".", prefix)
