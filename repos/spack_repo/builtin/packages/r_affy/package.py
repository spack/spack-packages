# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAffy(RPackage):
    """Methods for Affymetrix Oligonucleotide Arrays.

    The package contains functions for exploratory oligonucleotide array
    analysis. The dependence on tkWidgets only concerns few convenience
    functions. 'affy' is fully functional without it."""

    bioc = "affy"

    version("1.78.0", commit="cc7eac358b6e10ee86a7a93d2e436758f6fbd9b5")
    version("1.76.0", commit="3bb309388d5d6402c356d4a5270ee83c5b88942f")
    version("1.74.0", commit="2266c4a46eda7e5b64f7f3e17e8b61e7b85579ff")
    version("1.72.0", commit="3750b4eb8e5224b19100f6c881b67e568d8968a2")

    depends_on("c", type="build")  # generated

    depends_on("r-biocgenerics@0.1.12:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-affyio@1.13.3:", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
