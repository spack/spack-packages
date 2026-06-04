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

    version("0.69.0", sha256="49d722fb80a0324ea99fe11907f796cde635443084d15cc6f1afd9e0de54bde0")
    version("0.68.0", sha256="86cfd4232f99c5dac56bd1e6fab7b8d96cfaac7a4271738b50c8189031c97a66")
    version("0.67.0", sha256="a6a15d6ca9f9ab7c034d1770417d1829deb3fbe9dcf4731b9cba867e50e78437")
    version("0.65.0", sha256="59462f69e2cedfdc1bee4fd0da48fe9a7ae635cdb6818c1a300b31c0b146d4b8")
    version("0.64.0", sha256="54c7c93309ff9a2cbe87153ac1d16e80bacac4042c80f6b7206e9b71a6f10d0b")
    version("0.63.0", sha256="f96bcf4fc961921d52cd9fe5aa94017924abde3d5a3b5a4727b103e9c2d4b416")

    depends_on("rust@1.85:", type="build", when="@0.69:")
    depends_on("rust@1.77:", type="build", when="@0.68:")
    depends_on("rust@1.76:", type="build", when="@0.67:")
    depends_on("rust@1.75:", type="build", when="@0.65:")
    depends_on("rust@1.74.1:", type="build", when="@0.62:")

    depends_on("gmake", type="build")
