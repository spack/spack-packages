# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Scc(GoPackage):
    """
    Sloc, Cloc and Code: scc is a very fast accurate code counter with
    complexity calculations and COCOMO estimates written in pure Go.
    """

    homepage = "https://github.com/boyter/scc"
    url = "https://github.com/boyter/scc/archive/refs/tags/v3.1.0.tar.gz"
    git = "https://github.com/boyter/scc.git"

    license("MIT")

    version("4.0.0", sha256="7e0418d7b6dfa881b2673e50d32da81e9abc34475a305b612b57600d85801abc")
    version("3.7.0", sha256="447233f70ebcc24f1dafb27b093afdd17d3a1d662de96e8226130c5308b02d01")
    version("3.6.0", sha256="15e09f446ee44f3ebdb59f55933128256588d0343988692f1064b9bfb4f96dd7")
    version("3.5.0", sha256="161f5d9bb359c6440114b7d2e0f98d588c02aa66fbe474d7660b244687fefb70")
    version("3.4.0", sha256="bdedb6f32d1c3d73ac7e55780021c742bc8ed32f6fb878ee3e419f9acc76bdaa")
    version("3.3.2", sha256="2bbfed4cf34bbe50760217b479331cf256285335556a0597645b7250fb603388")
    version("3.1.0", sha256="bffea99c7f178bc48bfba3c64397d53a20a751dfc78221d347aabdce3422fd20")

    depends_on("go@1.20:", type="build", when="@3.2.0:")
    depends_on("go@1.22:", type="build", when="@3.4.0:")
    depends_on("go@1.24:", type="build", when="@3.5.0:")
    depends_on("go@1.25.2:", type="build", when="@3.6.0:")
    depends_on("go@1.26.4:", type="build", when="@4.0.0:")
