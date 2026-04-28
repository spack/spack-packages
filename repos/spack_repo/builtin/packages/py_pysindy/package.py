# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPysindy(PythonPackage):
    """Sparse Identification of Nonlinear Dynamics"""

    homepage = "https://github.com/dynamicslab/pysindy"
    pypi = "pysindy/pysindy-2.0.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("2.0.0", sha256="a619980319d48ef0bfb364cfdf3a00f8ec585d69d32b92980bf79e89c43cf392")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-scikit-learn@1.1:", type=("build", "run"))
    depends_on("py-numpy@2:", type=("build", "run"))
    depends_on("py-derivative@0.6.2:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))

    conflicts("^py-scikit-learn@1.5.0")
    conflicts("^py-scikit-learn@1.6.0")
    conflicts("^py-scikit-learn@1.7.1")
