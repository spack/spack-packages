# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class REdger(RPackage):
    """Empirical Analysis of Digital Gene Expression Data in R.

    Differential expression analysis of RNA-seq expression profiles with
    biological replication. Implements a range of statistical methodology
    based on the negative binomial distributions, including empirical Bayes
    estimation, exact tests, generalized linear models and quasi-likelihood
    tests. As well as RNA-seq, it be applied to differential signal analysis
    of other types of genomic data that produce counts, including ChIP-seq,
    Bisulfite-seq, SAGE and CAGE."""

    bioc = "edgeR"

    with default_args(get_full_repo=True):
        version("4.10.1", commit="5a71e43e4c203bf14f0201e9151d4fcfd00e8f0d")  # bioc 3.23
        version("4.8.2", commit="af0343acbb3998d2d2bb3e3d259bbee17a2c8a7e")  # bioc 3.22
        version("4.6.3", commit="0dc836a7c8e53633bb7817d55b27128ceb898ac9")  # bioc 3.21
        version("4.4.2", commit="c87d2400f5da6bf38514e17fc1e4111a66006214")  # bioc 3.20
        version("4.2.2", commit="d50e8020f272abdaf612326bf55a1ef7c2123f22")  # bioc 3.19
        version("4.0.16", commit="1e37a9b4c0660174016925d6294221e9ac9d5ea2")  # bioc 3.18
        version("3.42.4", commit="63d1dc664db2781088f53165e52256aac3967cdc")  # bioc 3.17
        version("3.42.0", commit="197b9a8ccc27016611b262c2c31ca22f991661c5")
        version("3.40.2", commit="ddb1cb9b22c1d27179ea4be7adefd72cc66c4fa7")  # bioc 3.16
        version("3.40.0", commit="0b25adcc6b3cb0a8c641964d1274536ee07ee162")
        version("3.38.4", commit="f5a3bb568a23b34146ac66329a95ee4785093536")
        version("3.38.1", commit="e58bf52f34ec451096f593126922ad7e5d517f7e")
        version("3.36.0", commit="c7db03addfc42138a1901834409c02da9d873026")
        version("3.32.1", commit="b881d801d60e5b38413d27f149384c218621c55a")
        version("3.26.8", commit="836809e043535f2264e5db8b5c0eabcffe85613f")
        version("3.24.3", commit="d1260a2aeba67b9ab7a9b8b197b746814ad0716d")
        version("3.22.5", commit="44461aa0412ef4a0d955730f365e44fc64fe1902")
        version("3.20.9", commit="acbcbbee939f399673678653678cd9cb4917c4dc")
        version("3.18.1", commit="101106f3fdd9e2c45d4a670c88f64c12e97a0495")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@3.6.0:", type=("build", "run"), when="@3.26.8:")
    depends_on("r@2.15.0:", type=("build", "run"))

    depends_on("r-limma@3.63.6:", type=("build", "run"), when="@4.5.6:")
    depends_on("r-limma@3.61.9:", type=("build", "run"), when="@4.3.8:")
    depends_on("r-limma@3.41.5:", type=("build", "run"), when="@3.32.1:")
    depends_on("r-limma@3.34.5:", type=("build", "run"), when="@3.20.9:")
    depends_on("r-limma", type=("build", "run"))

    depends_on("r-locfit", type=("build", "run"))

    depends_on("r-rcpp", type=("build", "run"), when="@3.20.9:4.3.10")
