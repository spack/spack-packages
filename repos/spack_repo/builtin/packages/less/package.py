# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Less(AutotoolsPackage):
    """The less utility is a text file browser that resembles more, but
    has more capabilities.  Less allows you to move backwards in the
    file aswell as forwards."""

    homepage = "https://www.greenwoodsoftware.com/less/"
    url = "https://www.greenwoodsoftware.com/less/less-551.zip"
    list_url = "https://www.greenwoodsoftware.com/less/download.html"

    depends_on("ncurses")

    license("GPL-3.0-or-later OR BSD-2-Clause", checked_by="wdconinc")

    depends_on("c", type="build")

    version("668", sha256="dbc0de59ea9c50e1e8927e6b077858db3a84954e767909bc599e6e6f602c5717")
    version("661", sha256="a900e3916738bf8c1a0a2a059810f1c59b8271ac8bb46898c6e921ea6aefd757")
    version("643", sha256="3bb417c4b909dfcb0adafc371ab87f0b22e8b15f463ec299d156c495fc9aa196")
