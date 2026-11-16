# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCoseq(RPackage):
    """Co-Expression Analysis of Sequencing Data

    Co-expression analysis for expression profiles arising from
    high-throughput sequencing data. Feature (e.g., gene) profiles are
    clustered using adapted transformations and mixture models or a K-means
    algorithm, and model selection criteria (to choose an appropriate number
    of clusters) are provided."""

    bioc = "coseq"

    license("GPL-3.0-only", checked_by="V-Karch")

    version("1.36.0", commit="7ba4b17889c8c303853b20cfb507ab80e3ef2c37")

    depends_on("r@4.0.0:", type=("build", "run"))

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-capushe", type=("build", "run"))
    depends_on("r-rmixmod", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-htsfilter", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-htscluster", type=("build", "run"))
    depends_on("r-compositions", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
