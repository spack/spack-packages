# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCigarillo(RPackage):
    """CIGAR stands for Concise Idiosyncratic Gapped Alignment Report. CIGAR
    strings are found in the BAM files produced by most aligners and in the
    AIRR-formatted output produced by IgBLAST. The cigarillo package provides
    functions to parse and inspect CIGAR strings, trim them, turn them into ranges
    of positions relative to the "query space" or "reference space", and project
    positions or sequences from one space to the other. Note that these operations
    are low-level operations that the user rarely needs to perform directly. More
    typically, they are performed behind the scene by higher-level functionality
    implemented in other packages like Bioconductor packages GenomicAlignments and
    igblastr."""

    bioc = "cigarillo"

    license("Artistic-2.0")

    version("1.0.0", commit="8775adf6c85995de7c778f0a0b4311c9c6a82068")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-biocgenerics")
        depends_on("r-s4vectors@0.47.2:")
        depends_on("r-iranges")
        depends_on("r-biostrings")
