# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Metaeuk(CMakePackage):
    """MetaEuk is a modular toolkit designed for large-scale gene discovery
    and annotation in eukaryotic metagenomic contigs.
    """

    homepage = "https://metaeuk.soedinglab.org/"
    url = "https://github.com/soedinglab/metaeuk/archive/refs/tags/6-a5d39d9.tar.gz"
    maintainers("snehring")

    license("GPL-3.0-or-later")

    version("6-a5d39d9", sha256="be19c26f5bdb7dcdd7bc48172105afecf19e5a2e5555edb3ba0c4aa0e4aac126")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@2.8.12:", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Same class of bug as spades: mmseqs2 (vendored inside metaeuk)
        # uses fixed-width int types (uint32_t/uint64_t/...) all over the
        # place but relies on getting <cstdint> transitively from whatever
        # standard header happened to pull it in on older GCC -- GCC 14's
        # libstdc++ doesn't. A static scan found 47 affected files, way
        # too many to patch one by one and too easy for a 48th to slip
        # through later. Force the header into every translation unit at
        # the compiler level instead of chasing individual includes.
        # <cstdint> is the C++ wrapper header, not visible to the plain C
        # compiler -- the equivalent for .c files is <stdint.h>.
        env.append_flags("CFLAGS", "-include stdint.h")
        env.append_flags("CXXFLAGS", "-include cstdint")
