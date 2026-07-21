# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RHypergeo(RPackage):
    """The Gauss Hypergeometric Function.

    The Gaussian hypergeometric function for complex numbers."""

    cran = "hypergeo"

    license("GPL-2.0-only")

    version("1.2-14", sha256="bf379a5d5543ca20b7ac779555f504a3b98f421abadf782676c161426e6570e4")

    depends_on("r@3.1.0:", type=("build", "run"))
    depends_on("r-elliptic@1.3-5:", type=("build", "run"))
    depends_on("r-contfrac@1.1-9:", type=("build", "run"))
    depends_on("r-desolve", type=("build", "run"))
