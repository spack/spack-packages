# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySsmSimulators(PythonPackage):
    """SSMS is a package collecting simulators and training data generators
    for cognitive science, neuroscience, and approximate bayesian
    computation."""

    homepage = "https://github.com/lnccbrown/ssm-simulators"
    pypi = "ssm_simulators/ssm_simulators-0.14.0.tar.gz"

    license("MIT")

    version("0.14.0", sha256="521d260491ba894a57945518bf362919888ea482188b0082839ce0c0aa17a840")

    with default_args(type="build"):
        depends_on("cxx")

        depends_on("py-setuptools")
        depends_on("py-cython@0.29.23:")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:3.14")

        depends_on("py-scipy@1.6.3:")
        depends_on("py-pandas@1:")
        depends_on("py-matplotlib")
        depends_on("py-scikit-learn@0.24:")
        depends_on("py-psutil@5:")
        depends_on("py-pathos@0.3:")
        depends_on("py-numpy@2:")
        depends_on("py-typer@0.15.3:")
        depends_on("py-pyyaml@6.0.2:")
        depends_on("py-tqdm@4.67.1:")
        depends_on("py-cloudpickle")
