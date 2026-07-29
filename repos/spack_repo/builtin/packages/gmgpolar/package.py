# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gmgpolar(CMakePackage):
    """GMGPolar is a performant geometric multigrid solver using implicit extrapolation
    to raise the convergence order."""

    homepage = "https://github.com/SciCompMod/GMGPolar"
    git = "https://github.com/SciCompMod/GMGPolar.git"
    url = "https://github.com/SciCompMod/GMGPolar/archive/refs/tags/v2.3.1.tar.gz"

    maintainers("mknaranja", "tpadioleau")

    license("Apache-2.0", checked_by="tpadioleau")

    version("main", branch="main", no_cache=True)
    version("2.3.1", sha256="c8e3ec83ec04bbe2c1e7d8f27e7be18a816ace04c3b3bae78c616f4d545c3382")

    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")

    depends_on("kokkos@4.4.1:")
    depends_on("kokkos@:5")

    depends_on("googletest@1.17:", type="test")
    depends_on("googletest@:1", type="test")

    # Fixes missing headers in 2.3.1
    patch(
        "https://github.com/SciCompMod/GMGPolar/commit/9356b29a80848c9c88eaa748eb6ce4d8dc67028f.patch?full_index=1",
        sha256="6f5c48536babcaead6c65866536ec9471f50cfef68eb13d8990628a4d7e05e00",
        when="@2.3.1",
    )
    # Fixes openmp dependency search in GMGPolarConfig.cmake in 2.3.1
    patch(
        "https://github.com/SciCompMod/GMGPolar/commit/7ea865536a4e0adc783a3dca3057a39fc30b0800.patch?full_index=1",
        sha256="863a0e92b9567dd950fff400186f3f42a22ec89e29f480860a1fd1dc9a4630f6",
        when="@2.3.1",
    )

    def cmake_args(self):
        args = [
            self.define("GMGPOLAR_BUILD_TESTS", self.run_tests),
            self.define("GMGPOLAR_ENABLE_COVERAGE", False),
            self.define("GMGPOLAR_USE_LIKWID", False),
            self.define("GMGPOLAR_USE_MUMPS", False),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
