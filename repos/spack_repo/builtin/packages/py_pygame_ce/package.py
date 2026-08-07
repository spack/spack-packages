# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPygameCe(PythonPackage):
    """Community Edition of Pygame, a cross-platform Python library for
    developing multimedia applications such as video games."""

    homepage = "https://pyga.me"
    pypi = "pygame-ce/pygame_ce-2.5.7.tar.gz"

    license("LGPL-2.1-or-later")

    version("2.5.7", sha256="86beb797cd73c141299a29b56f7df2b0543fbdc81d428022458329ff694aaa51")

    # pygame-ce 2.5.7 still builds the mixer and MIDI extensions when these
    # features are disabled.
    patch("disable-mixer-midi.patch", when="@2.5.7")

    depends_on("c", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-meson-python@:0.18.0", type="build")
    depends_on("meson@:1.10.0", type="build")
    depends_on("ninja@:1.13.0", type="build")
    depends_on("pkgconf", type="build")
    depends_on("py-cython@:3.2.4", type="build")
    depends_on("py-astroid@:3", type="build")
    depends_on("py-sphinx@:8.2.3", type="build")
    depends_on("py-sphinx-autoapi@:3.6.0", type="build")
    depends_on("py-pyproject-metadata", type="build")
    conflicts("^py-pyproject-metadata@0.9.1")
    depends_on("sdl2", type=("build", "link"))
    depends_on("sdl2-image", type=("build", "link"))
    depends_on("sdl2-ttf", type=("build", "link"))
    depends_on("freetype", type=("build", "link"))

    def config_settings(self, spec, prefix):
        return {
            "setup-args": {
                "-Dmixer": "disabled",
                "-Dmidi": "disabled",
                "-Dstripped": "true",
            }
        }
