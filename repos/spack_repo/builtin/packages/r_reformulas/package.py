# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RReformulas(RPackage):
    """Machinery for Processing Random Effect Formulas

    Takes formulas including random-effects components (formatted as in
    'lme4', 'glmmTMB', etc.) and processes them. Includes various helper
    functions."""

    cran = "reformulas"

    license("GPL-3.0-or-later")

    version("0.4.1", sha256="60c585ef8791d3f3f8d0c6eeac83fabcf1f21960a6ad1abd2b756603c603f0de")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
