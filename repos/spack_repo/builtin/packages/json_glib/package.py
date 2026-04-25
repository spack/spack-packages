# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class JsonGlib(MesonPackage):
    """JSON-GLib is a library for reading and parsing JSON using GLib and
    GObject data types and API."""

    homepage = "https://developer.gnome.org/json-glib"
    url = "https://ftp.gnome.org/pub/gnome/sources/json-glib/1.2/json-glib-1.2.8.tar.xz"
    list_url = "https://ftp.gnome.org/pub/gnome/sources/json-glib/"
    list_depth = 1

    license("LGPL-2.1-or-later")

    version("1.10.8", sha256="55c5c141a564245b8f8fbe7698663c87a45a7333c2a2c56f06f811ab73b212dd")
    version("1.9.2", sha256="8f9f04e0045bda82affd464ee575796600fe29014b817392a3b72ceb2d10c595")
    version("1.6.6", sha256="96ec98be7a91f6dde33636720e3da2ff6ecbb90e76ccaa49497f31a6855a490e")

    depends_on("c", type="build")

    depends_on("glib")
    depends_on("gobject-introspection")
    depends_on("pkgconfig", type="build")
    depends_on("gmake", type="build")

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/json-glib/{version.up_to(2)}/json-glib-{version}.tar.xz"

    def meson_args(self):
        args = ["-Ddocumentation=disabled"]
        return args
