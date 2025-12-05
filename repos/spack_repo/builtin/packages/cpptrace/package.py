# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Cpptrace(CMakePackage):
    """Simple, portable, and self-contained stacktrace library for C++11 and newer."""

    homepage = "https://github.com/jeremy-rifkin/cpptrace"
    url = "https://github.com/jeremy-rifkin/cpptrace/archive/refs/tags/v1.0.0.tar.gz"

    maintainers("RMeli")

    license("MIT", checked_by="RMeli")

    version("1.0.0", sha256="0e11aebb6b9b98ce9134a58532b63982365aadc76533a4fbb7f6fb6edb32de2e")

    variant("shared", default=False, description="Build shared libraries")
    variant("external_libdwarf", default=False, description="Use external libdwarf")
    variant("external_zstd", default=False, description="Use external zstd")

    generator("ninja")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("libdwarf", when="+external_libdwarf")
    depends_on("zstd", when="+external_zstd")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CPPTRACE_USE_EXTERNAL_LIBDWARF", "external_libdwarf"),
            self.define_from_variant("CPPTRACE_USE_EXTERNAL_ZSTD", "external_zstd"),
        ]
        return args
