# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AdaUrl(CMakePackage):
    """Ada is a fast URL parser written in C++20 that follows the WHATWG URL
    specification. It also implements the WHATWG URLPattern API."""

    homepage = "https://ada-url.com"
    url = "https://github.com/ada-url/ada/archive/refs/tags/v4.0.0.tar.gz"
    git = "https://github.com/ada-url/ada.git"

    maintainers("teaguesterling")

    license("Apache-2.0 OR MIT")

    version("4.0.0", sha256="6d6c7ef7dd2e329320d34eb2ab29ccdc879ee3935af9dfb894a6640e58dc381d")
    version("3.4.4", sha256="77bc5bbc383ed098cc60266ad6ee912de2431bb62d89248c0e17c4e712dcdaf9")

    variant("shared", default=True, description="Build a shared library")
    variant("pic", default=True, description="Build position-independent code")

    # project() enables C, though the library is C++
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.16:", type="build")

    # The project says that GCC 12 and Clang 15 are known to work
    conflicts("%gcc@:11", msg="ada-url needs C++20")
    conflicts("%clang@:14", msg="ada-url needs C++20")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            # Each of these includes cmake/CPM.cmake, which downloads during CMake
            self.define("ADA_TESTING", False),
            self.define("ADA_BENCHMARKS", False),
            self.define("ADA_TOOLS", False),
            self.define("ADA_USE_SIMDUTF", False),
            self.define("BUILD_TESTING", False),
        ]
