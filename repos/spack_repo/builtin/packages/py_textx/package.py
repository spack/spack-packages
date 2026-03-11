# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTextx(PythonPackage):
    """Meta-language for DSL implementation inspired by Xtext."""

    homepage = "https://textx.github.io/textX/"
    pypi = "textx/textx-4.0.1.tar.gz"

    license("MIT")

    version("4.3.0", sha256="0facac8029ad124ef21e5838dd8eb67f10129efcee96ea3548f5fd62428a9880")
    version("4.2.3", sha256="5c503fe335b24bc113c21cf20bfec9a174680cf95bb651dea8f90c27d305d4c8")
    version("4.2.2", sha256="62a84bfe6b956c3f3d221d34bd9c133268db0af16e35197a48932b17e9413ede")
    version("4.2.1", sha256="5dbeed35de960ef32364523fcda25472db6fa32e3377e0e71aee03ef12519c31")
    version("4.2.0", sha256="953fdd495195a26ca7af6fb1eeadd7ecf927f0a9d3821716f782c957c5b0e2ab")
    version("4.1.0", sha256="37b4f0c455452e27cc0f13d40777b5d20549eaa871311b26e2ed83c019456692")
    version("4.0.1", sha256="84aff5c95fd2c947402fcbe83eeeddc23aabcfed3464ab84184ef193c52d831a")

    depends_on("c", type="build")
    depends_on("py-flit-core@3.8:3", type="build")
    depends_on("python@3.8:3.12", type=("build", "run"), when="@:4.0.1")
    depends_on("python@3.8:", type=("build", "run"), when="@4.1.0:")
    depends_on("py-arpeggio@2:", type=("build", "run"))
    depends_on("py-importlib-metadata", when="^python@:3.9", type=("build", "run"))
