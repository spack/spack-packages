# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Krb5(AutotoolsPackage):
    """Network authentication protocol"""

    homepage = "https://kerberos.org"
    url = "https://kerberos.org/dist/krb5/1.16/krb5-1.16.1.tar.gz"
    list_url = "https://kerberos.org/dist/krb5/"
    list_depth = 1

    license("MIT", checked_by="wdconinc")

    version("1.21.3", sha256="b7a4cd5ead67fb08b980b21abd150ff7217e85ea320c9ed0c6dadd304840ad35")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("diffutils", type="build")
    depends_on("bison", type="build")
    depends_on("openssl")
    depends_on("gettext")
    depends_on("libedit")
    depends_on("perl", type="build")
    depends_on("findutils", type="build")
    depends_on("pkgconfig", type="build")

    variant(
        "shared", default=True, description="install shared libraries if True, static if false"
    )
    patch("freebsd-link.patch", when="platform=freebsd")

    configure_directory = "src"
    build_directory = "src"

    executables = ["^krb5-config$"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"Kerberos 5 release\s+(\S+)", output)
        return match.group(1) if match else None

    def url_for_version(self, version):
        url = "https://kerberos.org/dist/krb5/{0}/krb5-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def patch(self):
        # https://github.com/Homebrew/homebrew-core/blob/master/Formula/krb5.rb
        # https://krbdev.mit.edu/rt/Ticket/Display.html?id=8928
        filter_file(
            "void foo1() __attribute__((constructor));",
            "#include <unistd.h>\nvoid foo1() __attribute__((constructor));",
            join_path(self.configure_directory, "configure"),
            string=True,
        )

    def configure_args(self):
        spec = self.spec
        args = ["--without-system-verto", "--without-keyutils"]

        if spec.satisfies("~shared"):
            args.append("--enable-static")
            args.append("--disable-shared")
        else:
            args.append("--disable-static")

        # https://github.com/spack/spack/issues/34193
        if spec.satisfies("%gcc@10:"):
            args.append("CFLAGS=-fcommon")

        if spec["openssl"].satisfies("~shared"):
            pkgconf = which("pkg-config")
            ssllibs = pkgconf("--static", "--libs", "openssl", output=str)
            args.append(f"LDFLAGS={ssllibs}")

        return args

    def flag_handler(self, name, flags):
        if name == "ldlibs" and "intl" in self.spec["gettext"].libs.names:
            flags.append("-lintl")

        if name == "cflags":
            if self.spec.satisfies("@:1.21.3 %gcc@15:"):
                # gcc@15: is -std=gnu23 by default and
                # up to at least 1.21.3 doesn't compile
                flags.append("-std=gnu17")

        return (flags, None, None)
