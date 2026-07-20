# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Comet(MakefilePackage):
    """A tandem mass spectrometry (MS/MS) sequence database search tool."""

    homepage = "https://uwpr.github.io/Comet"
    url = "https://github.com/UWPR/Comet/archive/refs/tags/v2026.01.1.tar.gz"
    git = "https://github.com/UWPR/Comet.git"

    maintainers("w8jcik")

    license("Apache-2.0")

    version("2026.01.1", sha256="c444cf8e5b303677c8f8efe4d3141db9bfacba16b28c9e5e35621bd3e8e05c99")
    version("2025.03.0", sha256="7e1b1d9cf19a4af6c9fc3d2a635cb5066775904c7f3b486b7038a947cd6f3ead")
    version("2024.02.0", sha256="57ac30bc2d1a8b53c4eb3ccf7f282bbb36fa96691dacea7a41efa2205c288340")
    version("2023.01.2", sha256="4316230dab89e4cc16776e4c2bb1141b413fd1a347764abf5ce9e9bff522a4ca")
    version("2022.01.1", sha256="07763e6aa4ac166eb3ded38a74f23b26e6eadc0f7024262c052aa63811e84d75")
    version("2022.01.0", sha256="f59f2d8df1ee3a48919244cf107a03197f65b5e0533a96f1d55d35deb8054e94")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    parallel = False

    def edit(self, spec, prefix):
        if spec.satisfies("@2025.02.0:"):
            mstoolkit_makefile = FileFilter("MSToolkit/Makefile")
            mstoolkit_makefile.filter(r"CC = g\+\+", "")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("comet.exe", join_path(prefix.bin, "comet"))
