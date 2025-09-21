# Copyright Spack Project Developers. See COPYRIGHT file for details.
#

# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Msolve(AutotoolsPackage):
    """msolve is an open-source C library for solving multivariate polynomial
    systems with rational or finite field coefficients. It provides algorithms
    for computing Gröbner bases, isolating real roots, and determining
    invariants such as the dimension and degree of the solution set, along with
    related tools for polynomial system solving."""

    homepage = "https://msolve.lip6.fr/"
    url = "https://github.com/algebraic-solving/msolve/archive/refs/tags/v0.9.3.tar.gz"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("0.9.3", sha256="2e46b88b38abbe4e4937ef5fc4a90a006d1ff933ffa7563287b5d756de3bcf6e")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("c", type="build")

    depends_on("flint")
    depends_on("gmp")
    depends_on("mpfr")
