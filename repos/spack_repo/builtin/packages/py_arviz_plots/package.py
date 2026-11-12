# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArvizPlots(PythonPackage):
    """ArviZ-plots provides ready to use and composable plots for Bayesian
    Workflow."""

    homepage = "https://github.com/arviz-devs/arviz-plots"
    pypi = "arviz_plots/arviz_plots-1.3.1.tar.gz"

    license("Apache-2.0")

    version("1.3.1", sha256="0d17cbb98754ecce4484552dce7bd43cf5b040d6135a4e7b02383a50d817f1ae")

    with default_args(type="build"):
        depends_on("py-flit-core@3.4:3")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:")

        depends_on("py-arviz-base@1.3")
        depends_on("py-arviz-stats+xarray@1.3")
