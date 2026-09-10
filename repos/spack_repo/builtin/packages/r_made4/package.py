# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RMade4(RPackage):
    """Multivariate analysis of microarray data using ADE4"""

    bioc = "made4"

    with default_args(get_full_repo=True):
        version("1.86.0", commit="e95e18a3e90a95f49c864ccfcce7250bd55ef41f")  # bioc 3.23
        version("1.82.0", commit="af8e708e74dff93eee6e67c9c2d73e7941be783f")  # bioc 3.21

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))

    depends_on("r-ade4", type=("build", "run"))
