# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDerivative(PythonPackage):
    """Numerical differentiation in python."""

    homepage = "https://github.com/andgoldschmidt/derivative"
    pypi = "derivative/derivative-0.6.3.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.6.3", sha256="72e7fd56e92665f939b5449c4b9ceea88fdf02eda7378cf0a3e961ab0df58181")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-poetry-core@1.1.0:", type="build")
    depends_on("py-numpy@1.18.3:", type=("build", "run"))
    depends_on("py-scipy@1.4.1:", type=("build", "run"))
    depends_on("py-scikit-learn@1", type=("build", "run"))
    depends_on("py-importlib-metadata@7.1.0:", type=("build", "run"))
