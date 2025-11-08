# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Geany(AutotoolsPackage):
    """Geany is a powerful, stable and lightweight programmer's text editor
    that provides tons of useful features without bogging down your workflow.
    It runs on Linux, Windows and macOS, is translated into over 40 languages,
    and has built-in support for more than 50 programming languages."""

    homepage = "https://www.geany.org/"
    url = "https://download.geany.org/geany-2.1.tar.bz2"

    maintainers("Markus92")

    license("GPL-2.0-or-later", checked_by="Markus92")

    version("2.1", sha256="6b96a8844463300c10b9692a0a5edad8236eec9e84342f575f83d4fc89331228")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("gtkplus@3.24:")
    depends_on("pango")
    depends_on("glib")
    depends_on("atk")
    # not an official dependency, but it tries linking against it
    depends_on("libxinerama")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")
