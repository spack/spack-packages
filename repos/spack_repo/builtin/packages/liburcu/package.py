# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Liburcu(AutotoolsPackage):
    """liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library.
    This data synchronization library provides read-side access which
    scales linearly with the number of cores."""

    homepage = "https://liburcu.org"
    url = "https://lttng.org/files/urcu/userspace-rcu-0.14.0.tar.bz2"
    git = "https://git.lttng.org/userspace-rcu.git"

    license("LGPL-2.1", checked_by="wdconinc")

    version("0.15.7", sha256="2556b83adc0f9b3ac8024e613e17d014d04c4c49110604ce55fcb14eae32edd3")
    version("0.15.6", sha256="850b192096eb11ebf2c70e8f97bc7da7479ee41da1bebeb44e3986908bac414f")
    version("0.15.5", sha256="b2f787a8a83512c32599e71cdabcc5131464947b82014896bd11413b2d782de1")
    version("0.15.4", sha256="11a14a7660ac9ba9c0bbd3b2d81718523d27dc6c8a9dfabd5e401b406673ee3a")
    version("0.15.3", sha256="26687ec84e3e114759454c884a08abeaf79dec09b041895ddf4c45ec150acb6d")
    version("0.15.2", sha256="59f36f2b8bda1b7620a7eced2634f26c549444818a8313025a3bb09c0766a61d")
    version("0.15.1", sha256="98d66cc12f2c5881879b976f0c55d10d311401513be254e3bd28cf3811fb50c8")
    version("0.15.0", sha256="4f2d839af67905ad396d6d53ba5649b66113d90840dcbc89941e0da64bccd38c")
    version("0.14.3", sha256="bdcbf18ed37911f489851aa80e98b8d5bc565b329ee2fb66c11ee7a019f43aa0")
    version("0.14.2", sha256="1337c49658367ca6df3c09a7c02303f752e2d964aa98518f4593f7781ad7aac2")
    version("0.14.1", sha256="231acb13dc6ec023e836a0f0666f6aab47dc621ecb1d2cd9d9c22f922678abc0")
    version("0.14.0", sha256="ca43bf261d4d392cff20dfae440836603bf009fce24fdc9b2697d837a2239d4f")

    depends_on("autoconf@2.69:", type="build")
    depends_on("automake@1.12:", type="build")

    def patch(self):
        filter_file("-Wl,-rpath ", "-Wl,-rpath,", "doc/examples/Makefile.in")
