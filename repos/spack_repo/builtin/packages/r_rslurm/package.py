# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RRslurm(RPackage):
    """Submitting of R scripts to the Slurm workload manager."""

    cran = "rslurm"

    license("GPL-3.0")

    version("0.6.2", sha256="540158ece7d838c9630886f37e0960353038fefa4f9cc374004240b767f6b47c")

    depends_on("r@3.5:", type=("build", "run"))

    depends_on("r-whisker@0.3:", type=("build", "run"))
