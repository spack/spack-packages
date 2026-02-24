# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGridpattern(RPackage):
    """Provides 'grid' grobs that fill in a user-defined area with various patterns.
    Includes enhanced versions of the geometric and image-based patterns originally
    contained in the 'ggpattern' package as well as original 'pch', 'polygon_tiling',
    'regular_polygon', 'rose', 'text', 'wave', and 'weave' patterns plus support for
    custom user-defined patterns."""

    cran = "gridpattern"

    license("MIT")

    version("1.3.1", sha256="2e67ff7c4e381a4ce60fbc368d1fd01917503a970f3179641501ccbb7d8acea5")

    depends_on("r-glue", type=("build", "run"))
    depends_on("r-memoise", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-sf", type=("build", "run"))
