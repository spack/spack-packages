# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Linbox(AutotoolsPackage):
    """LinBox is a C++ template library for exact, high-performance linear
    algebra computation with dense, sparse, and structured matrices over
    the integers and over finite fields."""

    homepage = "https://linalg.org/"
    url = "https://github.com/linbox-team/linbox/releases/download/v1.7.1/linbox-1.7.1.tar.gz"

    maintainers("d-torrance")

    license("LGPL-2.1-or-later", checked_by="d-torrance")

    version("1.7.1", sha256="a2b5f910a54a46fa75b03f38ad603cae1afa973c95455813d85cf72c27553bd8")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("fflas-ffpack")
    depends_on("givaro")

    variant("flint", default=False, description="Enable FLINT support")
    depends_on("flint", when="+flint")

    variant("fplll", default=False, description="Enable fpLLL support")
    depends_on("fplll", when="+fplll")
    depends_on("mpfr", when="+fplll")

    variant("ntl", default=False, description="Enable NTL support")
    depends_on("ntl", when="+ntl")

    def configure_args(self):
        args = []
        for dep in ["flint", "fplll", "mpfr", "ntl"]:
            if self.spec.satisfies(f"^{dep}"):
                args.append(f"--with-{dep}={self.spec[dep].prefix}")
            else:
                args.append(f"--without-{dep}")
        return args
