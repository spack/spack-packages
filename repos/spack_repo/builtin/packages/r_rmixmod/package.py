# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRmixmod(RPackage):
    """Classification with Mixture Modelling

    Interface of 'MIXMOD' software for supervised, unsupervised and
    semi-supervised classification with mixture modelling."""

    homepage = "https://cran.r-project.org/package=Rmixmod"
    cran = "Rmixmod"

    license("GPL-3.0-only", checked_by="V-Karch")

    version("2.1.10", sha256="96d592c36a456ab744b5e885dbbc929e4d1d2a5f4d8489c9c224fe353f0af189")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    depends_on("r@2.12.0:", type=("build", "run"))
    depends_on("r-rcpp@0.8.0:", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
