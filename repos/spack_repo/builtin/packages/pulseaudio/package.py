# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, meson
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Pulseaudio(AutotoolsPackage, MesonPackage):
    """PulseAudio is a sound system for POSIX OSes, meaning that it is a proxy
    for your sound applications.

    PulseAudio is a sound system for POSIX OSes, meaning that it is a proxy for
    your sound applications. It allows you to do advanced operations on your
    sound data as it passes between your application and your hardware. Things
    like transferring the audio to a different machine, changing the sample
    format or channel count and mixing several sounds into one are easily
    achieved using a sound server."""

    homepage = "https://www.freedesktop.org/wiki/Software/PulseAudio/"
    url = "https://freedesktop.org/software/pulseaudio/releases/pulseaudio-17.0.tar.xz"

    license("LGPL-2.1-or-later")

    build_system(
        conditional("autotools", when="@:16"), conditional("meson", when="@17:"), default="meson"
    )

    version("17.0", sha256="053794d6671a3e397d849e478a80b82a63cb9d8ca296bd35b73317bb5ceb87b5")
    version("13.0", sha256="961b23ca1acfd28f2bc87414c27bb40e12436efcf2158d29721b1e89f3f28057")

    variant("alsa", default=False, description="alsa support")
    variant("fftw", default=False, description="FFTW support")
    variant("openssl", default=False, description="openSSL support (used for Airtunes/RAOP)")
    variant("x11", default=False, description="x11 support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    with when("build_system=autotools"):
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")
    with when("build_system=meson"):
        depends_on("meson", type="build")
        depends_on("gettext", type="build")

    depends_on("alsa-lib@1.0.19:", when="+alsa")
    depends_on("dbus@1.4.12:")
    depends_on("fftw@3:", when="+fftw")
    depends_on("gdbm")
    depends_on("gettext@0.18.1:")
    depends_on("glib")
    depends_on("json-c@0.11:")
    depends_on("libcap")
    depends_on("iconv")
    depends_on("libsndfile@1.0.18:")
    depends_on("libtool@2.4:", type="link")  # links to libltdl.so
    depends_on("libsm", when="+x11")
    depends_on("uuid", when="+x11")
    depends_on("libx11", when="+x11")
    depends_on("libxcb", when="+x11")
    depends_on("libxau", when="+x11")
    depends_on("libxext", when="+x11")
    depends_on("libxi", when="+x11")
    depends_on("libxtst", when="+x11")
    depends_on("openssl", when="+openssl")
    depends_on("perl-xml-parser", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("speexdsp@1.2:")
    depends_on("m4", type="build")

    patch("atomic.patch", when="@13")


class SetupEnvironment:
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.append_flags("LDFLAGS", "-Wl,--copy-dt-needed-entries")
        if self.spec.satisfies("build_system=meson"):
            env.append_flags("CPPFLAGS", "-I{0}".format(self.spec["libiconv"].prefix.include))
            env.append_flags("LDFLAGS", "-L{0} -liconv".format(self.spec["libiconv"].prefix.lib))


class AutotoolsBuilder(autotools.AutotoolsBuilder, SetupEnvironment):
    def configure_args(self):
        args = [
            "--disable-systemd-daemon",
            "--disable-systemd-journal",
            "--disable-systemd-login",
            "--disable-udev",
            "--disable-waveout",
            "--enable-dbus",
            "--enable-glib2",
            "--with-database=gdbm",
            "--with-systemduserunitdir=no",
            "CXXFLAGS={0}".format(self.spec["libtool"].headers.cpp_flags),
            "LDFLAGS={0}".format(self.spec["libtool"].libs.search_flags),
            "--libdir={0}".format(self.prefix.lib),
        ]
        # toggle based on variants
        args += self.enable_or_disable("alsa")
        args += self.enable_or_disable("openssl")
        args += self.enable_or_disable("x11")
        args += self.with_or_without("fftw")

        # possible future variants
        args.extend(
            [
                "--disable-asyncns",
                "--disable-avahi",
                "--disable-bluez5",
                "--disable-gcov",
                "--disable-gsettings",
                "--disable-gtk3",
                "--disable-hal-compat",
                "--disable-jack",
                "--disable-lirc",
                "--disable-orc",
                "--disable-tcpwrap",
            ]
        )

        return args


class MesonBuilder(meson.MesonBuilder, SetupEnvironment):
    def meson_args(self):
        return [
            "-Ddatabase=gdbm",
            "-Ddoxygen=false",
            "-Dbluez5=disabled",
            "-Dx11=disabled",
            "-Dtests=false",
            "-Ddefault_library=shared",
            "-Dprefix={0}".format(self.prefix),
            "-Dlibdir={0}".format(self.prefix.lib),
            "-Dbashcompletiondir={0}/share/bash-completion/completions".format(self.prefix),
            "-Dsystemduserunitdir={0}systemd/user".format(self.prefix.lib),
            "-Dudevrulesdir={0}udev/rules.d".format(self.prefix.lib),
        ]
