# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Iperf3(AutotoolsPackage):
    """The iperf series of tools perform active measurements to determine the
    maximum achievable bandwidth on IP networks. iperf2 is a separately
    maintained project."""

    homepage = "https://software.es.net/iperf/"
    url = "https://downloads.es.net/pub/iperf/iperf-3.17.tar.gz"

    license("BSD-3-Clause-LBNL")

    version("3.21", sha256="656e4405ebd620121de7ceca3eaf43a88f79ea1b857d041a6a0b1314801acdd8")
    version("3.20", sha256="3acc572d1ecca4e0b20359c7bf0132ddc80d982efeee20c86f6726a9a6094388")
    version("3.19.1", sha256="dc63f89ec581ea99f8b558d8eb35109de06383010db5a1906c208a562ba0c270")
    version("3.19", sha256="040161da1555ec7411a9d81191049830ef37717d429a94ee6cf0842618e0e29c")
    version("3.18", sha256="c0618175514331e766522500e20c94bfb293b4424eb27d7207fb427b88d20bab")
    version("3.17.1", sha256="84404ca8431b595e86c473d8f23d8bb102810001f15feaf610effd3b318788aa")
    version("3.17", sha256="077ede831b11b733ecf8b273abd97f9630fd7448d3ec1eaa789f396d82c8c943")
    version("3.16", sha256="cc740c6bbea104398cc3e466befc515a25896ec85e44a662d5f4a767b9cf713e")
    version("3.14", sha256="723fcc430a027bc6952628fa2a3ac77584a1d0bd328275e573fc9b206c155004")
    version("3.12", sha256="72034ecfb6a7d6d67e384e19fb6efff3236ca4f7ed4c518d7db649c447e1ffd6")
    version("3.9", sha256="24b63a26382325f759f11d421779a937b63ca1bc17c44587d2fcfedab60ac038")
    version("3.6", sha256="de5d51e46dc460cc590fb4d44f95e7cad54b74fea1eba7d6ebd6f8887d75946e")

    depends_on("c", type="build")  # generated

    conflicts("%gcc@15:", when="@:3.18")  # https://github.com/esnet/iperf/issues/1838
