# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Frobby(MakefilePackage):
    """Frobby is a software system for computations with monomial
    ideals, intended for research in computational algebra. It
    supports Euler characteristics, Hilbert series, maximal standard
    monomials, combinatorial optimization, primary and irreducible
    decomposition, Alexander duals, associated primes, minimization
    and intersection of monomial ideals, and the computation of
    Frobenius problems with very large numbers."""

    homepage = "https://github.com/Macaulay2/frobby"
    git = "https://github.com/Macaulay2/frobby"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("0.9.5", tag="v0.9.5", commit="cbda56e8bb0d706f8cd7e6594a8a034797f53eb5")

    depends_on("cxx", type="build")

    depends_on("gmp")

    def build(self, spec, prefix):
        make("all")
        make("library", "RANLIB=ranlib")  # static library
        make("library", "MODE=shared")

    def install(self, spec, prefix):
        make("install", f"PREFIX={prefix}", f"BIN_INSTALL_DIR={prefix.bin}")
        mkdirp(prefix.lib)
        mkdirp(prefix.include)
        install("bin/libfrobby.a", prefix.lib)
        install("bin/libfrobby.so", prefix.lib)
        install("src/frobby.h", prefix.include)
