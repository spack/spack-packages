# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libhandy(MesonPackage):
    """The libhandy package provides additional GTK UI widgets for use in developing user
    interfaces."""

    homepage = "https://github.com/gnome/libhandy"
    url = "https://download.gnome.org/sources/libhandy/1.8/libhandy-1.8.3.tar.xz"

    maintainers("KineticTheory")

    license("GNU LGPL-2.1")

    version("1.8.3", sha256="05b497229073ff557f10b326e074c5066f8743a302d4820ab97bcb5cd2dab087")

    depends_on("c", type="build")

    depends_on("cairo", type=("build", "link"))
    depends_on("dbus", type="build")
    depends_on("glib@2.54:", type=("build", "link"))
    depends_on("gtkplus", type=("build", "link"))
    depends_on("harfbuzz", type="build")
    depends_on("mesa", type="build")
    depends_on("vala", type=("build", "link"))

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/libhandy/{version.up_to(2)}/libhandy-{version}.tar.xz"
