# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class UserspaceRcu(AutotoolsPackage):
    """liburcu is a LGPLv2.1 userspace RCU (read-copy-update) library. This
    data synchronization library provides read-side access which scales
    linearly with the number of cores."""

    homepage = "https://liburcu.org/"
    url = "https://lttng.org/files/urcu/userspace-rcu-0.15.7.tar.bz2"
    git = "https://git.lttng.org/userspace-rcu.git"

    license("LGPL-2.1-or-later")

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
    version("0.13.3", sha256="49f9336a165a749b6cdb77e9bebf1c03254a5449654855e5d425ee49faa784a8")
    version("0.13.2", sha256="1213fd9f1b0b74da7de2bb74335b76098db9738fec5d3cdc07c0c524f34fc032")
    version("0.13.1", sha256="3213f33d2b8f710eb920eb1abb279ec04bf8ae6361f44f2513c28c20d3363083")
    version("0.13.0", sha256="cbb20dbe1a892c2a4d8898bac4316176e585392693d498766ccbbc68cf20ba20")
    version("0.12.3", sha256="9b50dac590cf1a482965d131a4ef6908255ed38e23eff068d2436fb2e61fd81e")
    version("0.12.2", sha256="4eefc11e4f6c212fc7d84d871e1cc139da0669a46ff3fda557a6fdd4d74ca67b")
    version("0.12.1", sha256="bbfaead0345642b97e0de90f889dfbab4b2643a6a5e5c6bb59cd0d26fc0bcd0e")
    version("0.12.0", sha256="409b1be506989e1d26543194df1a79212be990fe5d4fd84f34f019efed989f97")
    version("0.11.4", sha256="74d53dd35a7d431a3f9e0f0bb3cb184074fe1776162f858810782c9249b09e9a")
    version("0.11.3", sha256="cce7273fdc930ed2da595efab0d8392570d90087f0dc90f7f3b85ed656c7d51e")
    version("0.11.2", sha256="1eca960cbd51fd380c3d750537366f727a62a90706d675ed9aec92314634491c")
    version("0.11.1", sha256="92b9971bf3f1c443edd6c09e7bf5ff3b43531e778841f16377a812c8feeb3350")
    version("0.11.0", sha256="1af5694c4f6266f4eba5eb4b832daee600d1e7055fce6da5d514d735d72eb3e7")
    version("0.10.2", sha256="b3f6888daf6fe02c1f8097f4a0898e41b5fe9975e121dc792b9ddef4b17261cc")
    version("0.9.6", sha256="ae43776679739be43feab97ed1e3e4eb381fbc68c4f60811ecd67fe2e7541559")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build", when="@0.14:")

    def patch(self):
        filter_file("-Wl,-rpath ", "-Wl,-rpath,", "doc/examples/Makefile.in")
