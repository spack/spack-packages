# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPygobject(MesonPackage, PythonPackage):
    """bindings for the GLib, and GObject, to be used in Python."""

    homepage = "https://pygobject.readthedocs.io/en/latest/"

    license("LGPL-2.1-or-later")

    version("3.54.3", sha256="a8da09134a0f7d56491cf2412145e35aa74e91d760e8f337096a1cda0b92bae7")
    version("3.54.5", sha256="b6656f6348f5245606cf15ea48c384c7f05156c75ead206c1b246c80a22fb585")
    version(
        "3.46.0",
        sha256="426008b2dad548c9af1c7b03b59df0440fde5c33f38fb5406b103a43d653cafc",
        url="https://download.gnome.org/sources/pygobject/3.46/pygobject-3.46.0.tar.xz",
    )

    depends_on("c", type="build")  # generated

    build_system(
        conditional("python_pip", when="@:3.50.0"),
        conditional("meson", when="@3.50.0:"),
        default="meson",
    )

    extends("python")

    depends_on("py-setuptools", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gtkplus")

    # meson.build
    depends_on("python@3.8:3", type=("build", "run"), when="@3.46.0:")
    depends_on("glib@2.64.0:", when="@3.46.0:")
    depends_on("glib@2.80.0:", when="@3.54:")
    depends_on("py-pycairo@1.16:1", type=("build", "run"), when="@3.46.0:")
    depends_on("libffi@3.0.0:", when="@3.46.0:")

    depends_on("glib", when="@:3.46.0")
    depends_on("gobject-introspection", when="@:3.46.0")
    depends_on("py-pycairo", type=("build", "run"), when="@:3.46.0")
    depends_on("libffi", when="@:3.46.0")

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/pygobject/{version.up_to(2)}/pygobject-{version}.tar.gz"

    def patch(self):
        filter_file(r"Pycairo_IMPORT", r"//Pycairo_IMPORT", "gi/pygi-foreign-cairo.c")
