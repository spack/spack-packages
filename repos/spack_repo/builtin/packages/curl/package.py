# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os
import re
import sys

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.nmake import NMakeBuilder, NMakePackage

from spack.package import *

IS_WINDOWS = sys.platform == "win32"


class Curl(NMakePackage, AutotoolsPackage, CMakePackage):
    """cURL is an open source command line tool and library for
    transferring data with URL syntax"""

    homepage = "https://curl.se/"
    url = "https://curl.haxx.se/download/curl-7.78.0.tar.bz2"

    executables = ["^curl$"]
    tags = ["build-tools", "windows"]

    maintainers("alecbcs")

    license("curl")

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
    depends_on("cmake@:3", when="build_system=cmake @:7.63")

    depends_on("gnutls", when="tls=gnutls")
    depends_on("mbedtls@2: +pic", when="tls=mbedtls")
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
        conditional("nmake", when="@:8.11 platform=windows"),
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


class BuildEnvironment:
    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        if self.spec.satisfies("libs=static"):
            env.append_flags("CFLAGS", "-DCURL_STATICLIB")
            env.append_flags("CXXFLAGS", "-DCURL_STATICLIB")


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


class NMakeBuilder(BuildEnvironment, NMakeBuilder):
    phases = ["install"]

    def nmake_args(self):
        args = []
        mode = "dll" if self.spec.satisfies("libs=shared") else "static"
        args.append("mode=%s" % mode)
        args.append("WITH_ZLIB=%s" % mode)
        args.append("ZLIB_PATH=%s" % self.spec["zlib-api"].prefix)
        args.append("WINBUILD_ACKNOWLEDGE_DEPRECATED=yes")
        if self.spec.satisfies("+libssh"):
            args.append("WITH_SSH=%s" % mode)
        if self.spec.satisfies("+libssh2"):
            args.append("WITH_SSH2=%s" % mode)
            args.append("SSH2_PATH=%s" % self.spec["libssh2"].prefix)
        if self.spec.satisfies("+nghttp2"):
            args.append("WITH_NGHTTP2=%s" % mode)
            args.append("NGHTTP2=%s" % self.spec["nghttp2"].prefix)
        if self.spec.satisfies("tls=openssl"):
            args.append("WITH_SSL=%s" % mode)
            args.append("SSL_PATH=%s" % self.spec["openssl"].prefix)
        elif self.spec.satisfies("tls=mbedtls"):
            args.append("WITH_MBEDTLS=%s" % mode)
            args.append("MBEDTLS_PATH=%s" % self.spec["mbedtls"].prefix)
        elif self.spec.satisfies("tls=sspi"):
            args.append("ENABLE_SSPI=%s" % mode)

        # The trailing path seperator is REQUIRED for cURL to install
        # otherwise cURLs build system will interpret the path as a file
        # and the install will fail with ambiguous errors
        inst_prefix = self.prefix + "\\"
        args.append(f"WITH_PREFIX={windows_sfn(inst_prefix)}")
        return args

    def install(self, pkg, spec, prefix):
        # Spack's env CC and CXX values will cause an error
        # if there is a path in the space, and escaping with
        # double quotes raises a syntax issues, instead
        # cURLs nmake will automatically invoke proper cl.exe if
        # no env value for CC, CXX is specified
        # Unset the value to allow for cURLs heuristics (derive via VCVARS)
        # to derive the proper compiler
        env = os.environ
        env["CC"] = ""
        env["CXX"] = ""
        winbuild_dir = os.path.join(self.stage.source_path, "winbuild")
        winbuild_dir = windows_sfn(winbuild_dir)
        with working_dir(winbuild_dir):
            nmake("/f", "Makefile.vc", *self.nmake_args(), ignore_quotes=True)
        with working_dir(os.path.join(self.stage.source_path, "builds")):
            install_dir = glob.glob("libcurl-**")[0]
            install_tree(install_dir, self.prefix)
        if spec.satisfies("libs=static"):
            # curl is named libcurl_a when static on Windows
            # Consumers look for just libcurl
            # make a symlink to make consumers happy
            libcurl_a = os.path.join(prefix.lib, "libcurl_a.lib")
            libcurl = os.path.join(self.prefix.lib, "libcurl.lib")
            # safeguard against future curl releases that do this for us
            if os.path.exists(libcurl_a) and not os.path.exists(libcurl):
                symlink(libcurl_a, libcurl)


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
