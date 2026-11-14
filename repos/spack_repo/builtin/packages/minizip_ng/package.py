# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MinizipNg(CMakePackage):
    """minizip-ng is a zip manipulation library written in C. It is a fork of the minizip
    contribution of zlib, with a different API."""

    homepage = "https://github.com/zlib-ng/minizip-ng"
    url = "https://github.com/zlib-ng/minizip-ng/archive/refs/tags/4.2.2.tar.gz"
    git = "https://github.com/zlib-ng/minizip-ng.git"

    maintainers("teaguesterling")

    license("Zlib")

    version("4.2.2", sha256="71af7b9799856d8b03619df3949e9c1be9703f8de0795af71399ba283cb27aac")
    version("4.0.7", sha256="a87f1f734f97095fe1ef0018217c149d53d0f78438bcb77af38adc21dff2dfbc")

    variant("shared", default=True, description="Build a shared library")
    variant("pic", default=True, description="Build position-independent code")

    depends_on("c", type="build")
    # 3.24 for ZLIB_USE_STATIC_LIBS
    depends_on("cmake@3.24:", type="build")
    depends_on("zlib-api")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            # The names that other package managers use: minizip-ng, MINIZIP::minizip-ng
            self.define("MZ_LIB_SUFFIX", "-ng"),
            # These download zlib-ng, bzip2, xz, zstd or 7-Zip during CMake
            self.define("MZ_FETCH_LIBS", False),
            self.define("MZ_FORCE_FETCH_LIBS", False),
            self.define("MZ_PPMD", False),
            # Only zlib compression, as vcpkg minizip-ng[zlib]. These other options find
            # libraries on the host.
            self.define("MZ_ZLIB", True),
            # zlib-api, and not a native zlib-ng that the host has: ZLIBNG for 4.0, and
            # MZ_ZLIB_FLAVOR for 4.1 and later
            self.define("CMAKE_DISABLE_FIND_PACKAGE_ZLIBNG", True),
            self.define("MZ_ZLIB_FLAVOR", "zlib"),
            self.define("MZ_BZIP2", False),
            self.define("MZ_LZMA", False),
            self.define("MZ_ZSTD", False),
            self.define("MZ_LIBCOMP", False),
            self.define("MZ_PKCRYPT", False),
            self.define("MZ_WZAES", False),
            self.define("MZ_OPENSSL", False),
            self.define("MZ_LIBBSD", False),
            self.define("MZ_ICONV", False),
            self.define("MZ_BUILD_TESTS", False),
            self.define("MZ_BUILD_UNIT_TESTS", False),
            self.define("MZ_BUILD_FUZZ_TESTS", False),
        ]
        # The CMake package of minizip-ng records the path of the zlib library that it found.
        # A static library must record the static zlib, or its users link the shared one.
        if self.spec.satisfies("~shared"):
            args.append(self.define("ZLIB_USE_STATIC_LIBS", True))
        return args
