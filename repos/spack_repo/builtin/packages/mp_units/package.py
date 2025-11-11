# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MpUnits(CMakePackage):
    """mp-units: a modern C++ units library (from mpusz/mp-units)."""

    homepage = "https://mpusz.github.io/mp-units"
    url = "https://github.com/mpusz/mp-units/archive/refs/tags/v2.4.0.tar.gz"
    git = "https://github.com/mpusz/mp-units.git"

    license("MIT", checked_by="maiterth")

    version("master", branch="master")
    version("2.4.0", sha256="777e53ba8da891161e90a93b90b92fa66951d49aaae1b0203ddf934532bbeb56")
    version("2.3.0", sha256="ce2f167ff788ae769e73ea7676f15302827cd37908da3928dcae048f916898d6")
    version("2.2.1", sha256="ce5edb27fad9c54b388040341a03d7f2462d61dcedad85b4c983c0e648a91bac")
    version("2.2.0", sha256="91afd01464712542b6ea48a017500e9281aaaa85066b9bbec383ca9bec595c9d")
    version("2.1.1", sha256="881070fd9a15a8954a4e38d991e398dc9638907bbc13961a530519596c9783f9")
    version("2.1.0", sha256="a42057492f5a8e80442cf13602b97bb48b9c3a408bc91bdb60d86aadc84c95cc")
    version("2.0.0", sha256="c04cda9fdaeca3ae42886552658e8bde3b608a24a4a921a621a5db41ec416e0e")
    version("0.8.0", sha256="4081c75e5f2763bb95a6514d952f187519591e594b8fb93ddc9943741827e8c9")
    version("0.7.0", sha256="416d7ff19a2f371e41a2efd9e44b8ad8b8d59fa561f2cb2aaa45a8d7e1c16105")
    version("0.6.0", sha256="c9d8a98f7845024581a69d425d2de0e786f0c70d7a72358279ea67e1cf377529")

    # build tools / deps
    depends_on("cmake@3.25:", type="build")
    depends_on("ninja", type="build")
    # keep generator to hint Spack to prefer Ninja (only works if the selected cmake supports it)
    generator = "Ninja"

    depends_on("cxx", type="build")
    cxxstds = ["20", "23", "26"]
    variant("cxxstd", default="23", values=cxxstds, multi=False, description="C++ standard")

    requires(
        "%clang@:17,19:",
        when="%cxx=clang",
        msg="builds only with a GCC or Clang that support C++ 20",
    )

    depends_on("fmt", when="std_format=OFF")
    depends_on("fmt", when="std_format=AUTO")
    depends_on("gsl-lite", when="contracts=GSL-LITE")
    depends_on("catch2")

    # package-provided variants (keep only those that change cmake options)
    variant(
        "cxx_modules",
        default="ON",
        values=("ON", "OFF"),
        when="@2.2.0:",
        description="Adds C++ modules to the default targets.",
    )
    variant(
        "build_install",
        default="ON",
        values=("ON", "OFF"),
        when="@2.5.0:",
        description=(
            "Creates an installable target. Users may want to turn this off for example when "
            "consuming the library via CMake's add_subdirectory or similar mechanisms."
        ),
    )
    variant(
        "std_format",
        default="AUTO",
        values=("AUTO", "ON", "OFF"),
        when="@2.2.0:",
        description=(
            "Enables the usage of std::format and associated facilities for text formatting. If "
            "it is not supported, then the {fmt} library is used instead."
        ),
    )
    variant(
        "no_crtp",
        default="AUTO",
        values=("AUTO", "ON", "OFF"),
        when="@2.2.0:",
        description=(
            "Removes the need for the usage of the CRTP idiom in the quantity_spec definitions."
        ),
    )
    variant(
        "contracts",
        default="GSL-LITE",
        values=("NONE", "GSL-LITE", "MS-GSL"),
        when="@2.2.0:",
        description="Enables checking of preconditions and additional asserts in the code.",
    )
    variant(
        "freestanding",
        default="OFF",
        values=("ON", "OFF"),
        when="@2.2.0:",
        description=(
            "Configures the library in the freestanding mode. When enabled, the library's source "
            "code should build with the compiler's -ffreestanding compilation option without any "
            "issues."
        ),
    )
    variant(
        "natural_units",
        default="ON",
        values=("ON", "OFF"),
        when="@2.5.0:",
        description="Enables experimental natural units systems support.",
    )

    patch("format_header.patch", when="@2.2.0:2.4.0 std_format=ON")
    patch("format_header.patch", when="@2.2.0:2.4.0 std_format=AUTO")

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@2.2.0:"):
            args.append(self.define_from_variant("MP_UNITS_BUILD_CXX_MODULES", "cxx_modules"))
            args.append(self.define_from_variant("MP_UNITS_API_STD_FORMAT", "std_format"))
            args.append(self.define_from_variant("MP_UNITS_API_NO_CRTP", "no_crtp"))
            args.append(self.define_from_variant("MP_UNITS_API_CONTRACTS", "contracts"))
            args.append(self.define_from_variant("MP_UNITS_API_FREESTANDING", "freestanding"))

        # MP_UNITS_API_NATURAL_UNITS and MP_UNITS_BUILD_INSTALL were added later — guard them.
        if self.spec.satisfies("@2.5.0:"):
            args.append(self.define_from_variant("MP_UNITS_API_NATURAL_UNITS", "natural_units"))
            args.append(self.define_from_variant("MP_UNITS_BUILD_INSTALL", "build_install"))

        return args
