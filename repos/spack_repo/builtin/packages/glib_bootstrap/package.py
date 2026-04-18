# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class GlibBootstrap(MesonPackage):
    """GLib provides the core application building blocks for libraries and applications written
    in C.

    The GLib package contains a low-level libraries useful for providing data structure handling
    for C, portability wrappers and interfaces for such runtime functionality as an event loop,
    threads, dynamic loading and an object system.
    """

    homepage = "https://developer.gnome.org/glib/"
    url = "https://download.gnome.org/sources/glib/2.86/glib-2.86.1.tar.xz"
    list_url = "https://download.gnome.org/sources/glib"
    list_depth = 1

    maintainers("michaelkuhn")

    license("LGPL-2.1-or-later")

    # Even minor versions are stable, odd minor versions are development, only add even numbers
    version("2.86.3", sha256="b3211d8d34b9df5dca05787ef0ad5d7ca75dec998b970e1aab0001d229977c65")
    version("2.86.1", sha256="119d1708ca022556d6d2989ee90ad1b82bd9c0d1667e066944a6d0020e2d5e57")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        depends_on("meson@1.4:", when="@2.83:")
        depends_on("pkgconfig", type="build")

    depends_on("libffi")
    depends_on("zlib-api")
    depends_on("gettext")
    depends_on("perl", type=("build", "run"))
    extends("python", type=("build", "run"))
    depends_on("pcre2@10.34:")
    depends_on("iconv")

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/glib/{version.up_to(2)}/glib-{version}.tar.xz"

    @property
    def libs(self):
        return find_libraries(["libglib*"], root=self.prefix, recursive=True)


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        args = [
            "-Dselinux=disabled",
            "-Dlibmount=disabled",
            "-Dman-pages=disabled",
            "-Ddtrace=disabled",
            "-Dsystemtap=disabled",
            "-Dsysprof=disabled",
            "-Dtests=false",
            "-Dnls=disabled",
            "-Dlibelf=disabled",
            "-Dintrospection=disabled",
        ]

        return args
