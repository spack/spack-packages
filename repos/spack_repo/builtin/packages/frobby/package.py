# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import makefile
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Frobby(AutotoolsPackage, MakefilePackage):
    """Frobby is a software system for computations with monomial
    ideals, intended for research in computational algebra. It
    supports Euler characteristics, Hilbert series, maximal standard
    monomials, combinatorial optimization, primary and irreducible
    decomposition, Alexander duals, associated primes, minimization
    and intersection of monomial ideals, and the computation of
    Frobenius problems with very large numbers."""

    homepage = "https://github.com/Macaulay2/frobby"
    url = "https://github.com/Macaulay2/frobby/releases/download/v0.10.0/frobby-0.10.0.tar.gz"
    git = "https://github.com/Macaulay2/frobby"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    build_system(
        conditional("autotools", when="@0.10:"),
        conditional("makefile", when="@:0.9"),
        default="autotools",
    )

    version("0.10.0", sha256="5baf2133fa47c77fd87728d77b0a26e0a0e1de4a20fddab22619fe69a210ef34")
    version("0.9.9", sha256="4c072c2ee208d853b7173921d45cc7d39297cf3f7fd9c8e7da8e482da3b51aa3")
    version("0.9.8", sha256="a39fdc4d68c20bf7259ef8f11262e0f74df912be5012dfac834545aa40296301")
    version("0.9.7", sha256="efd0a825b67731aa5fb4ea8d2e1004830cc11685be3e09f5401612c411214a96")
    version("0.9.5", tag="v0.9.5", commit="cbda56e8bb0d706f8cd7e6594a8a034797f53eb5")

    depends_on("c", type="build", when="build_system=autotools")
    depends_on("cxx", type="build")

    depends_on("gmp+cxx")

    def url_for_version(self, version):
        base = "https://github.com/Macaulay2/frobby/releases/download"
        if version < Version("0.10"):
            version_sep = "_v"
        else:
            version_sep = "-"
        return f"{base}/v{version}/frobby{version_sep}{version}.tar.gz"


class MakefileBuilder(makefile.MakefileBuilder):
    def build(self, pkg, spec, prefix):
        make("all")
        make("library", "RANLIB=ranlib")  # static library
        make("library", "MODE=shared")

    @when("@0.9.7:")
    def install(self, pkg, spec, prefix):
        make("install", f"PREFIX={prefix}")

    @when("@:0.9.5")
    def install(self, pkg, spec, prefix):
        make("install", f"PREFIX={prefix}", f"BIN_INSTALL_DIR={prefix.bin}")
        mkdirp(prefix.lib)
        mkdirp(prefix.include)
        install("bin/libfrobby.a", prefix.lib)
        install("bin/libfrobby.so", prefix.lib)
        install("src/frobby.h", prefix.include)
