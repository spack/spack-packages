# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lean4(CMakePackage):
    """Lean 4 programming language and theorem prover.

    Lean is an open-source programming language and proof assistant
    that enables correct, maintainable, and formally verified code.
    """

    homepage = "https://lean-lang.org"
    url = "https://github.com/leanprover/lean4/archive/refs/tags/v4.30.0.tar.gz"
    git = "https://github.com/leanprover/lean4.git"

    supplier = "Organization: Lean FRO"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("4.30.0", sha256="c11edd040d77be85865e41b4a37a77d14f824c07d8642434eb3561163f2afa5d")

    variant("gmp", default=True, description="Use GMP for big integers")
    variant("mimalloc", default=True, description="Use mimalloc as the allocator")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.21:", type="build")

    depends_on("libuv")

    depends_on("gmp", when="+gmp")

    def cmake_args(self):
        args = [
            self.define_from_variant("USE_GMP", "gmp"),
            self.define_from_variant("USE_MIMALLOC", "mimalloc"),
        ]
        return args
