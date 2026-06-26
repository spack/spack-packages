# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class REnsembldb(RPackage):
    """Utilities to create and use Ensembl-based annotation databases.

    The package provides functions to create and use transcript centric
    annotation databases/packages. The annotation for the databases are
    directly fetched from Ensembl using their Perl API. The functionality
    and data is similar to that of the TxDb packages from the
    GenomicFeatures package, but, in addition to retrieve all
    gene/transcript models and annotations from the database, ensembldb
    provides a filter framework allowing to retrieve annotations for
    specific entries like genes encoded on a chromosome region or transcript
    models of lincRNA genes. EnsDb databases built with ensembldb contain
    also protein annotations and mappings between proteins and their
    encoding transcripts. Finally, ensembldb provides functions to map
    between genomic, transcript and protein coordinates."""

    bioc = "ensembldb"

    with default_args(get_full_repo=True):
        version("2.34.0", commit="a13967bb64a7188cb2e54dff9c46df32a8884a6e")
        version("2.24.0", commit="45a79a438fde11b0d244b071e6ae2b652100be03")
        version("2.22.0", commit="4dda178a14e080c643bbd8c4dd6378bfe4e6ee9f")
        version("2.20.2", commit="ac1fb8389efd88099600af298d6bb3384206f9ed")
        version("2.20.1", commit="e547d184730cfe5e65f59e4f3512395fb1cdba1a")
        version("2.18.3", commit="e2fcfc0c7700110df070a171d2d542b37ec098f3")
        version("2.14.0", commit="c7150519ed4ef38e5eac1043209863dbc7be43a1")
        version("2.8.1", commit="a4d8d89c143dca86b364d59dff8e46cc81c41ac0")
        version("2.6.8", commit="c2c4f41b4ecc81d5328ce1d380065dfcb5e0c54c")
        version("2.4.1", commit="b5b6b94826a2f46a4faecb9dde750ecd3bfaf327")
        version("2.2.2", commit="d71610e58aed88dbbe6a74e7a8ddfb7451398060")
        version("2.0.4", commit="514623d71e3cca7a4e547adb579b5a958702ef86")

    with default_args(type=("build", "run")):
        depends_on("r@3.5.0:", when="@2.20.1:")

        depends_on("r-biocgenerics@0.15.10:")

        depends_on("r-genomicranges@1.23.21:")
        depends_on("r-genomicranges@1.31.18:", when="@2.4.1:")
        depends_on("r-genomicranges@1.61.1:", when="@2.34:")

        depends_on("r-genomicfeatures@1.23.18:")
        depends_on("r-genomicfeatures@1.29.10:", when="@2.2.2:")
        depends_on("r-genomicfeatures@1.49.6:", when="@2.22.0:")
        depends_on("r-genomicfeatures@1.61.4:", when="@2.34:")

        depends_on("r-annotationfilter@0.99.7:")
        depends_on("r-annotationfilter@1.1.9:", when="@2.2.2:")
        depends_on("r-annotationfilter@1.5.2:", when="@2.6.8:")

        depends_on("r-rsqlite@1.1:")

        depends_on("r-dbi")

        depends_on("r-biobase")

        depends_on("r-seqinfo", when="@2.34:")
        depends_on("r-genomeinfodb")
        depends_on("r-genomeinfodb@1.45.5:", when="@2.34:")

        depends_on("r-annotationdbi@1.31.19:")

        depends_on("r-rtracklayer")
        depends_on("r-rtracklayer@1.69.1:", when="@2.34:")

        depends_on("r-s4vectors")
        depends_on("r-s4vectors@0.23.10:", when="@2.14.0:")

        depends_on("r-rsamtools")

        depends_on("r-iranges")
        depends_on("r-iranges@2.11.16:", when="@2.2.2:")
        depends_on("r-iranges@2.13.24:", when="@2.4.1:")

        depends_on("r-protgenerics")

        depends_on("r-biostrings")
        depends_on("r-biostrings@2.47.9:", when="@2.4.1:")
        depends_on("r-biostrings@2.77.2:", when="@2.34:")

        depends_on("r-curl")

        # Historical
        depends_on("r-annotationhub", when="@2.0.4:2.2.2")
