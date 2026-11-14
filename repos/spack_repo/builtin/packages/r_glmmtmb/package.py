# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGlmmtmb(RPackage):
    """Generalized Linear Mixed Models using Template Model Builder."""

    cran = "glmmTMB"

    license("AGPL-3.0-only")

    version("1.1.15.2", sha256="bee86a0e504a5e42dc6f7e44877ea5081fb0afe50c3a43b041247d6c5339e7d5")

    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3.6:")

        depends_on("r-rtmb")
        depends_on("r-tmb@1.9.23:")
        depends_on("r-lme4@1.1-18.9000:")
        depends_on("r-matrix")
        depends_on("r-nlme")
        depends_on("r-numderiv")
        depends_on("r-mgcv")
        depends_on("r-reformulas@0.4.3.1:")
        depends_on("r-pbkrtest")
        depends_on("r-sandwich")

