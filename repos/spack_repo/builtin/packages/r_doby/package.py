# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RDoby(RPackage):
    """Groupwise Statistics, LSmeans, Linear Estimates, Utilities.

    Utility package containing: 1) Facilities for working with grouped data:
        'do' something to data stratified 'by' some variables. 2) LSmeans
        (least-squares means), general linear estimates. 3) Restrict functions
        to a smaller domain. 4) Miscellaneous other utilities."""

    cran = "doBy"

    version("4.7.1", sha256="a6d9b14e3b4f907addbe7461a39bab2c0efda6b78ee6b91372908cfaf87b827b")
    version("4.6.22", sha256="2aa7e236de98af73de54a46214ceac50fdf69d90b12bb37f2779a501f40b0b0d")
    version("4.6.16", sha256="d5937eb57d293b0bc2e581ff2e1e628671cb4eacddc0b9574dc28a5316ecbbe7")

    with default_args(type=("build", "run")):
        depends_on("r@4.2.0:", when="@4.6.21:")
        depends_on("r@4.1.0:", when="@4.6.18:")
        depends_on("r@3.6.0:")
        depends_on("r-boot", when="@4.6.21:")
        depends_on("r-broom")
        depends_on("r-cowplot", when="@4.6.21:")
        depends_on("r-deriv")
        depends_on("r-dplyr")
        depends_on("r-forecast", when="@4.7.1:")
        depends_on("r-ggplot2")
        depends_on("r-mass")
        depends_on("r-matrix")
        depends_on("r-modelr", when="@4.6.21:")
        depends_on("r-microbenchmark")
        depends_on("r-rlang", when="@4.6.21:")
        depends_on("r-purrr", when="@4.7.1:")
        depends_on("r-tibble")
        depends_on("r-tidyr", when="@4.6.21:")

        # Historical dependencies
        depends_on("r-magrittr", when="@:4.6.20")
        depends_on("r-pbkrtest@0.4-8.1:", when="@:4.6.21")
