# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class Rapidxml(Package, SourceforgePackage):
    """Fast XML parser as a header-only C++ library"""

    homepage = "https://rapidxml.sourceforge.net"
    sourceforge_mirror_path = "rapidxml/rapidxml/rapidxml%201.13/rapidxml-1.13.zip"

    maintainers("dtaller")

    version("1.13", sha256="c3f0b886374981bb20fabcf323d755db4be6dba42064599481da64a85f5b3571")

    license("BSL-1.0", checked_by="rblake-llnl")

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        install("*.hpp", prefix.include)
