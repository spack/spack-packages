# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mdspan(CMakePackage):
    """Extension of std::span to enable multidimensional arrays"""

    homepage = "https://github.com/kokkos/mdspan/tree/stable"
    url = "https://github.com/kokkos/mdspan/archive/refs/tags/mdspan-0.6.0.zip"
    git = "https://github.com/kokkos/mdspan.git"

    maintainers("tpadioleau", "nmm0")

    version("stable", branch="stable")
    version("0.6.0", sha256="d6b7b9d4f472106df1d28729bd8383a8a7ea7938adf9f82d3be9c151344830d9")
    version("kokkos-develop", commit="884f17a24301955d47cbb22318f06b8d8bee7ca3")
    version("kokkos-5.2.1", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.2.0", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.1.1", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.1.0", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.0.2", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.0.1", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-5.0.0", commit="537053f83150f1b6f7528c1d961866d8628abc2e")
    version("kokkos-4.7.04", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-4.7.03", commit="5d4eb209c77f4744980c0b0c2af44636cc81b08b")
    version("kokkos-4.7.02", commit="537053f83150f1b6f7528c1d961866d8628abc2e")
    version("kokkos-4.7.01", commit="0e4eba59ad53451784b3839bdf98b25fa2d64931")
    version("kokkos-4.7.00", commit="0e4eba59ad53451784b3839bdf98b25fa2d64931")

    variant("examples", default=True, description="Enable examples")
    variant("tests", default=False, description="Enable tests")
    variant("benchmarks", default=False, description="Enable benchmarks")
    variant(
        "cxxstd", default="17", values=["14", "17", "20"], multi=False, description="C++ standard"
    )
    variant(
        "stdheaders",
        default=False,
        when="@stable",
        description="Whether to install headers to emulate standard library headers and namespace",
    )

    depends_on("cxx", type="build")

    depends_on("benchmark", when="+benchmarks")
    depends_on("googletest@1.14:1", when="+tests")

    def cmake_args(self):
        args = [
            self.define_from_variant("MDSPAN_ENABLE_TESTS", "tests"),
            self.define_from_variant("MDSPAN_USE_SYSTEM_GTEST", "tests"),
            self.define_from_variant("MDSPAN_ENABLE_BENCHMARKS", "benchmarks"),
            self.define_from_variant("MDSPAN_ENABLE_EXAMPLES", "examples"),
            self.define_from_variant("MDSPAN_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("MDSPAN_INSTALL_STDMODE_HEADERS", "stdheaders"),
        ]

        return args
