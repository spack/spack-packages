# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class BitcoinCore(AutotoolsPackage, CMakePackage):
    """Bitcoin Core is the reference implementation of the Bitcoin protocol."""

    homepage = "https://bitcoincore.org/"
    url = "https://bitcoincore.org/bin/bitcoin-core-30.2/bitcoin-30.2.tar.gz"

    license("MIT")

    version("30.2", sha256="6fd00b8c42883d5c963901ad4109a35be1e5ec5c2dc763018c166c21a06c84cb")
    version("29.2", sha256="a529d75d0512317d6334bb9fd74cb6ddca3b1eb345d2e9e31b66136583ecc045")
    version("29.1", sha256="067f624ae273b0d85a1554ffd7c098923351a647204e67034df6cc1dfacfa06b")
    version("28.4", sha256="2950d5e37d04ca7fadad615a06b964cdeab3a6995867f8c172a67733dbd91c89")

    build_system(
        conditional("cmake", when="@29:"),
        conditional("autotools", when="@:28"),
        default="cmake",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("python@3.9:", type="build")

    depends_on("cmake@3.22:", type="build", when="build_system=cmake")
    depends_on("autoconf", type="build", when="build_system=autotools")
    depends_on("automake", type="build", when="build_system=autotools")
    depends_on("libtool", type="build", when="build_system=autotools")

    depends_on("boost@1.81:+filesystem+program_options+system+test+thread")
    depends_on("libevent")
    depends_on("sqlite", when="+wallet+sqlite")
    depends_on("berkeley-db@4.8:5", when="+wallet+bdb")
    depends_on("libzmq", when="+zmq")
    depends_on("dbus", when="+gui+dbus")
    depends_on("libqrencode", when="+gui+qrcode")

    # Qt5 era
    depends_on("qt", when="@28:29 +gui")

    # Qt6 era
    depends_on("qt-base", when="@30: +gui")
    depends_on("qt-tools", when="@30: +gui")

    variant("daemon", default=True, description="Build bitcoind daemon")
    variant("cli", default=True, description="Build bitcoin-cli and utility binaries")
    variant("util", default=True, description="Build bitcoin-util")
    variant("wallet", default=True, description="Enable wallet support")
    variant("sqlite", default=True, description="Enable SQLite wallet backend")
    variant("bdb", default=False, description="Enable Berkeley DB legacy wallet backend")
    variant("gui", default=False, description="Build bitcoin-qt GUI")
    variant("dbus", default=True, description="Enable D-Bus integration in GUI")
    variant("qrcode", default=True, description="Enable QR code support in GUI")
    variant("zmq", default=False, description="Enable ZeroMQ notifications")
    variant("usdt", default=False, description="Enable USDT tracing support")
    variant("multiprocess", default=False, description="Build multiprocess experimental binaries")
    variant("tests", default=False, description="Build unit tests")
    variant("bench", default=False, description="Build benchmark binary")
    variant("fuzz", default=False, description="Build fuzz binary")
    variant("hardening", default=True, description="Enable hardening flags")
    variant("werror", default=False, description="Treat compiler warnings as errors")

    conflicts("+sqlite", when="~wallet", msg="SQLite backend requires wallet support")
    conflicts("+bdb", when="~wallet", msg="Berkeley DB backend requires wallet support")
    conflicts("+dbus", when="~gui", msg="D-Bus requires GUI")
    conflicts("+qrcode", when="~gui", msg="QR code support requires GUI")

    def url_for_version(self, version):
        return f"https://bitcoincore.org/bin/bitcoin-core-{version}/bitcoin-{version}.tar.gz"


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def autoreconf(self, pkg, spec, prefix):
        autogen = join_path(pkg.stage.source_path, "autogen.sh")
        if is_exe(autogen):
            bash = which("bash")
            with working_dir(pkg.stage.source_path):
                bash("./autogen.sh")

    def configure_args(self):
        args = []

        if self.spec.satisfies("+wallet"):
            args.append("--enable-wallet")
        else:
            args.append("--disable-wallet")

        if self.spec.satisfies("+sqlite"):
            args.append("--with-sqlite=yes")
        else:
            args.append("--with-sqlite=no")

        if self.spec.satisfies("+bdb"):
            args.append("--with-bdb")
        else:
            args.append("--without-bdb")

        if self.spec.satisfies("+zmq"):
            args.append("--with-zmq")
        else:
            args.append("--without-zmq")

        if self.spec.satisfies("+gui"):
            args.append("--with-gui=qt5")
        else:
            args.append("--without-gui")

        if self.spec.satisfies("+dbus"):
            args.append("--enable-dbus")
        else:
            args.append("--disable-dbus")

        if self.spec.satisfies("+qrcode"):
            args.append("--with-qrencode")
        else:
            args.append("--without-qrencode")

        if self.spec.satisfies("+tests"):
            args.append("--enable-tests")
        else:
            args.append("--disable-tests")

        if self.spec.satisfies("+bench"):
            args.append("--enable-bench")
        else:
            args.append("--disable-bench")

        if self.spec.satisfies("+hardening"):
            args.append("--enable-hardening")
        else:
            args.append("--disable-hardening")

        if self.spec.satisfies("+werror"):
            args.append("--enable-werror")
        else:
            args.append("--disable-werror")

        return args


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_DAEMON", "daemon"),
            self.define_from_variant("BUILD_CLI", "cli"),
            self.define_from_variant("BUILD_UTIL", "util"),
            self.define_from_variant("BUILD_GUI", "gui"),
            self.define_from_variant("BUILD_TESTS", "tests"),
            self.define_from_variant("BUILD_BENCH", "bench"),
            self.define_from_variant("BUILD_FUZZ_BINARY", "fuzz"),
            self.define_from_variant("ENABLE_WALLET", "wallet"),
            self.define_from_variant("WITH_SQLITE", "sqlite"),
            self.define_from_variant("WITH_ZMQ", "zmq"),
            self.define_from_variant("WITH_DBUS", "dbus"),
            self.define_from_variant("WITH_QRENCODE", "qrcode"),
            self.define_from_variant("WITH_USDT", "usdt"),
            self.define_from_variant("WITH_MULTIPROCESS", "multiprocess"),
            self.define_from_variant("ENABLE_HARDENING", "hardening"),
            self.define_from_variant("WERROR", "werror"),
            self.define_from_variant("WITH_BDB", "bdb"),
        ]
        return args
