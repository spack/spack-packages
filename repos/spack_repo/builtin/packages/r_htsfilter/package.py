# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RHtsfilter(RPackage):
    """Filter replicated high-throughput transcriptome sequencing data

    This package implements a filtering procedure for replicated
    transcriptome sequencing data based on a global Jaccard similarity index
    in order to identify genes with low, constant levels of expression across
    one or more experimental conditions."""

    bioc = "HTSFilter"

    license("Artistic-2.0", checked_by="V-Karch")

    version("1.52.0", commit="40d85430756cfae72e7fc0ece7e8029266e784c6")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
