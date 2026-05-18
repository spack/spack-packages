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
    url = "https://www.greenwoodsoftware.com/less/less-692.tar.gz"
    list_url = "https://www.greenwoodsoftware.com/less/download.html"

    depends_on("ncurses")

    license("GPL-3.0-or-later OR BSD-2-Clause", checked_by="wdconinc")

    depends_on("c", type="build")

    version("692", sha256="61300f603798ecf1d7786570789f0ff3f5a1acf075a6fb9f756837d166e37d14")
    version("668", sha256="2819f55564d86d542abbecafd82ff61e819a3eec967faa36cd3e68f1596a44b8")
    version("661", sha256="2b5f0167216e3ef0ffcb0c31c374e287eb035e4e223d5dae315c2783b6e738ed")
    version("643", sha256="2911b5432c836fa084c8a2e68f6cd6312372c026a58faaa98862731c8b6052e8")
