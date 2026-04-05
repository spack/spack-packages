# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Cry(MakefilePackage):
    """CRY — Cosmic-RaY shower generator library.

    A library for generating correlated cosmic-ray particle showers.
    """

    homepage = "https://nuclear.llnl.gov/simulation"
    url = "https://nuclear.llnl.gov/simulation/cry_v1.7.tar.gz"

    maintainers("wdconinc")

    version("1.7", sha256="dcee2428f81cba113f82e0c7c42f4d85bff4b8530e5ab5c82c059bed3e570c20")

    depends_on("cxx", type="build")

    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
        install_tree("src", prefix.include.cry)
        install_tree("data", prefix.share.cry.data)
