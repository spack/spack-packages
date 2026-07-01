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
        version("1.84.0", commit="34e97a7f79ecaa16d65ac2060413d4b5dbcd583f")  # bioc 3.22
        version("1.82.0", commit="af8e708e74dff93eee6e67c9c2d73e7941be783f")  # bioc 3.21
        version("1.80.0", commit="3db6e0c36d353732ce857203f77ee4414c57c26c")  # bioc 3.20
        version("1.78.0", commit="981e55a052f8809f524b9069c7125dc29d79efb4")  # bioc 3.19
        version("1.76.0", commit="4fa62322cf560d2720055f48c1dcf46f5bc5d745")  # bioc 3.18
        version("1.74.0", commit="d5b34b546d47e42523c61afc4c77e3b8c2c0f479")  # bioc 3.17
        version("1.72.0", commit="4f008b4fdcd1cdbda818b81ffa9efceaaf6a823e")  # bioc 3.16

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))

    depends_on("r-ade4", type=("build", "run"))
