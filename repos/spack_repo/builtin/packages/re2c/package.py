# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems import autotools, cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Re2c(AutotoolsPackage, CMakePackage):
    """re2c: a free and open-source lexer generator for C and C++"""

    homepage = "https://re2c.org/index.html"
    url = "https://github.com/skvadrik/re2c/releases/download/1.2.1/re2c-1.2.1.tar.xz"
    tags = ["windows"]

    license("Public-Domain")

    version("4.4", sha256="6b6b865924447ef992d5db4e52fb9307e5f65f26edd43efa91395da810f4280a")
    version("3.1", sha256="0ac299ad359e3f512b06a99397d025cfff81d3be34464ded0656f8a96676c029")
    version("3.0", sha256="b3babbbb1461e13fe22c630a40c43885efcfbbbb585830c6f4c0d791cf82ba0b")
    version("2.2", sha256="0fc45e4130a8a555d68e230d1795de0216dfe99096b61b28e67c86dfd7d86bda")
    version("2.1.1", sha256="036ee264fafd5423141ebd628890775aa9447a4c4068a6307385d7366fe711f8")
    version("2.1", sha256="8cba0d95c246c670de8f97f57def83a9c0f2113eaa6f7e4867a941f48f633540")

    build_system(conditional("cmake", when="@2.2:"), "autotools", default="autotools")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python@3.7:", when="@3.1:", type="build")

    with when("build_system=cmake"):
        depends_on("cmake@3.12:", type="build")


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def configure_args(self):
        return [
            "--disable-benchmarks",
            "--disable-debug",
            "--disable-dependency-tracking",
            "--disable-docs",
            "--disable-lexers",  # requires existing system re2c
            "--enable-libs",
            "--enable-golang",
        ]


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [
            self.define("RE2C_BUILD_LIBS", True),
            self.define("RE2C_REBUILD_DOCS", False),
            self.define("RE2C_REBUILD_LEXERS", False),
            self.define("RE2C_REBUILD_PARSERS", False),
            self.define("RE2C_BUILD_RE2RUST", False),
            self.define("RE2C_BUILD_RE2GO", False),
        ]
