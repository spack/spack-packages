# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re
import sys

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage

from spack.package import *

IS_WINDOWS = sys.platform == "win32"


class Curl(AutotoolsPackage, CMakePackage):
    """cURL is an open source command line tool and library for
    transferring data with URL syntax"""

    homepage = "https://curl.se/"
    url = "https://curl.haxx.se/download/curl-7.78.0.tar.bz2"

    executables = ["^curl$"]
    tags = ["build-tools", "windows"]

    maintainers("alecbcs")

    license("curl")

    version("8.21.0", sha256="ad6f2f94934b38e31e48272833c99b891d045b4565fe942a53fbd27bd3910e16")
    version("8.20.0", sha256="4be48e69cf467246cb97d369b85d78a08528f2b37cffef2418ee16e6a4eb596e")
    version("8.19.0", sha256="eba3230c1b659211a7afa0fbf475978cbf99c412e4d72d9aa92d020c460742d4")
    version("8.18.0", sha256="ffd671a3dad424fb68e113a5b9894c5d1b5e13a88c6bdf0d4af6645123b31faf")
    version("8.17.0", sha256="230032528ce5f85594d4f3eace63364c4244ccc3c801b7f8db1982722f2761f4")
    version("8.15.0", sha256="699a6d2192322792c88088576cff5fe188452e6ea71e82ca74409f07ecc62563")
    version("8.14.1", sha256="5760ed3c1a6aac68793fc502114f35c3e088e8cd5c084c2d044abdf646ee48fb")

    # TODO: add dependencies for other possible TLS backends

    # common arguments for tls variant definitions
    tls_args = {
        "description": "TLS backend",
        "multi": True,
        "values": (
            # 'amissl',
            # 'bearssl',
            "gnutls",
            "mbedtls",
            # 'mesalink',
            "openssl",
            # 'rustls',
            # 'schannel',
            # secure_transport support was removed in curl 8.15.0
            conditional("secure_transport", when="platform=darwin @:8.14"),
            # 'wolfssl',
            conditional("sspi", when="platform=windows"),
        ),
    }

    variant("tls", default="openssl", **tls_args)
    variant("tls", default="sspi", when="platform=windows", **tls_args)
    variant("tls", default="secure_transport", when="platform=darwin @:8.14", **tls_args)

    variant("nghttp2", default=True, description="build nghttp2 library (requires C++11)")
    variant("libssh2", default=False, description="enable libssh2 support")
    variant("libssh", default=False, description="enable libssh support")
    variant("gssapi", default=False, description="enable Kerberos support")
    variant("librtmp", default=False, description="enable Rtmp support")
    variant("ldap", default=False, description="enable ldap support")
    variant("libidn2", default=False, description="enable libidn2 support")
    variant(
        "libs",
        default="shared,static" if not IS_WINDOWS else "shared",
        values=("shared", "static"),
        multi=not IS_WINDOWS,
        description="Build shared libs, static libs or both",
    )

    with when("platform=windows build_system=cmake"):
        variant("static-crt", default=False, description="Link to static CRT")
        variant("unicode", default=False, description="Use the unicode version of Windows API")

    conflicts("platform=linux", when="tls=secure_transport", msg="Only supported on macOS")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build", when="platform=darwin")
    depends_on("pkgconfig", type="build", when="platform=linux")
    depends_on("pkgconfig", type="build", when="platform=freebsd")

    # CMake 4.0: is not compatible with CMake systems requiring
    # 3.0, which curl@7.63 requires
    depends_on("cmake@:3", type="build", when="build_system=cmake @:7.63")

    depends_on("gnutls@3.6.5:", when="tls=gnutls @8.18:")
    depends_on("gnutls", when="tls=gnutls")
    depends_on("mbedtls@3: +pic", when="tls=mbedtls @8.17:")
    depends_on("mbedtls@2: +pic", when="tls=mbedtls")
    depends_on("openssl@3:", when="tls=openssl @8.18:")
    depends_on("openssl", when="tls=openssl")

    depends_on("libidn2", when="+libidn2")
    depends_on("zlib-api")
    depends_on("nghttp2", when="+nghttp2")
    depends_on("libssh2", when="+libssh2")
    depends_on("libssh", when="+libssh")
    depends_on("krb5", when="+gssapi")
    depends_on("rtmpdump", when="+librtmp")

    # Perl pops up as a build-time dependency sometimes in curl.
    # They try to fix it quickly when it happens.
    # https://github.com/curl/curl/issues/12832
    # https://github.com/curl/curl/issues/13508
    # https://github.com/curl/curl/issues/18088
    depends_on("perl", type="build", when="@8.15.0")

    build_system(
        "autotools",
        "cmake",
        default="cmake" if IS_WINDOWS else "autotools",
    )

    @classmethod
    def determine_version(cls, exe):
        curl = Executable(exe)
        output = curl("--version", output=str, error=str)
        match = re.match(r"curl ([\d.]+)", output)
        return match.group(1) if match else None

    @classmethod
    def determine_variants(cls, exes, version):
        for exe in exes:
            variants = ""
            curl = Executable(exe)
            output = curl("--version", output=str, error=str)
            if "nghttp2" in output:
                variants += "+nghttp2"
            protocols_match = re.search(r"Protocols: (.*)\n", output)
            if protocols_match:
                protocols = protocols_match.group(1).strip().split(" ")
                if "ldap" in protocols:
                    variants += "+ldap"
            features_match = re.search(r"Features: (.*)\n", output)
            if features_match:
                features = features_match.group(1).strip().split(" ")
                if "GSS-API" in features:
                    variants += "+gssapi"
            # TODO: Determine TLS backend if needed.
            # TODO: Determine more variants.
            return variants

    @property
    def command(self):
        return Executable(self.prefix.bin.join("curl-config"))

    def flag_handler(self, name, flags):
        build_system_flags = []
        spec = self.spec
        if name == "cflags" and (spec.satisfies("%intel") or spec.satisfies("%oneapi")):
            build_system_flags = ["-we147"]
        return flags, None, build_system_flags


