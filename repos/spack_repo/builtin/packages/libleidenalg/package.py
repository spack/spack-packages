# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libleidenalg(CMakePackage):
    """This package implements the Leiden algorithm in C++. It relies on igraph
    for it to function. It is mainly used with the Python Leidenalg package"""

    homepage = "https://github.com/vtraag/libleidenalg/"
    url = "https://github.com/vtraag/libleidenalg/archive/refs/tags/0.10.0.tar.gz"

    maintainers("Markus92")

    license("GPL-3.0-or-later", checked_by="Markus92")

    version("0.10.0", sha256="ae265fb718e2233bfd01e3bc9679d9bed53a182e4cb13dbb12b49e6e92105cc7")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("igraph")
    depends_on("igraph@0.10", when="@0.10:0.11")

    # Cherry-pick Patch for wrong includes
    patch(
        "https://github.com/vtraag/libleidenalg/commit/cfee16027c47318a849deafbead412afd265feb0.patch?full_index=1",
        sha256="f4cb80b7e56502825981768919db8c25238552372d9f414ccaa393c437954bdf",
        when="@:0.10",
    )
