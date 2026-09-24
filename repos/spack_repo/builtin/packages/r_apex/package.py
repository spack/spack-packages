# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RApex(RPackage):
    """Toolkit for the analysis of multiple gene data (Jombart et al. 2017)
    <doi:10.1111/1755-0998.12567>. 'apex' implements the new S4 classes
    'multidna', 'multiphyDat' and associated methods to handle aligned DNA
    sequences from multiple genes."""

    cran = "apex"

    license("GPL-2.0-or-later")

    version("1.0.7", sha256="cb1ded385ce3a68f5f560a9af2e469944fc6a8715ebb19ed389775e4899dd446")

    with default_args(type=("build", "run")):
        depends_on("r@3.1.3:")

        depends_on("r-ape")
        depends_on("r-phangorn")
        depends_on("r-adegenet")
