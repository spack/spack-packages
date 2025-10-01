# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libgee(AutotoolsPackage):
    """Libgee is a collection library providing GObject-based interfaces and classes for commonly
    used data structures."""

    homepage = "https://gitlab.gnome.org/GNOME/libgee"
    url = "https://download.gnome.org/sources/libgee/0.20/libgee-0.20.8.tar.xz"
    git = "https://gitlab.gnome.org/GNOME/libgree.git"

    maintainers("KineticTheory")

    license("GNU LGPL-2.1")

    version("0.20.8", sha256="189815ac143d89867193b0c52b7dc31f3aa108a15f04d6b5dca2b6adfad0b0ee")

    depends_on("c", type="build")

    depends_on("autoconf", type="build")
    depends_on("m4", type="build")
    depends_on("glib@2.54:", type="build")
    depends_on("vala", type="build")

    def configure_args(self):
        extra_args = ["--enable-vala"]
        return extra_args

    def url_for_version(self, version):
        return (
            f"https://download.gnome.org/sources/libgee/{version.up_to(2)}/libgee-{version}.tar.xz"
        )
