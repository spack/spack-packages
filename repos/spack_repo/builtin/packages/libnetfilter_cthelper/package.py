# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class LibnetfilterCthelper(AutotoolsPackage):
    """Libnetfilter-cthelper library for user space helpers / ALGs"""

    homepage = "https://netfilter.org/projects/libnetfilter_cthelper/"
    url = "https://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-1.0.5.tar.bz2"

    license("GPL-2.0-or-later")

    version("1.0.1", sha256="14073d5487233897355d3ff04ddc1c8d03cc5ba8d2356236aa88161a9f2dc912")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("libmnl@1.0:")
