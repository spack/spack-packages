# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libgit2Glib(MesonPackage):
    """libgit2-glib is a glib wrapper library around the libgit2 git access library.
    libgit2 only implements the core plumbing functions, not really the higher
    level porcelain stuff."""

    homepage = "https://gitlab.gnome.org/GNOME/libgit2-glib"
    url = "https://download.gnome.org/sources/libgit2-glib/1.2/libgit2-glib-1.2.1.tar.xz"

    maintainers("KineticTheory")

    license("LGPL-2.1-or-later")

    version("1.2.1", sha256="97423a779002b3be8751c75f9d79049dfccca3616a26159fc162486772ba785f")

    variant("python", default=True, description="Build with python support")
    variant("vapi", default=True, description="Build Vala bindings")

    depends_on("c", type="build")

    depends_on("cairo", type="build")
    depends_on("glib@2.44:", type="build")
    depends_on("gobject-introspection", type=("build", "link"))
    depends_on("gtkplus", type="build")
    depends_on("harfbuzz", type="build")
    depends_on("libgit2", type=("build", "link"))
    depends_on("pcre2", type="build")
    depends_on("py-pygobject", when="+python", type="build")
    depends_on("vala", when="+vapi", type="build")

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/libgit2-glib/{version.up_to(2)}/libgit2-glib-{version}.tar.xz"


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        args = []
        if not self.spec.satisfies("^libgit2+ssh"):
            args.append("-Dssh=false")
        if self.spec.satisfies("~vapi"):
            args.append("-Dvapi=false")
        if self.spec.satisfies("~python"):
            args.append("-Dpython=false")
        return args
