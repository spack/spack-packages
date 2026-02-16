# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPatchwork(RPackage):
    """The Composer of Plots.

    The 'ggplot2' package provides a strong API for sequentially building up a
    plot, but does not concern itself with composition of multiple plots.
    'patchwork' is a package that expands the API to allow for arbitrarily
    complex composition of plots by, among others, providing mathematical
    operators for combining multiple plots. Other packages that try to address
    this need (but with a different approach) are 'gridExtra' and 'cowplot'."""

    cran = "patchwork"

    license("MIT")

    version("1.3.2", sha256="0ec469acfd69d1a4f1a6317c861e6bf000f768c2d5047e3aed6713df9afe27eb")
    version("1.2.0", sha256="cc31ea13560c424de9bfe2287d926a7d9e6cc8da2d5561402bb145b4f51b68a1")
    version("1.1.2", sha256="dab9d5d2d704d591717eaa6efeacf09cb6cd7bee2ca2c46d18414e8503ac8977")
    version("1.1.1", sha256="cf0d7d9f92945729b499d6e343441c55007d5b371206d5389b9e5154dc7cf481")

    depends_on("r-ggplot2@3.0.0:", type=("build", "run"))
    # https://github.com/thomasp85/patchwork/issues/454#issuecomment-3430577354
    depends_on("r-ggplot2@3.5.2:", type=("build", "run"), when="@1.3.2:")

    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-gtable@0.3.6:", type=("build", "run"), when="@1.3.2:")

    depends_on("r-rlang", type=("build", "run"), when="@1.1.3:")
    depends_on("r-rlang@1.0.0:", type=("build", "run"), when="@1.3.2:")

    depends_on("r-cli", type=("build", "run"), when="@1.1.3:")
    depends_on("r-farver", type=("build", "run"), when="@1.3.2:")
