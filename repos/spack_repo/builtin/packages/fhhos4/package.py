# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fhhos4(CMakePackage):
    """Algebraic multigrid (U-AMG) for the linear systems of hybrid discretizations (HHO, HDG...)
    of diffusion and convection-diffusion problems, symmetric or not: p-multigrid levels, then
    h-levels by aggregation, from the blocks of the uncondensed matrix. This package is the
    library of fhhos4, which only depends on Eigen; the research program of the repository is
    not built."""

    homepage = "https://github.com/pmatalon/fhhos4"
    url = "https://github.com/pmatalon/fhhos4/archive/refs/tags/v1.4.0.tar.gz"
    git = "https://github.com/pmatalon/fhhos4.git"

    maintainers("pmatalon")

    license("LGPL-3.0-or-later", checked_by="pmatalon")

    version("1.4.0", sha256="1134cc878c56c0e1e9ffe4e1bd87a0524b519cf4090c7bff9691d8026249ba88")

    variant("openmp", default=True, description="Parallel setup and solve with OpenMP")

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")
    # Eigen objects cross the interface of the library: the client code compiles with Eigen too.
    # The library checks that the client's Eigen has the same memory layout (3.4 and 5.x do).
    depends_on("eigen@3.4:")
    depends_on("llvm-openmp", when="+openmp %apple-clang")

    test_requires_compiler = True

    # A client code of the library, in the sources: find_package(fhhos4), then a solve
    test_client_dir = join_path("conda", "recipe", "test")

    def cmake_args(self):
        return [
            # The library alone: the program needs GMSH and CGAL
            self.define("ENABLE_PROGRAM", False),
            self.define_from_variant("ENABLE_OPENMP", "openmp"),
            # The target's flags come from Spack
            self.define("ENABLE_NATIVE_ARCH", False),
        ]

    @run_after("install")
    def cache_test_client(self):
        cache_extra_test_sources(self, [self.test_client_dir])

    def test_client(self):
        """build a client code with find_package(fhhos4), then solve a hybrid system"""
        source = join_path(self.test_suite.current_test_cache_dir, self.test_client_dir)
        # The build tool of the package: the test environment doesn't put it in the PATH
        if self.spec.satisfies("generator=ninja"):
            generator, build_tool = "Ninja", self.spec["ninja"].prefix.bin.ninja
        else:
            generator, build_tool = "Unix Makefiles", self.spec["gmake"].prefix.bin.make
        cmake = self.spec["cmake"].command
        cmake(
            "-S",
            source,
            "-B",
            "build-client",
            "-G",
            generator,
            self.define("CMAKE_MAKE_PROGRAM", build_tool),
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("CMAKE_CXX_COMPILER", self["cxx"].cxx),
            self.define("CMAKE_PREFIX_PATH", [self.prefix, self.spec["eigen"].prefix]),
            self.define("EXPECTED_VERSION", self.spec.version),
        )
        cmake("--build", "build-client")
        client = Executable(join_path("build-client", "fhhos4_client"))
        out = client(output=str.split, error=str.split)
        assert "iterations" in out
