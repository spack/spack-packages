# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, meson
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Gtkplus(AutotoolsPackage, MesonPackage):
    """The GTK+ package contains libraries used for creating graphical user
    interfaces for applications."""

    homepage = "https://www.gtk.org/"
    url = "https://download.gnome.org/sources/gtk/3.24/gtk-3.24.50.tar.xz"

    license("LGPL-2.0-or-later")

    build_system(
        conditional("autotools", when="@:3.24.35"),
        conditional("meson", when="@3.24.9:"),
        default="meson",
    )

    version("3.24.50", sha256="399118a5699314622165a11b769ea9b6ed68e037b6d46d57cfcf4851dec07529")
    version("3.24.43", sha256="7e04f0648515034b806b74ae5d774d87cffb1a2a96c468cb5be476d51bf2f3c7")
    version("3.24.41", sha256="47da61487af3087a94bc49296fd025ca0bc02f96ef06c556e7c8988bd651b6fa")
    version("3.24.29", sha256="f57ec4ade8f15cab0c23a80dcaee85b876e70a8823d9105f067ce335a8268caa")
    version("3.24.26", sha256="2cc1b2dc5cad15d25b6abd115c55ffd8331e8d4677745dd3ce6db725b4fff1e9")

    variant("cups", default=False, description="enable cups support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # See meson.build for version requirements
    depends_on("meson@0.48.0:", when="build_system=meson", type="build")
    depends_on("ninja", when="build_system=meson", type="build")
    # Needed to build man pages:
    # depends_on('docbook-xml', when='@3.24:', type='build')
    # depends_on('docbook-xsl', when='@3.24:', type='build')
    # depends_on('libxslt', when='@3.24:', type='build')
    depends_on("pkgconfig", type="build")
    depends_on("glib")
    depends_on("glib@2.49.4:", when="@3.22:")
    depends_on("glib@2.57.2:", when="@3.24:")
    depends_on("pango@1.41.0:+X")
    depends_on("fribidi@0.19.7:")
    # atk was also merged into at-spi2-core, but gtk3 doesn't want to build without it
    depends_on("atk@2.35.1:", when="@:3")
    # at-spi2-atk was merged into at-spi2-core, but gtk3 is picky
    depends_on("at-spi2-core@2.46:2.48", when="@:3")
    depends_on("cairo@1.14.0:+X+pdf+gobject")
    depends_on("gdk-pixbuf@2.30.0:")
    depends_on("gobject-introspection@1.39.0:")
    depends_on("shared-mime-info")
    depends_on("libxkbcommon")
    depends_on("librsvg")
    depends_on("xrandr")
    depends_on("libepoxy+glx", when="@3:")
    depends_on("libxi", when="@3:")
    depends_on("inputproto", when="@3:")
    depends_on("fixesproto", when="@3:")
    depends_on("gettext", when="@3:")
    depends_on("cups", when="+cups")
    depends_on("libxfixes", when="@:2")

    conflicts("%gcc@14:", when="@:3.24.35")

    patch("no-demos.patch", when="@2.0:2")

    def url_for_version(self, version):
        if self.spec.satisfies("@:3.24.43"):
            url = "https://download.gnome.org/sources/gtk+/{0}/gtk+-{1}.tar.xz"
        else:
            url = "https://download.gnome.org/sources/gtk/{0}/gtk-{1}.tar.xz"
        return url.format(version.up_to(2), version)

    def patch(self):
        if self.spec.satisfies("@:3.24.35"):
            # remove disable deprecated flag.
            filter_file(
                r'CFLAGS="-DGDK_PIXBUF_DISABLE_DEPRECATED $CFLAGS"', "", "configure", string=True
            )

        # https://gitlab.gnome.org/GNOME/gtk/-/issues/3776
        if self.spec.satisfies("@3.24:%gcc@11:"):
            filter_file("    '-Werror=array-bounds',", "", "meson.build", string=True)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))


class BuildEnvironment:
    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))


class MesonBuilder(BuildEnvironment, meson.MesonBuilder):
    def meson_args(self):
        args = []

        if self.spec.satisfies("platform=darwin"):
            args.extend(["-Dx11_backend=false", "-Dquartz_backend=true"])

        args.extend(
            ["-Dgtk_doc=false", "-Dman=false", "-Dintrospection=true", "-Dwayland_backend=false"]
        )

        args.append("-Dprint_backends=file,lpr{0}".format(",cups" if "+cups" in self.spec else ""))

        return args

    def check(self):
        """All build time checks open windows in the X server, don't do that"""
        pass


class AutotoolsBuilder(BuildEnvironment, autotools.AutotoolsBuilder):
    def configure_args(self):
        true = which("true", required=True)
        args = [
            "--prefix={0}".format(self.prefix),
            # disable building of gtk-doc files following #9771
            "--disable-gtk-doc-html",
            "GTKDOC_CHECK={0}".format(true),
            "GTKDOC_CHECK_PATH={0}".format(true),
            "GTKDOC_MKPDF={0}".format(true),
            "GTKDOC_REBASE={0}".format(true),
        ]
        if self.spec.satisfies("~cups"):
            args.append("--disable-cups")
        return args

    def check(self):
        """All build time checks open windows in the X server, don't do that"""
        pass
