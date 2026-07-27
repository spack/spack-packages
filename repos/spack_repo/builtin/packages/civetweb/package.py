# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Civetweb(CMakePackage):
    """CivetWeb is an easy to use, powerful, C (C/C++) embeddable
    web server with optional CGI, SSL and Lua support."""

    homepage = "https://github.com/civetweb/civetweb"
    url = "https://github.com/civetweb/civetweb/archive/refs/tags/v1.16.tar.gz"
    git = "https://github.com/civetweb/civetweb.git"
    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("1.16-213-g5864b55a", commit="5864b55a94f4b5238155cbf2baec707f0fa2ba6d")
    version("1.16", sha256="f0e471c1bf4e7804a6cfb41ea9d13e7d623b2bcc7bc1e2a4dd54951a24d60285")

    variant("shared", default=False, description="Build shared libraries instead of static ones")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("lua")
    depends_on("openssl")
    depends_on("zlib-api")

    def cmake_args(self):
        args = [
            self.define("CIVETWEB_BUILD_TESTING", self.run_tests),
            self.define("CIVETWEB_ENABLE_SERVER_EXECUTABLE", True),
            self.define("CIVETWEB_ENABLE_CXX", True),
            self.define("CIVETWEB_ENABLE_HTTP2", True),
            self.define("CIVETWEB_ENABLE_IPV6", True),
            self.define("CIVETWEB_ENABLE_WEBSOCKETS", True),
            self.define("CIVETWEB_ENABLE_X_DOM_SOCKET", True),
            self.define("CIVETWEB_ENABLE_LUA", False),
            self.define("CIVETWEB_ENABLE_ZLIB", True),
            self.define("CIVETWEB_ENABLE_SSL", True),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]
        args.append(
            self.define("CIVETWEB_SSL_OPENSSL_API_1_0", self.spec.satisfies("^openssl@1.0"))
        )
        args.append(
            self.define("CIVETWEB_SSL_OPENSSL_API_1_1", self.spec.satisfies("^openssl@1.1"))
        )
        args.append(
            self.define("CIVETWEB_SSL_OPENSSL_API_3_0", self.spec.satisfies("^openssl@3:"))
        )
        return args
