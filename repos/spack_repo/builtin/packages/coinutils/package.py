# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Coinutils(AutotoolsPackage):
    """CoinUtils is an open-source collection of classes and helper
    functions that are generally useful to multiple COIN-OR
    projects."""

    homepage = "https://projects.coin-or.org/Coinutils"
    url = "https://github.com/coin-or/CoinUtils/archive/releases/2.11.13.tar.gz"

    license("EPL-2.0")

    version("2.11.13", sha256="ddfea48e10209215748bc9f90a8c04abbb912b662c1aefaf280018d0a181ef79")
    version("2.11.10", sha256="80c7c215262df8d6bd2ba171617c5df844445871e9891ec6372df12ccbe5bcfd")
    version("2.11.9", sha256="15d572ace4cd3b7c8ce117081b65a2bd5b5a4ebaba54fadc99c7a244160f88b8")
    version("2.11.6", sha256="6ea31d5214f7eb27fa3ffb2bdad7ec96499dd2aaaeb4a7d0abd90ef852fc79ca")
    version("2.11.4", sha256="d4effff4452e73356eed9f889efd9c44fe9cd68bd37b608a5ebb2c58bd45ef81")
    version("2.10.15", sha256="b10e4ef56118f6c090e637fc75b84e8e0001c1ce5d867a834e9ff5ef03f119ad")
    version("2.10.10", sha256="f6c90b2a042faae84a6e8d56851283f594610372e0a54835f042de2d364541d6")
    version("2.9.19", sha256="0eb6139ff6d4dcc8957ef6a73b74d62c48339471595e70d67ba3e6470a8eab05")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    build_directory = "spack-build"

    def setup_build_environment(self, env):
        if self.spec.satisfies("%gcc@11:") and self.spec.satisfies("@:2.10.13"):
            # older autoconf script fails to set this variable with newer GCC versions
            env.append_flags("CXXFLAGS", "-DHAVE_CFLOAT=1")
