# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RXmlparsedata(RPackage):
    """Convert the output of 'utils::getParseData()' to an 'XML' tree, that one can search via
    'XPath', and easier to manipulate in general."""

    cran = "xmlparsedata"

    license("MIT")

    version("1.0.5", sha256="766034ab5e9728609bd240c9954d23ca0cdb881a98a31b9d3e1c8767c7b7cbb0")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3:")
