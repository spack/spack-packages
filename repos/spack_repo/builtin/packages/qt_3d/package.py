# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.qt_base.package import QtBase, QtPackage

from spack.package import *


class Qt3d(QtPackage):
    """Qt 3D provides a fully configurable renderer that enables developers to
    quickly implement any rendering pipeline that they need. Further, Qt 3D
    provides a generic framework for near-realtime simulations beyond
    rendering."""

    url = QtPackage.get_url(__qualname__)
    git = QtPackage.get_git(__qualname__)
    list_url = QtPackage.get_list_url(__qualname__)

    license("LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only", checked_by="melven")

    version("6.11.1", commit="1f4c3a7548201bcad21a273a49060c96ad9ff3a9", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("qt-base +gui +opengl +widgets +network")

    depends_on("gl", type=("build", "link"))
    depends_on("glu", type=("build", "link"))
    # unfortunately, the build process does not seem to pick up this external assimp
    # depends_on("assimp", type=("build", "link"))

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)
