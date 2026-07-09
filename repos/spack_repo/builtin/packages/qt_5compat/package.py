# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.packages.qt_base.package import QtBase, QtPackage

from spack.package import *


class Qt5compat(QtPackage):
    """The Qt5compat module contains unsupported Qt 5 APIs for use in Qt 6 projects."""

    url = QtPackage.get_url(__qualname__)
    list_url = QtPackage.get_list_url(__qualname__)

    maintainers("wdconinc")

    license("LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only")

    version("6.11.1", sha256="2b21eff89b309819e877f39747494c280fb7b13afea8ce68a6793c364ae289a9")
    version("6.10.2", sha256="3468f5ef429361b427a58830791b34ce4ea826583584b4ba9caaa2923002c78c")
    version("6.10.1", sha256="e936870e435dae57f23793f7d3fd92444f7b98e9aa2931eda458e7e11b3f3571")
    version("6.10.0", sha256="4f0c57c96bd5a04a59cc4fd9a6507392d5a5af886f59e8dc7274f2ccfa6d74f4")
    version("6.9.3", sha256="c2b1dc10ddf8372f2d8060f3dd7404ecf02a4f630d03e0f21e3131b4a8e0aa1b")
    version("6.9.2", sha256="49ddd0de9f76b35ef5f9420b024e6c066fd03218da732fb2ec131973db39c3b5")
    version("6.9.1", sha256="14a97fb93c342a6dcfff3bc827c7cdaff4dcb4853135aa7e391aa5df96fd7440")
    version("6.9.0", sha256="7c8fe0709d8efd758a788b1db47294ec1fb33387b11b4765e5ef98606aaa562c")
    version("6.8.3", sha256="67340c9c7a1d2007b593847363342c65570dc9e86edb6315226589dc4533e5ed")
    version("6.8.2", sha256="9b78a025f17d65eb826ee153f167546e6c12790235d75b7f4fcd03c166d9c689")
    version("6.8.1", sha256="5e51feb8d9362d860017ae72f63daa5caeddf3ec3396e73a4b27c672536fd774")
    version("6.8.0", sha256="0ea312a2d7e7033857712273e5ea42e61d1f485d23420307f7bbf0b8ca701453")
    version("6.7.3", sha256="959634d1a6a53f9a483882e81da87ec182ff44d7747a0cc771c786b0f2cf52e0")
    version("6.7.2", sha256="331a1e617952217868beeef7964828500388abeeb502ea3436f16eec816426c4")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("qt-base")

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)
