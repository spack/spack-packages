# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Megahit(CMakePackage, MakefilePackage):
    """Ultra-fast and memory-efficient (meta-)genome assembler"""

    homepage = "https://github.com/voutcn/megahit"
    url = "https://github.com/voutcn/megahit/archive/refs/tags/v1.2.9.tar.gz"

    license("GPL-3.0-only")

    build_system("cmake", "makefile", default="cmake")

    version("1.2.9", sha256="09026eb07cc4e2d24f58b0a13f7a826ae8bb73da735a47cb1cbe6e4693118852")
    version("1.1.4", sha256="ecd64c8bfa516ef6b19f9b2961ede281ec814db836f1a91953c213c944e1575f")
    version("1.1.3", sha256="b6eefdee075aaf7a8f9090e2e8b08b770caff90aa43a255e0e220d82ce71c492")

    variant(
        "generator",
        default="make",
        values=("make", "ninja"),
        when="build_system=cmake",
        description="CMake generator",
    )

    depends_on("zlib-api")

    # CMake path
    depends_on("cmake@2.8:", type="build", when="@1.2.9: build_system=cmake")
    depends_on("gcc@4.8.4:", type="build", when="@1.2.9: build_system=cmake")
    depends_on("c", type="build", when="@1.2.9: build_system=cmake")
    depends_on("cxx", type="build", when="@1.2.9: build_system=cmake")

    depends_on("gzip", type="run", when="@1.2.9: build_system=cmake")
    depends_on("bzip2", type="run", when="@1.2.9: build_system=cmake")

    # Makefile path
    depends_on("c", type="build", when="build_system=makefile")
    depends_on("cxx", type="build", when="build_system=makefile")

    patch("amd.patch", when="@1.1.4 target=aarch64:")


class MakefileBuilder(makefile.MakefileBuilder):
    def install(self, pkg, spec, prefix):
        mkdirp(prefix.bin)
        install("megahit", prefix.bin)
        install("megahit_asm_core", prefix.bin)
        install("megahit_sdbg_build", prefix.bin)
        install("megahit_toolkit", prefix.bin)
