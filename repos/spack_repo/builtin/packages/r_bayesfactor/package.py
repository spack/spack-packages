# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBayesfactor(RPackage):
    """Computation of Bayes Factors for Common Designs.

    A suite of functions for computing various Bayes factors for simple designs,
    including contingency tables, one- and two-sample designs, one-way designs,
    general ANOVA designs, and linear regression.
    """

    cran = "BayesFactor"

    license("GPL-2.0-only")

    version(
        "0.9.12-4.7", sha256="f92720697f8dbda248c7977873d582dc802522851647d563c5bcb1cada4e377d"
    )

    depends_on("cxx", type="build")

    depends_on("r@3.2.0:", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-matrix@1.1-1:", type=("build", "run"))
    depends_on("r-rcpp@0.11.2:", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.2.2.0:", type=("build", "run"))

    # build fails without the following dependencies:
    # ERROR: dependencies 'pbapply', 'mvtnorm', 'stringr', 'MatrixModels',
    # 'hypergeo' are not available for package 'BayesFactor'
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-matrixmodels", type=("build", "run"))
    depends_on("r-hypergeo", type=("build", "run"))
