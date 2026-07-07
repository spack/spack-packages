# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Coinmp(AutotoolsPackage):
    """C-API library for CLP, CBC, and CGL."""

    homepage = "https://github.com/coin-or/CoinMP"
    url = "https://github.com/coin-or/CoinMP/archive/refs/tags/releases/1.8.4.tar.gz"
    git = "https://github.com/coin-or/CoinMP.git"

    license("CPL-1.0")

    version("1.8.4", sha256="ec03a5110d9d79da950669e3400f3b81c4391747b14821d8997f9f8755873150")
    version("1.8.3", sha256="a7a70b5a2f19eb57f55ce079c0b83ca36507ba83118a1ade52e46cb75b35bcb1")
    version("1.7.6", sha256="d7316e2f11886d1b14d0be82990305e33f4b034f2251f05c206168b854f5010a")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("coinutils")
    depends_on("osi")
    depends_on("clp")
    depends_on("cgl")
    depends_on("cbc")
