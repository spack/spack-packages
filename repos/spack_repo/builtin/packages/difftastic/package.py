# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Difftastic(CargoPackage):
    """Difftastic is a structural diff tool that compares files based on their syntax."""

    homepage = "https://difftastic.wilfred.me.uk/"
    url = "https://github.com/Wilfred/difftastic/archive/refs/tags/0.63.0.tar.gz"

    maintainers("alecbcs")

    license("MIT")

    version("0.67.0", sha256="a6a15d6ca9f9ab7c034d1770417d1829deb3fbe9dcf4731b9cba867e50e78437")
    version("0.64.0", sha256="54c7c93309ff9a2cbe87153ac1d16e80bacac4042c80f6b7206e9b71a6f10d0b")
    version("0.63.0", sha256="f96bcf4fc961921d52cd9fe5aa94017924abde3d5a3b5a4727b103e9c2d4b416")

    depends_on("rust@1.76:", type="build", when="@0.67:")
    depends_on("rust@1.75:", type="build", when="@0.65:")
    depends_on("rust@1.74.1:", type="build", when="@0.62:")

    depends_on("gmake", type="build")
