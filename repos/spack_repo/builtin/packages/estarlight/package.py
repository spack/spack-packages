# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Estarlight(CMakePackage):
    """Monte Carlo event generator for coherent vector meson photo- and electro-
    production in electron-ion collisions."""

    homepage = "https://github.com/eic/estarlight"
    url = "https://github.com/eic/estarlight/archive/refs/tags/v1.0.0.zip"
    list_url = "https://github.com/eic/estarlight/tags"
    git = "https://github.com/eic/estarlight.git"

    maintainers("wdconinc")

    version("master", branch="master")
    version("1.2.0", sha256="230e6e02a198b5902f78289f1e7abc53877a09dfaa09b18e5379a17956cd309d")
    version("1.1.0", sha256="86896df9084975685efdf28d421d5bf273c65526be2d4ec24e6fddc94900a8c6")
    version("1.0.3", sha256="c417e5f62faf7983f548a83e3c86cef2cfc72a55f87c0928cd5eb5d38c86d434")
    version("1.0.2", sha256="cf54b833c66a905603a84c4f3132af61c4bfaa239f3e216431150e0fa22da494")
    version("1.0.1", sha256="b43c1dd3663d8f325f30b17dd7cf4b49f2eb8ceeed7319c5aabebec8676279fd")

    variant("dpmjet", default=False, description="Use dpmjet for jets")
    variant("hepmc3", default=False, description="Support HepMC3 writing")
    variant("pythia6", default=False, description="Use Pythia6 for parton showers")
    variant("pythia8", default=False, description="Use Pythia8 for parton showers")

    depends_on("dpmjet", when="+dpmjet")
    depends_on("hepmc3", when="+hepmc3")
    depends_on("pythia6", when="+pythia6")
    depends_on("pythia8", when="+pythia8")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_DPMJET", "dpmjet"),
            self.define_from_variant("ENABLE_HEPMC3", "hepmc3"),
            self.define_from_variant("ENABLE_PYTHIA6", "pythia6"),
            self.define_from_variant("ENABLE_PYTHIA", "pythia8"),
        ]
        return args
