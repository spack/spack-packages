# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Zig(CMakePackage):
    """A general-purpose programming language and toolchain for maintaining
    robust, optimal, and reusable software.
    """

    homepage = "https://ziglang.org/"
    git = "https://codeberg.org/ziglang/zig.git"

    maintainers("alalazo")

    license("MIT")

    version("0.16.0", tag="0.16.0", commit="24fdd5b7a4c1c8b5deb5b56756b9dbc8e08c86a8")
    version("0.15.2", tag="0.15.2", commit="e4cbd752c8c05f131051f8c873cff7823177d7d3")

    with default_args(deprecated=True):
        version("0.15.1", tag="0.15.1", commit="3db960767d12b6214bcf43f1966a037c7a586a12")
        version("0.14.1", tag="0.14.1", commit="d03a147ea0a590ca711b3db07106effc559b0fc6")
        version("0.14.0", tag="0.14.0", commit="5ad91a646a753cc3eecd8751e61cf458dadd9ac4")
        version("0.13.0", tag="0.13.0", commit="cf90dfd3098bef5b3c22d5ab026173b3c357f2dd")
        version("0.12.0", tag="0.12.0", commit="a685ab1499d6560c523f0dbce2890dc140671e43")
        version("0.11.0", tag="0.11.0", commit="67709b638224ac03820226c6744d8b6ead59184c")
        version("0.10.1", tag="0.10.1", commit="b57081f039bd3f8f82210e8896e336e3c3a6869b")

    variant(
        "build_type",
        values=("Release", "RelWithDebInfo", "MinSizeRel"),
        default="Release",
        description="CMake build type",
    )

    # See https://codeberg.org/ziglang/zig#building-from-source
    depends_on("cmake@3.5:", type="build")
    depends_on("cmake@3.15:", type="build", when="@0.13:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("llvm@21", when="@0.16")
    depends_on("llvm@20", when="@0.15")
    depends_on("llvm@19", when="@0.14")
    depends_on("llvm@18", when="@0.13")
    depends_on("llvm@17", when="@0.12")
    depends_on("llvm@16", when="@0.11")
    depends_on("llvm@15", when="@0.10")
    depends_on("llvm targets=all")

    depends_on("git", type="build")
    depends_on("ccache")

    provides("ziglang")

    def cmake_args(self):
        return [
            self.define("ZIG_USE_CCACHE", True),
            self.define("ZIG_STATIC_LLVM", True),
            self.define("ZIG_STATIC_ZLIB", True),
            self.define("ZIG_STATIC_ZSTD", True),
        ]
