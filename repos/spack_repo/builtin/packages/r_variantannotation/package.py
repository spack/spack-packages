# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RVariantannotation(RPackage):
    """Annotation of Genetic Variants.

    Annotate variants, compute amino acid coding changes, predict coding
    outcomes."""

    bioc = "VariantAnnotation"

    with default_args(get_full_repo=True):
        version("1.56.0", commit="dc8ecd11b893fdebfa561bca78205d909ce354a3")
        version("1.46.0", commit="80d43e024bead5afd48cb86910ba4670d8d37424")
        version("1.44.0", commit="2e7e0a3b7c1918c0d64170dc7c173a636d3764f4")
        version("1.42.1", commit="d1121696c76c189d6b4df9914806bf585a495845")
        version("1.40.0", commit="50ead7cb60cedf3c053853fab92d9f104f9f85bd")
        version("1.36.0", commit="9918bd19a2e6f89e5edc5fe03c8812f500bb3e19")
        version("1.30.1", commit="fb1ab00872570afb280522c4663e347dafc07a9e")
        version("1.28.13", commit="0393347b8ce2d5edf1a61589be93e6a93eda3419")
        version("1.26.1", commit="60ae67598cc3d7ed20ee6417920f8c209085faaf")
        version("1.24.5", commit="468d7f53fd743e04c9af853d58e871b4cc13a090")
        version("1.22.3", commit="3a91b6d4297aa416d5f056dec6f8925eb1a8eaee")

    depends_on("c", type="build")  # generated

    with default_args(type=("build", "run")):
        depends_on("r@2.8.0:")
        depends_on("r@4.0.0:", when="@1.40.0:")

        depends_on("r-biocgenerics@0.15.3:")
        depends_on("r-biocgenerics@0.37.0:", when="@1.40.0:")

        depends_on("r-matrixgenerics", when="@1.36.0:")

        depends_on("r-seqinfo", when="@1.56:")

        depends_on("r-genomicranges@1.27.6:")
        depends_on("r-genomicranges@1.31.8:", when="@1.26.1:")
        depends_on("r-genomicranges@1.41.5:", when="@1.36.0:")
        depends_on("r-genomicranges@1.61.1:", when="@1.56:")

        depends_on("r-summarizedexperiment@1.5.3:")
        depends_on("r-summarizedexperiment@1.19.5:", when="@1.36.0:")
        depends_on("r-summarizedexperiment@1.39.1:", when="@1.56:")

        depends_on("r-rsamtools@1.23.10:")
        depends_on("r-rsamtools@1.31.2:", when="@1.26.1:")
        depends_on("r-rsamtools@1.33.6:", when="@1.28.13:")
        depends_on("r-rsamtools@1.99.0:", when="@1.30.1:")
        depends_on("r-rsamtools@2.25.1:", when="@1.56:")

        depends_on("r-dbi")

        depends_on("r-biobase")

        depends_on("r-s4vectors@0.13.13:")
        depends_on("r-s4vectors@0.17.24:", when="@1.26.1:")
        depends_on("r-s4vectors@0.27.12:", when="@1.36.0:")

        depends_on("r-iranges@2.3.25:")
        depends_on("r-iranges@2.13.13:", when="@1.26.1:")
        depends_on("r-iranges@2.23.9:", when="@1.36.0:")

        depends_on("r-xvector@0.5.6:")
        depends_on("r-xvector@0.19.7:", when="@1.26.1:")
        depends_on("r-xvector@0.29.2:", when="@1.36.0:")

        depends_on("r-biostrings@2.33.5:")
        depends_on("r-biostrings@2.47.6:", when="@1.26.1:")
        depends_on("r-biostrings@2.57.2:", when="@1.36.0:")
        depends_on("r-biostrings@2.77.2:", when="@1.56:")

        depends_on("r-annotationdbi@1.27.9:")

        depends_on("r-rtracklayer@1.25.16:")
        depends_on("r-rtracklayer@1.39.7:", when="@1.26.1:")
        depends_on("r-rtracklayer@1.69.1:", when="@1.56:")

        depends_on("r-bsgenome@1.37.6:")
        depends_on("r-bsgenome@1.47.3:", when="@1.26.1:")
        depends_on("r-bsgenome@1.77.1:", when="@1.56:")

        depends_on("r-genomicfeatures@1.27.4:")
        depends_on("r-genomicfeatures@1.31.3:", when="@1.26.1:")
        depends_on("r-genomicfeatures@1.61.4:", when="@1.56:")

        depends_on("r-curl", when="@1.56:")

        depends_on("gmake", type="build")

        # Historical
        depends_on("r-genomeinfodb@1.11.4:", when="@:1.46.0")
        depends_on("r-genomeinfodb@1.15.2:", when="@1.26.1:1.46.0")
        depends_on("r-zlibbioc", when="@:1.46.0")
        depends_on("r-rhtslib", when="@1.30.1:1.46.0")
        depends_on("r-rhtslib@1.99.3:", when="@1.44.0:1.46.0")

    # Not listed but needed
    depends_on("curl")
