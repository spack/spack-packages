# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class LibnetfilterCttimeout(AutotoolsPackage):
    """Conntrack timeout policy library."""

    homepage = "https://netfilter.org/projects/libnetfilter_cttimeout/"
    url = "https://www.netfilter.org/projects/libnetfilter_cttimeout/files/libnetfilter_cttimeout-1.0.1.tar.bz2"

    license("GPL-2.0-only", checked_by="wdconinc")

    version("1.0.1", sha256="0b59da2f3204e1c80cb85d1f6d72285fc07b01a2f5678abf5dccfbbefd650325")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("libmnl")
