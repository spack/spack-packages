# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGage(RPackage):
    """Generally Applicable Gene-set Enrichment for Pathway Analysis."""

    bioc = "gage"

    with default_args(get_full_repo=True):
        version("2.62.0", commit="aaad820da493193b0258850156d2421ae24919e7")  # bioc 3.23
        version("2.58.0", commit="a5f163f25570e94e236636273bd388c4071c7dfc")  # bioc 3.21

    depends_on("r@2.10:", type=("build", "run"))

    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
