# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RSeqinfo(RPackage):
    """A simple S4 class for storing basic information about a collection of genomic sequences."""

    bioc = "Seqinfo"

    with default_args(get_full_repo=True):
        version("1.2.0", commit="345dd61b77c8ff7e90ecc587d7b32c4d7189f690")  # bioc 3.23
        version("1.0.0", commit="9fc5a613b84efd096416b9810ed62ceef79522cb")  # bioc 3.22

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors@0.47.6:", type=("build", "run"))
