# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Tdls(CMakePackage):
    """TDLS (Tiny Device-callable Linear Solvers) is a header-only C++20
    library of direct solvers for small dense linear systems, developed
    by CEA. The solvers are callable from host code as well as inside
    CUDA, HIP, SYCL, Kokkos, stdpar or OpenMP kernels, and are designed
    to be embedded in TFEL/MFront."""

    homepage = "https://trsxvz.github.io/TDLS/"
    git = "https://github.com/trsxvz/TDLS.git"

    maintainers("trsxvz")

    license("BSD-3-Clause", checked_by="trsxvz")

    version("main", branch="main")

    depends_on("cmake@3.21:", type="build")
    # A compiler is only needed to build and run the test suites and the
    # examples under --test. The compiler wrapper is not injected for a
    # test-typed language dependency (spack/spack#45573), so the compiler
    # of the spec is handed to CMake explicitly.
    depends_on("cxx", type="test")

    def cmake_args(self):
        args = [
            self.define("TDLS_BUILD_TESTS", self.run_tests),
            self.define("TDLS_BUILD_EXAMPLES", self.run_tests),
        ]
        if self.run_tests:
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["cxx"].package.cxx))
        return args

    def check(self):
        """Skip the target 'test', which does not build the test programs
        (they stay out of 'all'); the target 'check' builds and runs them."""
        with working_dir(self.build_directory):
            if self.generator == "Unix Makefiles":
                self._if_make_target_execute("check")
            elif self.generator == "Ninja":
                self._if_ninja_target_execute("check")
