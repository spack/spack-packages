# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGgstats(RPackage):
    """Provides new statistics, new geometries and new positions for
    'ggplot2' and a suite of functions to facilitate the creation of
    statistical plots."""

    homepage = "https://larmarange.github.io/ggstats/"
    cran = "ggstats"

    license("GPL-3.0-or-later", checked_by="wdconinc")

    version("0.13.0", sha256="82dd03ca8dd49baa5567b54a25c749516800574b008d61e63e95efc6c87cd787")
    version("0.6.0", sha256="f80aaa229f542cb18174b9ab82b0026c6bd3331f22bf2662712ab6af480b6d80")

    depends_on("r@4.2:", type=("build", "run"), when="@0.7:")

    depends_on("r-cli", type=("build", "run"))

    depends_on("r-dplyr", type=("build", "run"))

    depends_on("r-forcats", type=("build", "run"))

    depends_on("r-ggplot2@4:", type=("build", "run"), when="@0.11:")
    depends_on("r-ggplot2@3.4:", type=("build", "run"))

    depends_on("r-lifecycle", type=("build", "run"))

    depends_on("r-patchwork", type=("build", "run"))

    depends_on("r-purrr", type=("build", "run"))

    depends_on("r-rlang", type=("build", "run"))

    depends_on("r-scales", type=("build", "run"))

    depends_on("r-stringr", type=("build", "run"))

    depends_on("r-tidyr", type=("build", "run"))

    # Historical dependencies
    conflicts("^r-vctrs@7:", when="@:0.11")
    depends_on("r-broom-helpers@1.14:", type=("build", "run"), when="@:0.6")
    depends_on("r-magrittr", type=("build", "run"), when="@:0.6")
