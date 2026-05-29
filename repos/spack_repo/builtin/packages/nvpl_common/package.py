# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class NvplCommon(Package):
    """
    NVPL Common provides CMake packages for NVIDIA Performance Libraries (NVPL).
    """

    homepage = "https://docs.nvidia.com/nvpl/latest/index.html"
    url = (
        "https://developer.download.nvidia.com/compute/nvpl/redist"
        "/nvpl_common/linux-sbsa/nvpl_common-linux-sbsa-0.1.0.1-archive.tar.xz"
    )

    maintainers("rbberger")

    redistribute(source=False, binary=False)

    license("NVIDIA Software License Agreement")

    version("0.3.4", sha256="c68891dd293df0faf2ae3cebfeae69c567cf784c98006351abcde2a34fc387df")
    version("0.3.3", sha256="fe87ccd63817427c6c9b9e292447a4e8f256b9c9157065fba1a338719fa433c8")
    version("0.3.2", sha256="66c4d3d2772b10f40e5d92fa2bf92b68d33db58d4c448bfbb9f94bfe5ab94720")
    version("0.3.1", sha256="8a516d983a5e6ddc299aacaccc7992c3028e1abbd020a47ffcdb0219187e41b6")
    version("0.3.0", sha256="3019e73b6ea93ea41113fa6aab268ff1e76c706c2b5fea6a9a033b177e30fbbf")
    version("0.2.0.1", sha256="8b3c65cb5001fd09be1f020582822e2a040a0ad8a30093f58f2eedbcee1e8ff6")
    version("0.1.0.1", sha256="aa72c18dbbcfd882d77776370896fb4678bc92cf0dca3d868ae51b495ad59413")

    def url_for_version(self, version):
        return f"https://developer.download.nvidia.com/compute/nvpl/redist/nvpl_common/linux-sbsa/nvpl_common-linux-sbsa-{version}-archive.tar.xz"

    def install(self, spec, prefix):
        install_tree(".", prefix)
