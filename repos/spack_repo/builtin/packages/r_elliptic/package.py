# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RElliptic(RPackage):
    """Weierstrass and Jacobi Elliptic Functions.

    A suite of elliptic and related functions including Weierstrass and Jacobi
    forms. Also includes various tools for manipulating and visualizing complex
    functions.
    """

    cran = "elliptic"

    license("GPL-2.0-only")

    version("1.5-1", sha256="e6ecfddf7a1a2c6e40889e42f5a7e2e5693a99359d190dda6fdceb2bf93bc901")

    depends_on("r@2.5.0:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
