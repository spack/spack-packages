# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class LibnetfilterConntrack(AutotoolsPackage):
    """libnetfilter_conntrack is a userspace library providing a programming
    interface (API) to the in-kernel connection tracking state table."""

    homepage = "https://netfilter.org/projects/libnetfilter_conntrack/"
    url = "https://www.netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-1.0.5.tar.bz2"

    license("GPL-2.0-or-later", checked_by="wdconinc")

    version("1.0.9", sha256="67bd9df49fe34e8b82144f6dfb93b320f384a8ea59727e92ff8d18b5f4b579a8")
    version("1.0.8", sha256="0cd13be008923528687af6c6b860f35392d49251c04ee0648282d36b1faec1cf")
    version("1.0.7", sha256="33685351e29dff93cc21f5344b6e628e41e32b9f9e567f4bec0478eb41f989b6")
    version("1.0.6", sha256="efcc08021284e75f4d96d3581c5155a11f08fd63316b1938cbcb269c87f37feb")
    version("1.0.5", sha256="fc9d7daf43605a73045de203bbfc0bca3e07f72d4ac61bcf656868f48692d73a")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("libmnl@1.0.3:")
    depends_on("libnfnetlink@1.0.0:")
