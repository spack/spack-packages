# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySkorch(PythonPackage):
    """Scikit-learn compatible neural network library for PyTorch."""

    homepage = "https://skorch.readthedocs.io/"
    pypi = "skorch/skorch-1.4.0.tar.gz"

    license("BSD-3-Clause")

    version("1.4.0", sha256="f7a5d3c13a3aecf0a0fe689ff25188be1145a95268f8fe81f01aaa9fbd7cead1")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@61.1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.13.3:")
        depends_on("py-scikit-learn@0.22:")
        depends_on("py-scipy@1.1:")
        depends_on("py-tabulate@0.7.7:")
        depends_on("py-torch@1.1:")
        depends_on("py-tqdm@4.14:")
