# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRots(RPackage):
    """Reproducibility-Optimized Test Statistic.

    Calculates the Reproducibility-Optimized Test Statistic (ROTS) for
    differential testing in omics data."""

    bioc = "ROTS"

    with default_args(get_full_repo=True):
        version("2.4.0", commit="a2b50206bab429a357ec81854c6a8226a78ceaba")  # bioc 3.23
        version("2.0.0", commit="d7e5c3989e56f46d80a43826d2e1e1c9d5cd80a5")  # bioc 3.21
        version("1.28.0", commit="032cb97ed6fe303758856c669a4f63fb9e43d124")  # bioc 3.17
        version("1.26.0", commit="8bb45fe78779583ae4d30cf0dc3af0d8de405fdf")  # bioc 3.16
        version("1.24.0", commit="372e4623b39f585d4196d21164436c1ba013173f")  # bioc 3.15
        version("1.22.0", commit="a53ec77c40ed3b3c84e91d794c1602dd509cad83")
        version("1.18.0", commit="1d4e206a8ce68d5a1417ff51c26174ed9d0ba7d2")
        version("1.12.0", commit="7e2c96fd8fd36710321498745f24cc6b59ac02f0")
        version("1.10.1", commit="1733d3f868cef4d81af6edfc102221d80793937b")
        version("1.8.0", commit="02e3c6455bb1afe7c4cc59ad6d4d8bae7b01428b")
        version("1.6.0", commit="3567ac1142ba97770b701ee8e5f9e3e6c781bd56")
        version("1.4.0", commit="2e656514a4bf5a837ee6e14ce9b28a61dab955e7")

    depends_on("cxx", type="build")

    depends_on("r@3.6:", type=("build", "run"), when="@1.99.7:")
    depends_on("r@3.3:", type=("build", "run"))

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"), when="@1.35:")
    depends_on("r-lme4", type=("build", "run"), when="@1.35:")
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"), when="@2.3.3:")
