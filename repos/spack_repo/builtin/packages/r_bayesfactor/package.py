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
        "0.9.12-4.8", sha256="becd30201d6ce57dc1fd742e17881c09a253d5c7ee4c1b5b7b6cae8496326213"
    )
    version(
        "0.9.12-4.7", sha256="f92720697f8dbda248c7977873d582dc802522851647d563c5bcb1cada4e377d"
    )

    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3.2.0:")
        depends_on("r-coda")
        depends_on("r-matrix@1.1-1:")

        depends_on("r-pbapply")
        depends_on("r-mvtnorm")
        depends_on("r-stringr")
        depends_on("r-matrixmodels")
        depends_on("r-rcpp@1.1.1:", when="@0.9.12-4.8:")
        depends_on("r-rcpp@0.11.2:")
        depends_on("r-hypergeo")
        depends_on("r-rcppeigen@0.3.2.2.0:")
