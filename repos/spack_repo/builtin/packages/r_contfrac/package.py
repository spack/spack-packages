# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RContfrac(RPackage):
    """Continued Fractions.

    Various utilities for evaluating continued fractions.
    """

    cran = "contfrac"

    license("GPL-2.0-only")

    version("1.1-12", sha256="95bfc5e970513416c080486a1cd8dfd9f8d59fb691b02ef6ccbe0ce1ed61056b")

    depends_on("c", type="build")
