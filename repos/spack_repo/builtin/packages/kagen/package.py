# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kagen(CMakePackage):
    """KaGen - Communication-free Massively Distributed Graph Generation.

    KaGen provides generators for a variety of network models commonly found
    in practice, including Erdos-Renyi, random geometric, random hyperbolic,
    Barabasi-Albert, random Delaunay, R-MAT, and grid graphs. By using
    pseudorandomization and divide-and-conquer schemes, the generators follow
    a communication-free paradigm, enabling embarrassingly parallel generation
    of graphs with up to 2^43 vertices and 2^47 edges.
    """

    homepage = "https://github.com/KarlsruheGraphGeneration/KaGen"
    url = "https://github.com/KarlsruheGraphGeneration/KaGen/archive/refs/tags/v1.3.0.tar.gz"
    git = "https://github.com/KarlsruheGraphGeneration/KaGen.git"
    maintainers("schulzchristian")

    license("BSD-2-Clause")

    version("develop", branch="main", submodules=True)
    version(
        "1.3.0",
        sha256="3037beb7a3add746921a737a3b7ecc5bdcd6e476a5956f4f8e08116f93142905",
        submodules=True,
    )
    version(
        "1.2.9",
        sha256="52896cf6eaf4a27a064ad82f45d2577b2166b51a825084b562395d8aa5556707",
        submodules=True,
    )
    version(
        "1.2.1",
        sha256="f2d64a3123e2e2e7fe5f95f1af8aa4837f4883cfe471d99c1028c96ae248f4df",
        submodules=True,
    )
    version(
        "1.2.0",
        sha256="fc9935101849b0da151a00ea0bbcdf0f2bf22cc9fa24646f2e0bb0a71ed7a19a",
        submodules=True,
    )
    version(
        "1.1.0",
        sha256="41f7f2f4bee6f7c3de381232652370f1003298e563d98442a31ce43ba4c37a4f",
        submodules=True,
    )

    variant("cgal", default=True, description="Enable RDG generators via CGAL")
    variant("sparsehash", default=False, description="Use Google Sparsehash instead of std::unordered_map")
    variant("xxhash", default=True, description="Enable xxHash for path permutation")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.16:", type="build")
    depends_on("mpi")
    depends_on("cgal", when="+cgal")
    depends_on("sparsehash", when="+sparsehash")
    depends_on("boost", when="+cgal")

    conflicts("%apple-clang")

    def cmake_args(self):
        return [
            self.define_from_variant("KAGEN_USE_CGAL", "cgal"),
            self.define_from_variant("KAGEN_USE_SPARSEHASH", "sparsehash"),
            self.define_from_variant("KAGEN_USE_XXHASH", "xxhash"),
            self.define("KAGEN_BUILD_APPS", True),
            self.define("KAGEN_BUILD_TESTS", False),
            self.define("KAGEN_BUILD_EXAMPLES", False),
        ]
