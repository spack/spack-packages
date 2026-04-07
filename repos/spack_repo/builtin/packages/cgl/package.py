# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Cgl(AutotoolsPackage):
    """The COIN-OR Cut Generation Library (Cgl) is a collection of cut
    generators that can be used with other COIN-OR packages that make
    use of cuts, such as, among others, the linear solver Clp or the
    mixed integer linear programming solvers Cbc or BCP. Cgl uses the
    abstract class OsiSolverInterface (see Osi) to use or communicate
    with a solver. It does not directly call a solver."""

    homepage = "https://projects.coin-or.org/Cgl"
    url = "https://github.com/coin-or/Cgl/archive/releases/0.60.10.tar.gz"

    license("EPL-2.0")

    version("0.60.10", sha256="41b7ac9402db883d9c487eb7101e59eb513cefd726e6e7a669dc94664d9385e6")
    version("0.60.8", sha256="1482ba38afb783d124df8d5392337f79fdd507716e9f1fb6b98fc090acd1ad96")
    version("0.60.7", sha256="93b30a80b5d2880c2e72d5877c64bdeaf4d7c1928b3194ea2f88b1aa4517fb1b")
    version("0.60.6", sha256="9e2c51ffad816ab408763d6b931e2a3060482ee4bf1983148969de96d4b2c9ce")
    version("0.60.3", sha256="cfeeedd68feab7c0ce377eb9c7b61715120478f12c4dd0064b05ad640e20f3fb")
    version("0.59.11", sha256="b670f69a81fed8eddd3198688b73bd8ee4b6382388901f78df92fcaf97c40a92")
    version("0.59.7", sha256="1bf0fb2012ec535d1c44aea53469d9705967e7bbae5de1d87e1985c90fd6d6a8")
    version("0.58.11", sha256="7503594257d08f48a48fa1cfdd9982aeac8b34b787efb6c9af475bf3f6563d16")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("coinutils@2.11.0:", when="@0.60:")
    depends_on("coinutils@2.10.3:", when="@0.59:")
    depends_on("coinutils")

    depends_on("osi")
    depends_on("clp")

    build_directory = "spack-build"

    def setup_build_environment(self, env):
        # With older versions of GCC, there was a high chance of math headers being included
        # implicitly by other headers, allowing files with missing inclusion to build.

        if self.spec.satisfies("%gcc@11:") and self.spec.satisfies("@:0.59.9"):
            env.append_flags("CXXFLAGS", "-DHAVE_CFLOAT=1")
