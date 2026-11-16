# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Croaring(CMakePackage):
    """CRoaring is a C and C++ library for Roaring bitmaps, which are compressed
    bitsets."""

    homepage = "https://roaringbitmap.org"
    url = "https://github.com/RoaringBitmap/CRoaring/archive/refs/tags/v4.7.1.tar.gz"
    git = "https://github.com/RoaringBitmap/CRoaring.git"

    maintainers("teaguesterling")

    license("Apache-2.0 OR MIT")

    version("5.5.5", sha256="f78a93b8cf373fe4a3d31075cf2b3dc21dcfd7bbbc17674df35071ec8e461aef")
    version("4.7.1", sha256="56657dab885c3dd1d3ff3b4a795a5ae05cb0a70c0f53d0093b0c281af30aa8ac")

    variant("shared", default=True, description="Build a shared library")
    variant("pic", default=True, description="Build position-independent code")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("ROARING_BUILD_STATIC", self.spec.satisfies("~shared")),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("ENABLE_ROARING_TESTS", False),
            # CPM downloads its own script and packages during CMake
            self.define("ROARING_USE_CPM", False),
        ]
