# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RHtscluster(RPackage):
    """Clustering High-Throughput Transcriptome Sequencing (HTS) Data

    A Poisson mixture model is implemented to cluster genes from
    high-throughput transcriptome sequencing (RNA-seq) data. Parameter
    estimation is performed using either the EM or CEM algorithm, and the
    slope heuristics are used for model selection (i.e., to choose the number
    of clusters)."""

    homepage = "https://cran.r-project.org/package=HTSCluster"
    cran = "HTSCluster"

    license("GPL-3.0-or-later", checked_by="V-Karch")

    version("2.0.11", sha256="77dd865197c859a3f47f68f5786fa0e24ce06a73ef9801e76c7425453d843a75")

    depends_on("r@2.10.0:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-capushe", type=("build", "run"))
