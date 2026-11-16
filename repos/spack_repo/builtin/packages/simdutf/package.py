# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Simdutf(CMakePackage):
    """simdutf validates and transcodes Unicode (UTF-8, UTF-16, UTF-32, Latin-1) and
    base64 with SIMD instructions."""

    homepage = "https://simdutf.github.io/simdutf/"
    url = "https://github.com/simdutf/simdutf/archive/refs/tags/v9.3.3.tar.gz"
    git = "https://github.com/simdutf/simdutf.git"

    maintainers("teaguesterling")

    license("Apache-2.0 OR MIT")

    version("9.3.3", sha256="441e374e8629bd8469f6d5cde9f0fa17ef3ad158aeb077791606d8aa73b565ef")
    version("6.1.1", sha256="34f2e28ad9bbc1cd5909abe20b819e877200d48eb86d5839e042011909cbdf7a")

    variant("shared", default=True, description="Build a shared library")
    variant("pic", default=True, description="Build position-independent code")

    depends_on("c", type="build", when="@9:")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")
    depends_on("cmake@3.18:", type="build", when="@9:")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("SIMDUTF_TESTS", False),
            self.define("SIMDUTF_BENCHMARKS", False),
            self.define("SIMDUTF_TOOLS", False),
            self.define("SIMDUTF_FUZZERS", False),
        ]
