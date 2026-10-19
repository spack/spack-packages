# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArvizStats(PythonPackage):
    """Statistical computation and diagnostics for ArviZ."""

    homepage = "https://arviz-stats.readthedocs.io/"
    pypi = "arviz_stats/arviz_stats-1.3.2.tar.gz"
    git = "https://github.com/arviz-devs/arviz-stats.git"

    license("Apache-2.0")

    version("1.3.2", sha256="7b8296f4416757e706b829273d5391c97f4dd52702bc279059dfca0fe90681fd")

    variant("xarray", default=False, description="Build with xarray support")

    with default_args(type="build"):
        depends_on("py-flit-core@3.4:3")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:")

        depends_on("py-numpy@2:")
        depends_on("py-scipy@1.13:")

        with when("+xarray"):
            depends_on("py-arviz-base@1.3")
            depends_on("py-xarray-einstats")
            depends_on("py-xarray@2024.11.0:")
