# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Gspell(MesonPackage):
    """A spell-checking library for GTK applications"""

    homepage = "https://github.com/gnome/gspell"
    url = "https://download.gnome.org/sources/gspell/1.14/gspell-1.14.0.tar.xz"

    maintainers("KineticTheory")

    license("GNU LGPL-2.1")

    version("1.14.0", sha256="64ea1d8e9edc1c25b45a920e80daf67559d1866ffcd7f8432fecfea6d0fe8897")

    depends_on("c", type="build")

    depends_on("cairo", type="build")
    depends_on("enchant", type="build")
    depends_on("glib@2.54:", type="build")
    depends_on("gtk-doc", type="build")
    depends_on("gtkplus")
    depends_on("harfbuzz", type="build")
    depends_on("icu4c", type="build")
    depends_on("libffi", type="build")
    depends_on("mesa", type="build")
    depends_on("pcre2", type="build")
    depends_on("vala", type="build")
    depends_on("zlib", type="build")

    def url_for_version(self, version):
        return (
            f"https://download.gnome.org/sources/gspell/{version.up_to(2)}/gspell-{version}.tar.xz"
        )

    def meson_args(self):
        return ["-Dgtk_doc=false", "-Dtests=false"]
