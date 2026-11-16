# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyriemann(PythonPackage):
    """Machine learning for multivariate data with Riemannian geometry."""

    homepage = "https://pyriemann.readthedocs.io"
    pypi = "pyriemann/pyriemann-0.12.tar.gz"
    git = "https://github.com/pyRiemann/pyRiemann.git"

    license("BSD-3-Clause")

    version("0.12", sha256="a1450307bf3360fafe4e2e11a5db81889245f34b0042094bf8b59b7fe2bdeb9f")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")

        depends_on("py-numpy@1.25:")
        depends_on("py-scipy")
        depends_on("py-scikit-learn@0.24:")
        depends_on("py-array-api-compat@1.11:")
        depends_on("py-array-api-extra@0.6:")
        depends_on("py-joblib")
        depends_on("py-matplotlib")
