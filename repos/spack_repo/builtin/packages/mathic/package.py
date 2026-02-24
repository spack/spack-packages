# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mathic(AutotoolsPackage):
    """Mathic is a C++ library providing optimized data structures for
    Gröbner basis computation. It includes support for ordering
    S-pairs, divisor queries, and polynomial term ordering during
    reduction. The library is template-based and can be used with
    arbitrary monomial and coefficient representations, though it
    currently works best with dense term representations."""

    homepage = "https://github.com/Macaulay2/mathic"
    url = "https://github.com/Macaulay2/mathic/releases/download/v1.1/mathic-1.1.tar.gz"
    git = "https://github.com/Macaulay2/mathic"

    maintainers("d-torrance")

    license("LGPL-2.0-or-later", checked_by="d-torrance")

    version("1.2", sha256="1a7d459290e9183e0934a6dd2278db372b831b37fdb4a6f1db7e02e0f380fe1a")
    version("1.1", sha256="2499fb3df3c2f8a201ae5627cad95538aaabee0eee235002b8737bdb842b694a")
    version("1.0.2025.05.13", commit="7abf77e4ce493b3830c7f8cc09722bbd6c03818e")

    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("memtailor")

    def configure_args(self):
        return ["--enable-shared"]
