# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPepxmltab(RPackage):
    """pepXMLTab: Parsing pepXML files and filter based on peptide FDR"""

    bioc = "pepXMLTab"

    with default_args(get_full_repo=True):
        version("1.46.0", commit="a49de2215c3801a932d52aae976835b471946ae0")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-xml@3.98-1.1:", type=("build", "run"))
