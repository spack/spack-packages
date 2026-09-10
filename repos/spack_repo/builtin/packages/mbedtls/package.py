# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Mbedtls(CMakePackage, MakefilePackage):
    """mbed TLS (formerly known as PolarSSL) makes it trivially easy for
    developers to include cryptographic and SSL/TLS capabilities in
    their (embedded) products, facilitating this functionality with a
    minimal coding footprint.
    """

    homepage = "https://tls.mbed.org"
    url = "https://github.com/Mbed-TLS/mbedtls/releases/download/v3.6.0/mbedtls-3.6.0.tar.bz2"

    maintainers("haampie")

    license("Apache-2.0 OR GPL-2.0-or-later", checked_by="wdconinc")

    version("4.0.0", sha256="2f3a47f7b3a541ddef450e4867eeecb7ce2ef7776093f3a11d6d43ead6bf2827")
    version("3.6.2", sha256="8b54fb9bcf4d5a7078028e0520acddefb7900b3e66fec7f7175bb5b7d85ccdca")
    version("2.28.9", sha256="e85ea97aaf78dd6c0a5ba2e54dd5932ffa15f39abfc189c26beef7684630c02b")
    version("2.28.8", sha256="241c68402cef653e586be3ce28d57da24598eb0df13fcdea9d99bfce58717132")
    version("2.28.2", sha256="1db6d4196178fa9f8264bef5940611cd9febcd5d54ec05f52f1e8400f792b5a4")
    version("2.7.19", sha256="3da12b1cebe1a25da8365d5349f67db514aefcaa75e26082d7cb2fa3ce9608aa")

    build_system(
        conditional("cmake", when="@4:"), conditional("makefile", when="@:3"), default="cmake"
    )

    variant("pic", default=False, description="Compile with position independent code.")
    variant(
        "build_type",
        default="Release",
        description="Build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
        when="build_system=makefile",  # CMake has this builtin
    )
    variant(
        "libs",
        default="static",
        values=("shared", "static"),
        multi=True,
        description="What libraries to build",
    )

    depends_on("c", type="build")

    # See https://github.com/Mbed-TLS/mbedtls/issues/4917
    # Only 2.16.12, 2.28.0 and 3.1.0 support clang 12.
    conflicts("%clang@12:", when="@:2.16.11,2.17:2.27,2.29:3.0")

    # See https://github.com/ARMmbed/mbedtls/pull/5126
    # and the 2.x backport: https://github.com/ARMmbed/mbedtls/pull/5133
    patch("fix-dt-needed-shared-libs.patch", when="@2.7:2.27,3.0.0")

    def url_for_version(self, version):
        if self.spec.satisfies("@:2.28.7,3:3.5"):
            return f"https://github.com/Mbed-TLS/mbedtls/archive/refs/tags/v{version}.tar.gz"
        if self.spec.satisfies("@2.28.8,3.6.0"):
            return f"https://github.com/Mbed-TLS/mbedtls/releases/download/v{version}/mbedtls-{version}.tar.bz2"
        # release tags for @2.28.9:2,3.6.1:
        return f"https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-{version}/mbedtls-{version}.tar.bz2"

    def flag_handler(self, name, flags):
        # CMake builds have proper build types and handle PIC automatically
        if self.spec.satisfies("build_system=cmake"):
            return (flags, None, None)

        # Compile with PIC, if requested.
        build_type_to_flags = {
            "Debug": "-O0 -g",
            "Release": "-O3",
            "RelWithDebInfo": "-O2 -g",
            "MinSizeRel": "-Os",
        }
        if name == "cflags":
            build_type = self.spec.variants["build_type"].value
            flags.append(build_type_to_flags[build_type])
            if self.spec.variants["pic"].value:
                flags.append(self.compiler.cc_pic_flag)

        return (None, flags, None)


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [
            self.define("USE_STATIC_MBEDTLS_LIBRARY", self.spec.satisfies("libs=static")),
            self.define("USE_SHARED_MBEDTLS_LIBRARY", self.spec.satisfies("libs=shared")),
            self.define("ENABLE_PROGRAMS", False),
            self.define("ENABLE_TESTING", False),
        ]


class MakefileBuilder(makefile.MakefileBuilder):
    def setup_build_environment(self, env):
        if self.spec.satisfies("libs=shared"):
            env.set("SHARED", "yes")

        if self.spec.satisfies("%nvhpc"):
            # -Wno-format-nonliteral is not supported.
            env.set("WARNING_CFLAGS", "-Wall -Wextra -Wformat=2")

    def build(self, pkg, spec, prefix):
        make("no_test")

    def install(self, pkg, spec, prefix):
        make("install", "DESTDIR={0}".format(prefix))

    @run_after("install")
    def darwin_fix(self):
        if self.spec.satisfies("platform=darwin"):
            fix_darwin_install_name(self.prefix.lib)
