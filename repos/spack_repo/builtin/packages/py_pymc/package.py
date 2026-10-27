# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymc(PythonPackage):
    """PyMC (formerly PyMC3) is a Python package for Bayesian statistical
    modeling focusing on advanced Markov chain Monte Carlo (MCMC) and
    variational inference (VI) algorithms. Its flexibility and extensibility
    make it applicable to a large suite of problems."""

    homepage = "https://www.pymc.io/"
    pypi = "pymc/pymc-6.3.2.tar.gz"
    git = "https://github.com/pymc-devs/pymc.git"

    license("Apache-2.0")

    version("6.3.2", sha256="3cd58e55249b3650786e2c717078de5595811e17187a666868072d15e3a931a1")
    version(
        "3.8",
        sha256="1bb2915e4a29877c681ead13932b0b7d276f7f496e9c3f09ba96b977c99caf00",
        url="https://files.pythonhosted.org/packages/source/p/pymc3/pymc3-3.8.tar.gz",
    )

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-versioneer+toml@0.29")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:", when="@6:")
        depends_on("python@3.5.4:")

        depends_on("py-arviz@1.1:1", when="@5.28.5:")
        depends_on("py-arviz@0.4.1:")
        depends_on("py-cachetools@4.2.1:6", when="@3.11.2:")
        depends_on("py-cloudpickle", when="@4:")
        depends_on("py-numpy@1.25:", when="@5.19:")
        # numpy 2 support added in pymc 5.21, pymc3 is the legacy package
        # https://github.com/pymc-devs/pymc/pull/7688
        depends_on("py-numpy@1.13.0:1", when="@:3.10")
        depends_on("py-pandas@0.24.0:", when="@3.11:")
        depends_on("py-pandas@0.18.0:")
        depends_on("py-pytensor@3.2.2:3.3", when="@6.3.1:")
        depends_on("py-rich@13.7.1:", when="@5.13:")
        depends_on("py-scipy@1.4.1:", when="@4:")
        depends_on("py-scipy@0.18.1:")
        depends_on("py-threadpoolctl@3.1.0:3", when="@5.15.1:")
        depends_on("py-typing-extensions@3.7.4:", when="@3.9:")

        # Historical dependencies
        with when("@3.8"):
            depends_on("py-h5py@2.7.0:")
            depends_on("py-patsy@0.4.0:")
            depends_on("py-theano@1.0.4:")
            depends_on("py-tqdm@4.8.4:")
