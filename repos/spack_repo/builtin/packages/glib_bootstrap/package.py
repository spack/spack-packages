# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class GlibBootstrap(MesonPackage):
    """GLib with no dependency on gobject-introspection used to bootstrap a gobject-introspection."""

    homepage = "https://developer.gnome.org/glib/"
    url = "https://download.gnome.org/sources/glib/2.82/glib-2.82.5.tar.xz"
    list_url = "https://download.gnome.org/sources/glib"
    list_depth = 1

    maintainers("michaelkuhn")

    license("LGPL-2.1-or-later")

    # Even minor versions are stable, odd minor versions are development, only add even numbers
    version("2.86.1", sha256="119d1708ca022556d6d2989ee90ad1b82bd9c0d1667e066944a6d0020e2d5e57")
    version("2.82.5", sha256="05c2031f9bdf6b5aba7a06ca84f0b4aced28b19bf1b50c6ab25cc675277cbc3f")
    version("2.82.2", sha256="ab45f5a323048b1659ee0fbda5cecd94b099ab3e4b9abf26ae06aeb3e781fd63")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        depends_on("meson@1.4:", when="@2.83:")
        depends_on("meson@1.2:", when="@2.79:")
        depends_on("pkgconfig", type="build")

    depends_on("libffi")
    depends_on("zlib-api")
    depends_on("gettext")
    depends_on("perl", type=("build", "run"))
    extends("python", type=("build", "run"))
    depends_on("pcre2@10.34:", when="@2.74:")
    depends_on("iconv")
    depends_on("elf")  # bin/gresource

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/glib/{version.up_to(2)}/glib-{version}.tar.xz"

    def patch(self):
        """A few glib tests have external dependencies / try to access the X server"""
        # Surgically disable tests which we cannot make pass in a spack build
        gio_tests = FileFilter("gio/tests/meson.build")
        gio_tests.filter("if not glib_have_cocoa", "if false")
        gio_tests.filter("'contenttype' : {},", "")
        gio_tests.filter("'file' : {},", "")
        gio_tests.filter("'gdbus-peer'", "'file'")
        gio_tests.filter("'gdbus-address-get-session' : {},", "")
        filter_file("'fileutils' : {},", "", "glib/tests/meson.build")

    @property
    def libs(self):
        return find_libraries(["libglib*"], root=self.prefix, recursive=True)


class MesonBuilder(meson.MesonBuilder):

    @run_after("install")
    def gettext_libdir(self):
        # Packages that link to glib were also picking up -lintl from glib's
        # glib-2.0.pc file. However, packages such as py-pygobject were
        # bypassing spack's compiler wrapper for linking and thus not finding
        # the gettext library directory. The patch below explicitly adds the
        # appropriate -L path.
        spec = self.spec
        if (
            spec.satisfies("@2")
            and "intl" in spec["gettext"].libs.names
            and not is_system_path(spec["gettext"].prefix)
        ):
            filter_file(
                "Libs:",
                "Libs: -L{0} -Wl,-rpath={0} ".format(spec["gettext"].libs.directories[0]),
                join_path(
                    self.spec["glib-bootstrap"].libs.directories[0], "pkgconfig", "glib-2.0.pc"
                ),
            )

    def meson_args(self):
        args = []
        args.append("-Dlibmount=disabled")
        args.append("-Ddtrace=false")
        args.append("-Dsystemtap=false")
        args.append("-Dselinux=disabled")
        args.append("-Dgtk_doc=false")
        args.append("-Dlibelf=enabled")
        args.append("-Dintrospection=disabled")
        args.append("-Dglib_debug=disabled")
        args.append("-Dman=false")
        args.append("-Dman-pages=false")

        return args
