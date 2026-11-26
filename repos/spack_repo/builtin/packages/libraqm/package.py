# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libraqm(MesonPackage):
    """Raqm provides a convenient API for the logic of complex text layout."""

    homepage = "https://github.com/HOST-Oman/libraqm"
    url = "https://github.com/HOST-Oman/libraqm/releases/download/v0.9.0/raqm-0.9.0.tar.xz"
    git = "https://github.com/HOST-Oman/libraqm.git"

    license("MIT")

    version("0.11.0", sha256="3d0add115f7d4a9410d3377462ed3c05e86342193ef984183e4380e3787b2d4c")
    version("0.10.5", sha256="563053e724892a7b037913110ea2daef50ad575d4fa9f7c368ae1e4515f5e856")
    version("0.9.0", sha256="9ed6fdf41da6391fc9bf7038662cbe412c330aa6eb22b19704af2258e448107c")

    variant(
        "bidi_algo",
        default="fribidi",
        description="Unicode Bidirectional Algorithm",
        values=("fribidi", "sheenbidi"),
        multi=False,
    )

    depends_on("c", type="build")

    depends_on("freetype@2.11:")
    depends_on("harfbuzz")

    depends_on("fribidi@1.0.6:", when="bidi_algo=fribidi")
    # 2.6 does not provide dependency-discovery integration to find sheenbidi
    # but 2.9 introduced both CMake package support and pkg-config support
    depends_on("sheenbidi@2.9:", when="bidi_algo=sheenbidi")

    def meson_args(self):
        if self.spec.variants["bidi_algo"].value == "sheenbidi":
            return ["-Dsheenbidi=true"]
        else:
            return ["-Dsheenbidi=false"]
