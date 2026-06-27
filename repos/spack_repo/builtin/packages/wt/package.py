# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Wt(CMakePackage):
    """Wt, C++ Web Toolkit.

    Wt is a C++ library for developing web applications."""

    homepage = "https://www.webtoolkit.eu/wt"
    url = "https://github.com/emweb/wt/archive/4.13.2.tar.gz"
    git = "https://github.com/emweb/wt.git"

    version("master", branch="master")
    version("4.13.2", sha256="10955bf9ffa912fb00314f0969e51128d25940effdeee9059d74257fcc5a6c16")
    version(
        "3.3.7",
        sha256="054af8d62a7c158df62adc174a6a57610868470a07e7192ee7ce60a18552851d",
        deprecated=True,
    )

    # wt builds in parallel, but requires more than 5 GByte RAM per -j <njob>
    # which most machines do not provide and crash the build
    parallel = False

    variant(
        "openssl",
        default=True,
        description="SSL and WebSockets support in the built-in httpd, "
        "the HTTP(S) client, and additional cryptographic "
        "hashes in the authentication module",
    )
    variant("libharu", default=True, description="painting to PDF")
    # variant('graphicsmagick', default=True,
    #         description='painting to PNG, GIF')
    variant("sqlite", default=False, description="create SQLite3 DBO")
    variant("mariadb", default=False, description="create MariaDB/MySQL DBO")
    variant("postgresql", default=False, description="create PostgreSQL DBO")
    # variant('firebird', default=False, description='create Firebird DBO')
    variant(
        "pango", default=True, description="improved font support in PDF and raster image painting"
    )
    variant("zlib", default=True, description="compression in the built-in httpd")
    # variant('fastcgi', default=False,
    #         description='FastCGI connector via libfcgi++')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pkgconfig", type="build")
    with when("@3"):
        depends_on("boost@1.46.1:1.65")
        depends_on(Boost.with_default_variants)

    depends_on("boost@1.71:+program_options+thread+filesystem+system", when="@4:")

    depends_on("openssl", when="+openssl")
    depends_on("libharu", when="+libharu")
    depends_on("sqlite", when="+sqlite")
    depends_on("mariadb", when="+mariadb")
    depends_on("postgresql", when="+postgresql")
    depends_on("pango", when="+pango")
    depends_on("zlib-api", when="+zlib")

    def cmake_args(self):
        return [
            self.define("BUILD_EXAMPLES", False),
            self.define("CONNECTOR_FCGI", False),
            self.define("ENABLE_OPENGL", False),
            self.define("ENABLE_QT4", False),
            self.define_from_variant("ENABLE_SSL", "openssl"),
            self.define_from_variant("ENABLE_HARU", "libharu"),
            self.define_from_variant("ENABLE_PANGO", "pango"),
            self.define_from_variant("ENABLE_SQLITE", "sqlite"),
            self.define_from_variant("ENABLE_MYSQL", "mariadb"),
            self.define_from_variant("ENABLE_POSTGRES", "postgresql"),
        ]
