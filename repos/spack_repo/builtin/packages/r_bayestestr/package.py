# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RBayestestr(RPackage):
    """Understand and Describe Bayesian Models and Posterior Distributions."""

    cran = "bayestestR"

    license("GPL-3.0-only")

    version("0.20.0", sha256="0071a3e8ac99db84d81a3aaf45e6b61e13e9a7097610febc235713359f212b36")

    with default_args(type=("build", "run")):
        depends_on("r@3.6:")

        depends_on("r-insight@1.5.4:")
        depends_on("r-datawizard@1.4:")
