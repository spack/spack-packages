# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *
from spack.version import ver


class Pcsclite(AutotoolsPackage):
    """PCSC lite project

    Middleware to access a smart card using SCard API (PC/SC)."""

    homepage = "https://pcsclite.apdu.fr"
    git = "https://salsa.debian.org/rousseau/PCSC.git"

    maintainers("cessenat")

    license("GPL-3.0-or-later")

    _xz_range = ver("2:")
    def url_for_version(self, version):
        if version in self.__class__._xz_range:
            url = "https://pcsclite.apdu.fr/files/pcsc-lite-2.4.1.tar.xz"
        else:
            url = "https://pcsclite.apdu.fr/files/pcsc-lite-1.9.8.tar.bz2"
        return url

    version("2.4.1", sha256="afd3ba68c8000d2be048dc292df99a9812df9ad2efaf0a366eea22ac1faa19a7")
    version("master", branch="master")
    version("1.9.8", sha256="502d80c557ecbee285eb99fe8703eeb667bcfe067577467b50efe3420d1b2289")

    variant("libudev", default=False, description="Build with libudev")

    depends_on("c", type="build")  # generated

    depends_on("flex", type="build")
    depends_on("libusb")
    depends_on("libudev", when="+libudev")

    depends_on("autoconf", type="build")
    depends_on("autoconf-archive", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    # FIXME: add in polkit!
    # FIXME: this (or libfido2) needs:
    #        1. ccid (https://ccid.apdu.fr/)
    #        2. acsccid (https://github.com/acshk/acsccid)
    #        in order to build on arch with pacman!
    # and also then required starting up a service:
    # systemctl enable pcscd
    # Created symlink '/etc/systemd/system/sockets.target.wants/pcscd.socket' → '/usr/lib/systemd/system/pcscd.socket'.


    @when("@master")
    def autoreconf(self, spec, prefix):
        bootstrap = Executable("./bootstrap")
        bootstrap()

    def configure_args(self):
        args = []
        args.extend(self.enable_or_disable("libudev"))
        if not self.spec.dependencies("systemd"):
            args.append("--disable-systemd")
        return args
