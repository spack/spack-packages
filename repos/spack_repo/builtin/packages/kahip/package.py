# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kahip(CMakePackage):
    """KaHIP - Karlsruhe High Quality Partitioning - is a family of graph
    partitioning programs. It includes KaFFPa (Karlsruhe Fast Flow
    Partitioner), which is a multilevel graph partitioning algorithm,
    in its variants Strong, Eco and Fast, KaFFPaE (KaFFPaEvolutionary)
    which is a parallel evolutionary algorithm that uses KaFFPa to
    provide combine and mutation operations, as well as KaBaPE which
    extends the evolutionary algorithm. Moreover, specialized
    techniques are included to partition road networks (Buffoon), to
    output a vertex separator from a given partition or techniques
    geared towards efficient partitioning of social networks.
    """

    homepage = "https://algo2.iti.kit.edu/documents/kahip/index.html"
    url = "https://github.com/KaHIP/KaHIP/archive/v3.14.tar.gz"
    git = "https://github.com/KaHIP/KaHIP.git"
    maintainers("ma595")

    license("MIT")

    version("develop", branch="master")
    version("3.14", sha256="9da04f3b0ea53b50eae670d6014ff54c0df2cb40f6679b2f6a96840c1217f242")
    version("3.13", sha256="fae21778a4ce8e59ccb98e5cbb6c01f0af7e594657d21f6c0eb2c6e74398deb1")
    version("3.12", sha256="df923b94b552772d58b4c1f359b3f2e4a05f7f26ab4ebd00a0ab7d2579f4c257")
    version("3.11", sha256="347575d48c306b92ab6e47c13fa570e1af1e210255f470e6aa12c2509a8c13e3")

    variant(
        "deterministic",
        default=False,
        when="@3.13:",
        description="Compile with the deterministic seed",
    )
    variant("metis", default=False, description="metis support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("argtable")
    depends_on("mpi")  # Note: upstream package only tested on openmpi
    depends_on("metis", when="@3.12: +metis")

    conflicts("%apple-clang")
    conflicts("%clang")

    patch("cstdint.patch")

    @when("@3.13:")
    def cmake_args(self):
        return [self.define_from_variant("DETERMINISTIC_PARHIP", "deterministic")]
