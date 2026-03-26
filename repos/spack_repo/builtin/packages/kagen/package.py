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
    git = "https://github.com/KarlsruheGraphGeneration/KaGen.git"
    maintainers("schulzchristian")

    license("BSD-2-Clause")

    version("main", branch="main", submodules=True)
    version(
        "1.3.0", tag="v1.3.0", commit="4443548b96b3bea903ce66438034906814bf1622", submodules=True
    )
    version(
        "1.2.9", tag="v1.2.9", commit="786579bbfbf8c81b2d2ab52c431ce5c7a8d068a4", submodules=True
    )
    version(
        "1.2.1", tag="v1.2.1", commit="7bfcf979e746580ddd8402c07216750c640bc24e", submodules=True
    )
    version(
        "1.2.0", tag="v1.2.0", commit="66c6349a8f9ba700a84acc6ece4c992ab50bf8af", submodules=True
    )
    version(
        "1.1.0", tag="v1.1.0", commit="a8118be48efa69f86e7e2251fcc03f55eee2ca8c", submodules=True
    )

    variant("cgal", default=True, description="Enable RDG generators via CGAL")
    variant(
        "sparsehash",
        default=False,
        description="Use Google Sparsehash instead of std::unordered_map",
    )
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
