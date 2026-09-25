# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArviz(PythonPackage):
    """ArviZ (pronounced "AR-vees") is a Python package for exploratory
    analysis of Bayesian models. Includes functions for posterior analysis,
    model checking, comparison and diagnostics."""

    homepage = "https://github.com/arviz-devs/arviz"
    pypi = "arviz/arviz-0.6.1.tar.gz"

    license("Apache-2.0")

    version("0.21.0", sha256="ad5c99b998b750e585bdd1f3ba11e3f8729e01d06dc7fdc251450039e88cfd71")
    version("0.6.1", sha256="435edf8db49c41a8fa198f959e7581063006c49a4efdef4755bb778db6fd4f72")

    depends_on("py-setuptools", type="build")

    with when("@:0.6"):
        with default_args(type=("build", "run")):
            depends_on("py-matplotlib@3.0:")
            depends_on("py-netcdf4")
            depends_on("py-numpy@1.12:")
            depends_on("py-packaging")
            depends_on("py-pandas@0.23:")
            depends_on("py-scipy@0.19:")
            depends_on("py-xarray@0.11:")

    with when("@0.21:"):
        depends_on("python@3.10:", type=("build", "run"))
        depends_on("py-setuptools@60:", type=("build", "run"))

        with default_args(type=("build", "run")):
            depends_on("py-h5netcdf@1.0.2:")
            depends_on("py-matplotlib@3.5:")
            depends_on("py-numpy@1.23:")
            depends_on("py-packaging")
            depends_on("py-pandas@1.5:")
            depends_on("py-scipy@1.9:")
            depends_on("py-typing-extensions@4.1:")
            depends_on("py-xarray@2022.6:")
            depends_on("py-xarray-einstats@0.3:")
