# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MpUnits(CMakePackage):
    """mp-units is a Modern C++ (C++20 and later) library providing the full
    spectrum of compile-time safety for domain-specific quantities and units, from
    dimensional analysis to quantity kind safety, built on the ISO 80000
    International System of Quantities (ISQ). It is a candidate for C++29
    standardization (P3045)"""

    homepage = "https://mpusz.github.io/mp-units"
    git = "https://github.com/mpusz/mp-units.git"

    license("MIT")

    version("master", branch="master")
    version("2.5.0", tag="v2.5.0", commit="27d2def9082ce00d7eb4f75695dbead4a748f23f")

    root_cmakelists_dir = "src"

    variant(
        "cxxstd",
        default="20",
        values=("20", "23", "26"),
        multi=False,
        description="C++ language standard",
    )

    variant(
        "cxx_modules", default=False, description="Build and install C++ module interface units"
    )

    variant(
        "freestanding", default=False, description="Configure for a freestanding C++ environment"
    )

    variant(
        "std_format",
        default=False,
        when="~freestanding",
        description="Use std::format instead of the fmt library",
    )

    variant(
        "no_crtp",
        default=False,
        when="~freestanding",
        description="Use C++23 explicit-object syntax instead of CRTP",
    )

    variant(
        "contracts",
        default="gsl-lite",
        values=(
            "none",
            conditional("gsl-lite", when="~freestanding"),
            conditional("ms-gsl", when="~freestanding"),
            conditional("std", when="@2.5.1: ~freestanding cxxstd=26"),
        ),
        multi=False,
        description="Contract checking implementation",
    )

    variant(
        "natural_units", default=True, description="Enable the experimental natural-units system"
    )

    depends_on("cxx", type="build")
    depends_on("cmake@4.2.1:4", type="build")

    depends_on("fmt@12.1.0:", when="~freestanding~std_format")
    depends_on("gsl-lite@1.0.1:", when="~freestanding contracts=gsl-lite")
    depends_on("ms-gsl@4.2.0:", when="~freestanding contracts=ms-gsl")

    requires(
        "%gcc@12:",
        "%clang@16:",
        "%apple-clang@15:",
        "%msvc@19.40:",
        policy="one_of",
        when="cxxstd=20",
        msg="C++20 requires GCC 12+, Clang 16+, Apple Clang 15+, or MSVC 19.40+",
    )

    requires(
        "%gcc@14:",
        "%clang@18:",
        "%apple-clang@17:",
        "%msvc@19.40:",
        policy="one_of",
        when="cxxstd=23",
        msg="C++23 requires GCC 14+, Clang 18+, Apple Clang 17+, or MSVC 19.40+",
    )

    requires(
        "%gcc@16:",
        when="cxxstd=26",
        msg="The supported C++26 configuration currently requires GCC 16+",
    )

    requires(
        "%clang@17:",
        when="+cxx_modules",
        msg="C++ modules are currently supported only with Clang 17+",
    )

    conflicts("%clang@19", msg="Clang 19 has a compiler bug that prevents building mp-units")

    conflicts("%apple-clang@17", msg="Apple Clang 17 has the same compiler bug as Clang 19")

    requires(
        "%gcc@13:",
        "%clang@17:",
        "%apple-clang@16:",
        "%msvc@19.40:",
        policy="one_of",
        when="+std_format cxxstd=20",
        msg="The selected compiler does not provide sufficient std::format support",
    )

    requires(
        "cxxstd=23",
        "cxxstd=26",
        policy="one_of",
        when="+no_crtp",
        msg="The no_crtp variant requires C++23 or newer",
    )

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_STANDARD", self.spec.variants["cxxstd"].value),
            self.define("CMAKE_CXX_STANDARD_REQUIRED", True),
            self.define("CMAKE_CXX_EXTENSIONS", False),
            self.define("MP_UNITS_BUILD_INSTALL", True),
            self.define_from_variant("MP_UNITS_BUILD_CXX_MODULES", "cxx_modules"),
            self.define_from_variant("MP_UNITS_API_NATURAL_UNITS", "natural_units"),
            self.define_from_variant("CMAKE_CXX_SCAN_FOR_MODULES", "cxx_modules"),
            self.define_from_variant("MP_UNITS_API_FREESTANDING", "freestanding"),
            self.define("MP_UNITS_API_CONTRACTS", self.spec.variants["contracts"].value.upper()),
        ]

        if self.spec.satisfies("+freestanding"):
            args.extend([self.define("CMAKE_TRY_COMPILE_TARGET_TYPE", "STATIC_LIBRARY")])
        else:
            args.extend(
                [
                    self.define_from_variant("MP_UNITS_API_STD_FORMAT", "std_format"),
                    self.define_from_variant("MP_UNITS_API_NO_CRTP", "no_crtp"),
                ]
            )
        return args
