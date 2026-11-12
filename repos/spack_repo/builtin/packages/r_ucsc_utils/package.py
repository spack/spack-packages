# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RUcscUtils(RPackage):
    """Low-level utilities to retrieve data from the UCSC Genome Browser."""

    bioc = "UCSC.utils"

    with default_args(get_full_repo=True):
        version("1.8.0", commit="e02c191d114d0507bd45df4d4bbbb48220383fbe")  # bioc 3.23
        version("1.4.0", commit="8ff250442d482b89dfc6c5c3449218228d6f8b2e")  # bioc 3.21

    depends_on("r-httr", type=("build", "run"))

    depends_on("r-jsonlite", type=("build", "run"))

    depends_on("r-s4vectors@0.47.6:", type=("build", "run"), when="@1.5.1:")
    depends_on("r-s4vectors", type=("build", "run"))
