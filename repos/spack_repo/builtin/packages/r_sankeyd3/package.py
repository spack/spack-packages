# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RSankeyd3(RPackage):
    """Sankey Network Graphs in R and Shiny"""

    homepage = "https://github.com/fbreitwieser/sankeyD3"
    url = "https://github.com/fbreitwieser/sankeyD3/archive/refs/tags/v0.2.tar.gz"

    license("GPL-3.0")

    version("0.2", sha256="5ed925912c835ea45048ee4918722e2dc130bebed39f56f61c3a26b34f530e80")
    version("0.1", sha256="be5ba216fbf637edd456d5594d3401dd39e07a62ff15fb37b91ee1498f0c3468")

    depends_on("r@3.0.0:", type=("build", "run"))
    depends_on("r-d3r", type=("build", "run"))
    depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
