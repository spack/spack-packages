# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RShinywidgets(RPackage):
    """This package provide custom widgets and other components to enhance your shiny
    applications."""

    homepage = "https://github.com/dreamRs/shinyWidgets"
    url = "https://github.com/dreamRs/shinyWidgets/archive/refs/tags/v0.9.0.tar.gz"

    license("GPL-3.0")

    version("0.9.0", sha256="0e45af8670f9c885a07e3c4064d40e20ca6ddce67ac5a335a5173b9addbf263d")
    version("0.8.7", sha256="eeb30b5afcd0b3dbbb35aa0a833867692b396d747a0833a14eb6106ba4f0bc67")
    version("0.8.6", sha256="b3eb931a3d13b412a4ec7b7e6c08595168dd4f8477bb5ae77f0e74b55738ac1d")
    version("0.8.5", sha256="3f8e3391fea5aa5ea36a001479a5084981211c9c505e90224f551e7c261b0212")
    version("0.8.4", sha256="1d5817e883b9589f34beddc9e7692836e993d3a0d62d1540bb8c434241d617ae")
    version("0.8.3", sha256="67d2e52fba66fb2ff16b51e0209e82bcb391d1f1b5532d8827d9b4d0ae1f8b1a")
    version("0.8.2", sha256="586edf6b4fcea2f282abd93f37a7c3628dc59d28292845118e81ff08edb100f8")
    version("0.8.1", sha256="0844f76c12db3105dc447668631692b87a10eeee4ab86ee02a5a4ffadc103540")
    version("0.8.0", sha256="31547ce1aca72743e0e76cc07eec648724e2ba2fbf90897c3c611f49c871f68d")
    version("0.7.6", sha256="637a10bd3ffabc4f82a19556aafb0d2778b13cdd66e84e5b7384c5c6eb94be1c")

    depends_on("r@3.1.0:", type=("build", "run"))
    depends_on("r-anytime", type=("build", "run"), when="@0.7.6:0.8.6")
    depends_on("r-bslib", type=("build", "run"))
    depends_on("r-sass", type=("build", "run"))
    depends_on("r-shiny@1.6.0:", type=("build", "run"))
    depends_on("r-htmltools@0.5.1:", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
