# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mdspan(CMakePackage):
    """Extension of std::span to enable multidimensional arrays"""

    homepage = "https://github.com/kokkos/mdspan/tree/stable"
    url = "https://github.com/kokkos/mdspan/archive/5.3.0.tar.gz"
    git = "https://github.com/kokkos/mdspan.git"

    maintainers("tpadioleau", "nmm0")

    version("develop", branch="develop")
    version("stable", branch="stable")
    version("5.3.0", sha256="ba71517536c646b9160c10e7d83e6aad5663e3289a1f619deb6a3760f252ffae")
    version(
        "0.6.0",
        sha256="d6b7b9d4f472106df1d28729bd8383a8a7ea7938adf9f82d3be9c151344830d9",
        url="https://github.com/kokkos/mdspan/archive/refs/tags/mdspan-0.6.0.zip",
    )

    # TODO: Update supported C++ standards when needed
    # Note that mdspan currently has a "detect" mode, not sure we want to replicate that here
    with default_args(multi=False, description="C++ standard"):
        variant("cxxstd", default="17", values=("14", "17", "20"), when="@0.6.0")
        variant("cxxstd", default="20", values=("14", "17", "20", "23", "26"), when="@5.3:")
    variant(
        "stdheaders",
        default=False,
        when="@5.3:",
        description="Whether to install headers to emulate standard library headers and namespace",
    )

    depends_on("cxx", type="build")

    depends_on("googletest@1.14:1", type="test")

    def cmake_args(self):
        args = [
            self.define("MDSPAN_ENABLE_BENCHMARKS", False),
            self.define("MDSPAN_ENABLE_EXAMPLES", False),
            self.define("MDSPAN_ENABLE_TESTS", self.run_tests),
            self.define("MDSPAN_GENERATE_STD_NAMESPACE_TARGETS", False),
            self.define("MDSPAN_USE_SYSTEM_GTEST", self.run_tests),
            self.define_from_variant("MDSPAN_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("MDSPAN_INSTALL_STDMODE_HEADERS", "stdheaders"),
        ]

        return args
