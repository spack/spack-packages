# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RPerformance(RPackage):
    """Assessment of Regression Models Performance."""

    cran = "performance"

    license("GPL-3.0-only")

    version("0.19.0", sha256="83a32c6b263709a9bf0a59012f13b6e1ca25b93026864bf1f58b0b538ebde175")

    with default_args(type=("build", "run")):
        depends_on("r@4:")

        depends_on("r-bayestestr@0.19:")
        depends_on("r-insight@1.5.4:")
        depends_on("r-datawizard@1.4:")
