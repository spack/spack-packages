# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RLmertest(RPackage):
    """Tests in Linear Mixed Effects Models.

    Provides p-values in type I, II or III anova and summary tables for lmer
    model fits (cf. lme4) via Satterthwaite's degrees of freedom method. A
    Kenward-Roger method is also available via the pbkrtest package. Model
    selection methods include step, drop1 and anova-like tables for random
    effects (ranova). Methods for Least-Square means (LS-means) and tests of
    linear contrasts of fixed effects are also available."""

    cran = "lmerTest"

    version("3.2-1", sha256="a0c5e6958940824fe09fc595383548e65ff08d3e363f4940e84a51084c025968")
    version("3.1-3", sha256="35aa75e9f5f2871398ff56a482b013e6828135ef04916ced7d1d7e35257ea8fd")

    with default_args(type=("build", "run")):
        depends_on("r@3.2.5:")

        depends_on("r-lme4@1.1-10:")
        depends_on("r-numderiv")
        depends_on("r-mass")
        depends_on("r-ggplot2")
        depends_on("r-reformulas", when="@3.2:")
