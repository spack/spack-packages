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
    url = "https://github.com/pmatalon/fhhos4/archive/refs/tags/v1.5.0.tar.gz"
    git = "https://github.com/pmatalon/fhhos4.git"

    maintainers("pmatalon")

    license("LGPL-3.0-or-later", checked_by="pmatalon")

    version("1.5.0", sha256="863ef51fb03c27faa60e0382a2ad0077a468ff7a89bb2d1aab3cf20eab64eeeb")
    version("1.4.0", sha256="1134cc878c56c0e1e9ffe4e1bd87a0524b519cf4090c7bff9691d8026249ba88")

    variant("openmp", default=True, description="Parallel setup and solve with OpenMP")
    variant(
        "int64",
        default=False,
        when="@1.5:",
        description="64-bit indices (int64_t) in the sparse matrices of the interface",
    )
    variant(
        "mpi",
        default=True,
        when="@1.5:",
        description="Solve on several processes (MPI), the coarsest level with MUMPS",
    )
    # MUMPS: always with MPI, which solves the coarsest level with it; optional without
    variant(
        "mumps",
        default=True,
        when="@1.5: +mpi",
        description="MUMPS as coarse solver, also on one process (CoarseSolver::MUMPS)",
    )
    variant(
        "mumps",
        default=False,
        when="@1.5: ~mpi",
        description="MUMPS as coarse solver, also on one process (CoarseSolver::MUMPS)",
    )
    conflicts("~mumps", when="+mpi", msg="MPI solves the coarsest level with MUMPS")

    depends_on("cxx", type="build")
    depends_on("cmake@3.20:", type="build")
    # The public header takes Eigen matrices: the client code compiles with Eigen too
    # (3.4 or 5.x, not necessarily the library's).
    depends_on("eigen@3.4:", type=("build", "link"))
    depends_on("llvm-openmp", type=("build", "link"), when="+openmp %apple-clang")
    # The public header includes mpi.h: the client code compiles with MPI too
    depends_on("mpi", type=("build", "link"), when="+mpi")
    depends_on("mumps+double+mpi", type=("build", "link"), when="+mpi")
    depends_on("mumps+double~mpi", type=("build", "link"), when="+mumps~mpi")

    test_requires_compiler = True

    # A client code of the library, in the sources: find_package(fhhos4), then a solve
    test_client_dir = join_path("conda", "recipe", "test")

    def cmake_args(self):
        return [
            # The library alone: the program needs GMSH and CGAL
            self.define("ENABLE_PROGRAM", False),
            self.define_from_variant("ENABLE_OPENMP", "openmp"),
            self.define_from_variant("ENABLE_64BIT_INDEX", "int64"),
            self.define_from_variant("ENABLE_MPI", "mpi"),
            self.define_from_variant("ENABLE_MUMPS", "mumps"),
            # Its tests with MPI need GoogleTest; the stand-alone test checks the installation
            self.define("ENABLE_TESTS", False),
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
        prefix_path = [self.prefix, self.spec["eigen"].prefix]
        if self.spec.satisfies("+mpi"):
            # find_package(fhhos4) looks for MPI
            prefix_path.append(self.spec["mpi"].prefix)
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
            self.define("CMAKE_PREFIX_PATH", prefix_path),
            self.define("EXPECTED_VERSION", self.spec.version),
        )
        cmake("--build", "build-client")
        client = Executable(join_path("build-client", "fhhos4_client"))
        out = client(output=str.split, error=str.split)
        assert "iterations" in out