class AutotoolsBuilder(AutotoolsBuilder):
    def configure_args(self):
        spec = self.spec

        args = [
            "--with-zlib=" + spec["zlib-api"].prefix,
            # Prevent unintentional linking against system libraries: we could
            # add variants for these in the future
            "--without-brotli",
            "--without-libgsasl",
            "--without-libpsl",
            "--without-zstd",
            "--disable-docs",
            "--disable-manual",
        ]

        args += self.enable_or_disable("libs")

        # Make gnutls / openssl decide what certs are trusted.
        # TODO: certs for other tls options.
        if spec.satisfies("tls=gnutls") or spec.satisfies("tls=openssl"):
            args.extend(["--without-ca-bundle", "--without-ca-path", "--with-ca-fallback"])

        if spec.satisfies("+gssapi"):
            args.append("--with-gssapi=" + spec["krb5"].prefix)
        else:
            args.append("--without-gssapi")

        args += self.with_or_without("tls")
        args += self.with_or_without("libidn2", activation_value="prefix")
        args += self.with_or_without("librtmp")
        args += self.with_or_without("nghttp2", activation_value="prefix")
        args += self.with_or_without("libssh2", activation_value="prefix")
        args += self.with_or_without("libssh", activation_value="prefix")
        args += self.enable_or_disable("ldap")

        return args

    def with_or_without_gnutls(self, activated):
        if activated:
            return "--with-gnutls=" + self.spec["gnutls"].prefix
        else:
            return "--without-gnutls"

    def with_or_without_mbedtls(self, activated):
        if activated:
            return "--with-mbedtls=" + self.spec["mbedtls"].prefix
        else:
            return "--without-mbedtls"

    def with_or_without_openssl(self, activated):
        if activated:
            return "--with-openssl=" + self.spec["openssl"].prefix
        else:
            return "--without-openssl"

    def with_or_without_secure_transport(self, activated):
        if activated:
            return "--with-secure-transport"
        else:
            return "--without-secure-transport"


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", False),
            self.define("CURL_USE_LIBPSL", False),
            # Curl's CMake will turn this off if not building static libcurl
            self.define("BUILD_STATIC_CURL", True),
            # enables install from cmake
            self.define("CURL_DISABLE_INSTALL", False),
            self.define("BUILD_MISC_DOCS", False),
            self.define("BUILD_LIBCURL_DOCS", False),
            self.define("BUILD_EXAMPLES", False),
            self.define("CURL_BROTLI", False),
            self.define("CURL_USE_GSASL", False),
            self.define("CURL_ZSTD", False),
            self.define("ENABLE_CURL_MANUAL", False),
            self.define_from_variant("CURL_USE_LIBSSH2", "libssh2"),
            self.define_from_variant("CURL_USE_LIBSSH", "libssh"),
            self.define_from_variant("CURL_USE_OPENLDAP", "ldap"),
            self.define_from_variant("CURL_DISABLE_LDAP", "ldap"),
            self.define_from_variant("USE_NGHTTP2", "nghttp2"),
            self.define_from_variant("CURL_USE_GSSAPI", "gssapi"),
            self.define_from_variant("USE_LIBRTMP", "librtmp"),
            self.define_from_variant("USE_LIBIDN2", "libidn2"),
        ]

        if self.spec.satisfies("tls=sspi"):
            args.append(self.define("CURL_WINDOWS_SSPI", True))
        if self.spec.satisfies("tls=gnutls"):
            args.append(self.define("CURL_USE_GNUTLS", True))
        if self.spec.satisfies("tls=mbedtls"):
            args.append(self.define("CURL_USE_MBEDTLS", True))
        if self.spec.satisfies("tls=openssl"):
            args.append(self.define("CURL_USE_OPENSSL", True))

        if self.spec.satisfies("platform=windows"):
            args.extend(
                [
                    self.define_from_variant("ENABLE_UNICODE", "unicode"),
                    self.define_from_variant("CURL_STATIC_CRT", "static-crt"),
                ]
            )
            if self.spec.satisfies("+ldap"):
                args.append(self.define("USE_WIN32_LDAP", True))

        if self.spec.satisfies("libs=shared"):
            args.append(self.define("BUILD_SHARED_LIBS", True))
        if self.spec.satisfies("libs=static"):
            args.append(self.define("BUILD_STATIC_LIBS", True))
        return args
