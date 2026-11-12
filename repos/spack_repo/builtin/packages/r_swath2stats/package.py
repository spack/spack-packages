# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSwath2stats(RPackage):
    """Transform and Filter SWATH Data for Statistical Packages."""

    bioc = "SWATH2stats"

    with default_args(get_full_repo=True):
        version("1.42.0", commit="402b2fc59942d5dabcd33717ef209940bb402489")  # bioc 3.23

    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
