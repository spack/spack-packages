# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSeqinfo(RPackage):
    """The Seqinfo class stores the names, lengths, circularity flags, and genomes
    for a particular collection of sequences. These sequences are typically the
    chromosomes and/or scaffolds of a specific genome assembly of a given organism.
    Seqinfo objects are rarely used as standalone objects. Instead, they are used
    as part of higher-level objects to represent their seqinfo() component.
    Examples of such higher-level objects are GRanges, RangedSummarizedExperiment,
    VCF, GAlignments, etc... defined in other Bioconductor infrastructure
    packages."""

    bioc = "Seqinfo"

    license("Artistic-2.0")

    version("1.0.0", commit="9fc5a613b84efd096416b9810ed62ceef79522cb")

    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-s4vectors@0.47.6:")
        depends_on("r-iranges")
