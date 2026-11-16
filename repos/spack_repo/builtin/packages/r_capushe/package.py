# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCapushe(RPackage):
    """Capushe, Data-Driven Slope Estimation and Dimension Jump

    Calibration of penalized criteria for model selection. The calibration
    methods available in this package are based on the slope heuristics."""

    homepage = "https://cran.r-project.org/package=capushe"
    cran = "capushe"

    license("GPL-2.0-or-later", checked_by="V-Karch")

    version("1.1.3", sha256="3aa40d130d9738d7afff13201824def11ade6588b9e035fe45f3c5eb077349e3")

    depends_on("r-mass", type=("build", "run"))
