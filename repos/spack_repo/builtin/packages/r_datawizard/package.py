# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RDatawizard(RPackage):
    """Easy Data Wrangling and Statistical Transformations."""

    cran = "datawizard"

    license("MIT")

    version("1.5.0", sha256="3493aadb142e7c581597771c96708583b487160afd6e74bbeacec89a28357f4a")

    with default_args(type=("build", "run")):
        depends_on("r@4:")

        depends_on("r-insight@1.5.4:")
