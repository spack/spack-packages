# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymc(PythonPackage):
    """Probabilistic programming in Python."""

    homepage = "https://github.com/pymc-devs/pymc"
    pypi = "pymc/pymc-5.25.1.tar.gz"

    license("Apache-2.0")

    version("5.25.1", sha256="9e739315c0547336b4c11127aae8b3750145b29cdd8e21609196594aa29c21f8")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-versioneer@0.29+toml", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-arviz@0.13:")
        depends_on("py-cachetools@4.2.1:")
        depends_on("py-cloudpickle")
        depends_on("py-numpy@1.25:")
        depends_on("py-pandas@0.24:")
        depends_on("py-pytensor@2.31.7:2.31")
        depends_on("py-rich@13.7.1:")
        depends_on("py-scipy@1.4.1:")
        depends_on("py-threadpoolctl@3.1:3")
        depends_on("py-typing-extensions@3.7.4:")
