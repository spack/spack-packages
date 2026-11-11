# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRhandsontable(RPackage):
    """An R interface to the 'Handsontable' JavaScript library, which is a
    minimalist Excel-like data grid editor."""

    homepage = "http://jrowen.github.io/rhandsontable/"
    cran = "rhandsontable"

    license("MIT")

    version("0.3.8", sha256="901ed9c59936f7fa52ad8db3111c8904ab962f9c74f1b6cd40f81683af35d21d")

    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-htmlwidgets@0.3.3:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
