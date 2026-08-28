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

    def cmake_args(self):
        return [
            self.define("TDLS_BUILD_TESTS", False),
            self.define("TDLS_BUILD_EXAMPLES", False),
        ]
