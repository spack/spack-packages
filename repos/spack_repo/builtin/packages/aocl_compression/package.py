# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefileBuilder, MakefilePackage

from spack.package import *


class AoclCompression(CMakePackage, MakefilePackage):
    """
    AOCL-Compression is a software framework of various lossless compression
    and decompression methods tuned and optimized for AMD Zen based CPUs.
    This framework offers a single set of unified APIs for all the supported
    compression and decompression methods which facilitate the applications
    to easily integrate and use them.
    AOCL-Compression supports lz4, zlib/deflate, lzma, zstd, bzip2, snappy,
    and lz4hc based compression and decompression methods along with their
    native APIs.
    The library offers openMP based multi-threaded implementation of lz4, zlib,
    zstd and snappy compression methods. It supports the dynamic dispatcher
    feature that executes the most optimal function variant implemented using
    Function Multi-versioning thereby offering a single optimized library
    portable across different x86 CPU architectures.
    AOCL-Compression framework is developed in C for UNIX® and Windows® based
    systems. A test suite is provided for the validation and performance
    benchmarking of the supported compression and decompression methods.
    This suite also supports the benchmarking of IPP compression methods, such
    as, lz4, lz4hc, zlib and bzip2. The library build framework offers CTest
    based testing of the test cases implemented using GTest and the library
    test suite.

    LICENSING INFORMATION: By downloading, installing and using this software,
    you agree to the terms and conditions of the AMD AOCL-Compression license
    agreement.  You may obtain a copy of this license agreement from
    https://www.amd.com/content/dam/amd/en/documents/developer/version-4-2-eulas/compression-elua-4-2.pdf
    """

    _name = "aocl-compression"
    homepage = "https://www.amd.com/en/developer/aocl/compression.html"
    git = "https://github.com/amd/aocl-compression.git"
    url = "https://github.com/amd/aocl-compression/archive/4.2.tar.gz"

    maintainers("amd-toolchain-support")

    version("5.3", sha256="fdc58c1f42933290b8c127102c28d8a8f93102eab251046d8ed01a69a0abdbcb")
    version("5.2", sha256="93a4eddd0a70e6d8701ecf2c55a06ab341d987ccd2e87c50a5c7e1efb37e033e")
    version("5.1", sha256="9462c6898350d66a5d9ce0236c432c94b4c9393b638ddf6511628b784eb02720")
    version("5.0", sha256="50bfb2c4a4738b96ed6d45627062b17bb9d0e1787c7d83ead2841da520327fa4")
    version("4.2", sha256="a18b3e7f64a8105c1500dda7b4c343e974b5e26bfe3dd838a1c1acf82a969c6f")

    build_system("cmake", conditional("makefile", when="@5.3:"), default="cmake")

    variant("shared", default=True, description="Build shared library")
    variant("zlib", default=True, description="Build zlib library")
    variant("bzip2", default=True, description="Build bzip2 library")
    variant("snappy", default=True, description="Build snappy library")
    variant("zstd", default=True, description="Build zstd library")
    variant("lzma", default=True, description="Build lzma library")
    variant("lz4", default=True, description="Build lz4 library")
    variant("lz4hc", default=True, description="Build lz4hc library")
    variant(
        "openmp",
        default=False,
        description="openmp based multi-threaded compression and decompression",
    )
    variant(
        "decompress_fast",
        default="OFF",
        values=("OFF", "1", "2"),
        description="Enable fast decompression modes",
        multi=False,
    )
    variant("enable_fast_math", default=False, description="Enable fast-math optimizations")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.22:", when="build_system=cmake @:5.0", type="build")
    depends_on("cmake@3.26:", when="build_system=cmake @5.1:5.2", type="build")


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        """Runs ``cmake`` in the build directory"""
        spec = self.spec
        args = []

        args = [
            self.define_from_variant("AOCL_ENABLE_THREADS", "openmp"),
            self.define_from_variant("ENABLE_FAST_MATH", "enable_fast_math"),
            "-DLZ4_FRAME_FORMAT_SUPPORT=ON",
            "-DAOCL_LZ4HC_DISABLE_PATTERN_ANALYSIS=ON",
        ]
        if spec.satisfies("~shared"):
            args.append("-DBUILD_STATIC_LIBS=ON")
        if spec.satisfies("~zlib"):
            args.append("-DAOCL_EXCLUDE_ZLIB=ON")
        if spec.satisfies("~bzip2"):
            args.append("-DAOCL_EXCLUDE_BZIP2=ON")
        if spec.satisfies("~snappy"):
            args.append("-DAOCL_EXCLUDE_SNAPPY=ON")
        if spec.satisfies("~zstd"):
            args.append("-DAOCL_EXCLUDE_ZSTD=ON")
        if spec.satisfies("~lzma"):
            args.append("-DAOCL_EXCLUDE_LZMA=ON")
        if spec.satisfies("~lz4"):
            args.append("-DAOCL_EXCLUDE_LZ4=ON")
        if spec.satisfies("~lz4hc"):
            args.append("-DAOCL_EXCLUDE_LZ4HC=ON")

        args.append("-DAOCL_DECOMPRESS_FAST={}".format(spec.variants["decompress_fast"].value))
        return args


class MakefileBuilder(MakefileBuilder):
    def _make_options(self, spec):
        """Shared Make variable list used by both build and install phases."""
        options = [
            "LZ4_FRAME_FORMAT_SUPPORT=1",
            "AOCL_LZ4HC_DISABLE_PATTERN_ANALYSIS=1",
            "AOCL_ENABLE_THREADS={0}".format("1" if spec.satisfies("+openmp") else "0"),
            "ENABLE_FAST_MATH={0}".format("1" if spec.satisfies("+enable_fast_math") else "0"),
        ]
        if spec.satisfies("~shared"):
            options.append("BUILD_STATIC_LIBS=1")
        if spec.satisfies("~zlib"):
            options.append("AOCL_EXCLUDE_ZLIB=1")
        if spec.satisfies("~bzip2"):
            options.append("AOCL_EXCLUDE_BZIP2=1")
        if spec.satisfies("~snappy"):
            options.append("AOCL_EXCLUDE_SNAPPY=1")
        if spec.satisfies("~zstd"):
            options.append("AOCL_EXCLUDE_ZSTD=1")
        if spec.satisfies("~lzma"):
            options.append("AOCL_EXCLUDE_LZMA=1")
        if spec.satisfies("~lz4"):
            options.append("AOCL_EXCLUDE_LZ4=1")
        if spec.satisfies("~lz4hc"):
            options.append("AOCL_EXCLUDE_LZ4HC=1")
        decompress_fast = spec.variants["decompress_fast"].value
        if decompress_fast != "OFF":
            options.append("AOCL_DECOMPRESS_FAST={0}".format(decompress_fast))
        return options

    def build(self, pkg, spec, prefix):
        make(*self._make_options(spec))

    def install(self, pkg, spec, prefix):
        make("install", "PREFIX={0}".format(prefix), *self._make_options(spec))
