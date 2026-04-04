# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Llhttp(CMakePackage):
    """Fast HTTP message parser based on llparse."""

    homepage = "https://llhttp.org/"
    url = "https://github.com/nodejs/llhttp/archive/refs/tags/release/v9.2.1.tar.gz"
    git = "https://github.com/nodejs/llhttp.git"

    license("MIT")

    version("9.2.1", sha256="3c163891446e529604b590f9ad097b2e98b5ef7e4d3ddcf1cf98b62ca668f23e")

    variant("shared", default=True, description="Build shared library")
    variant("static", default=True, description="Build static library")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.5.1:", type="build")

    conflicts("~shared~static", msg="llhttp requires at least one library variant")

    def cmake_args(self):
        return [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("BUILD_STATIC_LIBS", "static"),
        ]
