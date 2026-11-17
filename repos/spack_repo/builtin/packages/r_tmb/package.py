# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RTmb(RPackage):
    """Template Model Builder: A General Random Effect Tool Inspired by 'ADMB'."""

    cran = "TMB"

    license("GPL-2.0-only")

    version("1.9.25", sha256="cf9663b29949cd5eaccb32e11900c9e07caec7d6ac4f17cfd938317dc33acff2")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

    with default_args(type=("build", "run")):
        depends_on("r@3:")

        depends_on("r-matrix@1.0.12:")
        depends_on("r-rcppeigen")
