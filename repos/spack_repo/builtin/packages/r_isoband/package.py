# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RIsoband(RPackage):
    """Generate Isolines and Isobands from Regularly Spaced Elevation Grids.

    A fast C++ implementation to generate contour lines (isolines) and contour
    polygons (isobands) from regularly spaced grids containing elevation
    data."""

    cran = "isoband"

    license("MIT")

    version("0.3.0", sha256="fe8d3d58ca75bbee32f389152ac0058818f3f76f09c9867949531de7abc424ac")
    version("0.2.7", sha256="7693223343b45b86de2b5b638ff148f0dafa6d7b1237e822c5272902f79cdf61")
    version("0.2.6", sha256="27e460945753f6710649563dc817e2f314392ef6d1f8b6af2b1bf9447fab43a3")
    version("0.2.5", sha256="46f53fa066f0966f02cb2bf050190c0d5e950dab2cdf565feb63fc092c886ba5")
    version("0.2.3", sha256="f9d3318fdf6d147dc2e2c7015ea7de42a55fa33d6232b952f982df96066b7ffe")

    depends_on("cxx", type="build")  # generated

    with default_args(type=("build", "run")):
        depends_on("r-cpp11", when="@0.3:")

        # additional dependencies to prevent
        # ERROR: dependencies 'cli', 'rlang' are not available for package 'isoband'
        depends_on("r-cli", when="@0.3:")
        depends_on("r-rlang", when="@0.3:")

        # Historical dependencies
        depends_on("r-testthat", when="@0.2.3")
