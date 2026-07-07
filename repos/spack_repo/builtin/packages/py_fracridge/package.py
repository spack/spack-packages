# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFracridge(PythonPackage):
    """Fractional Ridge Regression."""

    homepage = "https://nrdg.github.io/fracridge"
    pypi = "fracridge/fracridge-1.4.3.tar.gz"
    git = "https://github.com/nrdg/fracridge"

    license("BSD-2-Clause")

    version("3.0", sha256="b9df5c433381bd6e80d7bb5bc384865e03b5b9f6c20e6b252c5e095b2e73fe21")
    version("2.0", sha256="d49fbffbd58e85da38f572e6ca2ef7563b1a6c8c4e1ab779e2dd207ac944db90")

    with default_args(type="build"):
        depends_on("py-setuptools@64:", when="@3:")
        depends_on("py-setuptools@42:")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:", when="@3:")

        depends_on("py-scikit-learn@1.8:", when="@3:")
        depends_on("py-scikit-learn")
        depends_on("py-numba")
        # version restriction for py-setuptools-scm from pyproject.toml
        depends_on("py-setuptools-scm@8:", when="@3:")
        depends_on("py-setuptools-scm+toml@3.4:", when="@2")
        depends_on("pil")
