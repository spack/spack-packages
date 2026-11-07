# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Miniz(CMakePackage):
    """miniz is a lossless data compression library in C that implements the zlib
    (RFC 1950) and Deflate (RFC 1951) formats, and reads and writes ZIP archives."""

    homepage = "https://github.com/richgel999/miniz"
    url = "https://github.com/richgel999/miniz/archive/refs/tags/3.1.2.tar.gz"
    git = "https://github.com/richgel999/miniz.git"

    maintainers("teaguesterling")

    license("MIT")

    version("3.1.2", sha256="98468f8924934b723276680f85238b6c78bf1f8b49b4459cc9b7214a20e2e9fb")
    version("3.1.1", sha256="8bb29c7bd6f22356e5583e794bed4a0b3e6dfcbcadb49974fc9270ccca1e5557")

    variant("shared", default=True, description="Build a shared library")
    variant("pic", default=True, description="Build position-independent code")

    depends_on("c", type="build")
    depends_on("cmake@3.5:", type="build")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("BUILD_EXAMPLES", False),
            self.define("BUILD_FUZZERS", False),
            self.define("BUILD_TESTS", False),
            self.define("INSTALL_PROJECT", True),
        ]
