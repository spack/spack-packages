# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCummerbund(RPackage):
    """Allows for persistent storage, access, exploration, and manipulation of
    Cufflinks high-throughput sequencing data. In addition, provides numerous
    plotting functions for commonly used visualizations."""

    bioc = "cummeRbund"

    license("Artistic-2.0")

    version("2.51.0", commit="e87a6c2090fef5b06f4b6234d46fc217978157e5")

    with default_args(type=("build", "run")):
        depends_on("r@2.7:")
        depends_on("r-biocgenerics@0.3.2:")
        depends_on("r-rsqlite")
        depends_on("r-ggplot2")
        depends_on("r-reshape2")
        depends_on("r-fastcluster")
        depends_on("r-rtracklayer")
        depends_on("r-gviz")
        depends_on("r-plyr")
        depends_on("r-s4vectors@0.9.25:")
        depends_on("r-biobase")
