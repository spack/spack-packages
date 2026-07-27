# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Terminalimageviewer(MakefilePackage):
    """
    Small C++ program to display images in a (modern) terminal
    using RGB ANSI codes and unicode block graphic characters.
    """

    homepage = "https://github.com/stefanhaustein/TerminalImageViewer"
    url = "https://github.com/stefanhaustein/TerminalImageViewer/archive/refs/tags/v1.2.1.tar.gz"

    license("Apache-2.0	OR GPL-3.0-or-later", checked_by="ExplorerRay")

    version("1.2.1", sha256="08d0c30e3ffa47b69d1bce07bea56f04b7deb4a8a79307ce435a4f0852fbcd5f")
    version("1.2", sha256="f9b3c96554a24eccc3b4cdce2ce37fd3bade24a16a2e13038233f3b26a662542")

    depends_on("gcc", type="build")

    depends_on("imagemagick")

    build_directory = "src"

    def edit(self, spec, prefix):
        makefile = FileFilter("src/Makefile")
        makefile.filter(r"prefix *\?=\s*\/usr\/local", f"prefix ?= {prefix}")
