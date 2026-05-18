# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RUcscUtils(RPackage):
    """A set of low-level utilities to retrieve data from the UCSC Genome Browser.
    Most functions in the package access the data via the UCSC REST API but some of
    them query the UCSC MySQL server directly. Note that the primary purpose of the
    package is to support higher-level functionalities implemented in downstream
    packages like GenomeInfoDb or txdbmaker."""

    bioc = "UCSC.utils"

    license("Artistic-2.0")

    with default_args(get_full_repo=True):
        version("1.6.1", commit="625d5544d0de9cb47ea67364136efc1535c67682")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r-httr")
        depends_on("r-jsonlite")
        depends_on("r-s4vectors@0.47.6:")
