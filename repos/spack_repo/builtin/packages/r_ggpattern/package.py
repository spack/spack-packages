# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGgpattern(RPackage):
    """Provides 'ggplot2' geoms filled with various patterns.
    Includes a patterned version of every 'ggplot2' geom that has a region that can be
    filled with a pattern. Provides a suite of 'ggplot2' aesthetics and scales for
    controlling pattern appearances. Supports over a dozen builtin patterns (every
    pattern implemented by 'gridpattern') as well as allowing custom user-defined patterns.
    """

    cran = "ggpattern"

    license("MIT")

    version("1.2.1", sha256="bf6d4df5636c791b1cb8f4d96ac97cc56f9d7f502088de7116f2f795f4ea5827")

    depends_on("r-cli", type=("build", "run"))
    depends_on("r-ggplot2@3.5.1:", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-gridpattern@1.2.2:", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-rlang@1.1.3:", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
