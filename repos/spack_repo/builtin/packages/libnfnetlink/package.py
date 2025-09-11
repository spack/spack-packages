# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libnfnetlink(AutotoolsPackage):
    """libnfnetlink is a userspace library that provides some low-level
    nfnetlink handling functions.  It is used as a foundation for other,
    netfilter subsystem specific libraries such as libnfnetlink_conntrack,
    libnfnetlink_log and libnfnetlink_queue."""

    homepage = "https://netfilter.org/projects/libnfnetlink/"
    url = "https://netfilter.org/projects/libnfnetlink/files/libnfnetlink-1.0.2.tar.bz2"

    license("GPL-2.0-only")

    version("1.0.2", sha256="b064c7c3d426efb4786e60a8e6859b82ee2f2c5e49ffeea640cfe4fe33cbc376")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
