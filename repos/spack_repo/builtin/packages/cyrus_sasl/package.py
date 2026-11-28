# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class CyrusSasl(AutotoolsPackage):
    """This is the Cyrus SASL API implementation. It can be used on the
    client or server side to provide authentication and authorization
    services."""

    homepage = "https://github.com/cyrusimap/cyrus-sasl"
    url = "https://github.com/cyrusimap/cyrus-sasl/archive/cyrus-sasl-2.1.27.tar.gz"
    git = "https://github.com/cyrusimap/cyrus-sasl.git"

    license("custom")

    version("2.1.28", sha256="3e38933a30b9ce183a5488b4f6a5937a702549cde0d3287903d80968ad4ec341")

    # master snapshot once needed for gcc@15; superseded by -std=gnu17 in flag_handler
    version(
        "2.1.28-148-ge256dd0c",
        commit="e256dd0cc61d60cbb905b601241077f0a2ba0907",
        deprecated=True,
    )

    # ensure include time.h, https://github.com/cyrusimap/cyrus-sasl/pull/709
    patch(
        "https://github.com/cyrusimap/cyrus-sasl/commit/266f0acf7f5e029afbb3e263437039e50cd6c262.patch?full_index=1",
        sha256="819342fe68475ac1690136ff4ce9b73c028f433ae150898add36f724a8e2274b",
        when="@2.1.27:2.1.28-0",
    )

    depends_on("c", type="build")

    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("groff", type="build")

    depends_on("openssl", type="link")
    depends_on("libxcrypt", type="link")
    depends_on("krb5", type="link")

    def flag_handler(self, name, flags):
        # md5.c uses K&R definitions, rejected by C23
        if name == "cflags" and self.spec.satisfies("@:2.1.28-147"):
            flags.append("-std=gnu17")
        return (flags, None, None)

    @when("platform=darwin")
    def configure_args(self):
        # avoid installing to /Library/Frameworks/SASL2.framework
        return ["--disable-macos-framework"]
