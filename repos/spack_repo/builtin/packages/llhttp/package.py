# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Llhttp(CMakePackage):
    """Fast HTTP message parser based on llparse."""

    homepage = "https://llhttp.org/"
    url = "https://github.com/nodejs/llhttp/archive/refs/tags/release/v9.3.1.tar.gz"
    git = "https://github.com/nodejs/llhttp.git"

    license("MIT")

    version("9.3.1", sha256="c14a93f287d3dbd6580d08af968294f8bcc61e1e1e3c34301549d00f3cf09365")

    variant("shared", default=True, description="Build shared library")
    variant("static", default=True, description="Build static library")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.25:", type="build")

    conflicts("~shared~static", msg="llhttp requires at least one library variant")

    def cmake_args(self):
        return [
            self.define_from_variant("LLHTTP_BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("LLHTTP_BUILD_STATIC_LIBS", "static"),
        ]
