# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libmnl(AutotoolsPackage):
    """libmnl is a minimalistic user-space library oriented to Netlink
    developers. There are a lot of common tasks in parsing, validating,
    constructing of both the Netlink header and TLVs that are repetitive
    and easy to get wrong. This library aims to provide simple helpers
    that allows you to re-use code and to avoid re-inventing the wheel."""

    homepage = "https://netfilter.org/projects/libmnl/"
    url = "https://netfilter.org/projects/libmnl/files/libmnl-1.0.5.tar.bz2"

    license("LGPL-2.1-or-later", checked_by="wdconinc")

    version("1.0.5", sha256="274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
