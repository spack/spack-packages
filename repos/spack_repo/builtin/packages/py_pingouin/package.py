# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPingouin(PythonPackage):
    """Pingouin: statistical package for Python."""

    homepage = "https://pingouin-stats.org/index.html"
    pypi = "pingouin/pingouin-0.7.0.tar.gz"
    git = "https://github.com/raphaelvallat/pingouin.git"

    license("GPL-3.0-or-later")

    version("0.7.0", sha256="19d180d2fe9663ec91908f3bf6c81cef32564f55c34aa186ad5b2cd9cad33ee3")

    with default_args(type="build"):
        depends_on("py-setuptools@80:")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")

        depends_on("py-matplotlib@3.10.1:")
        depends_on("py-numpy@2.2.2:")
        depends_on("py-pandas@2.3:")
        depends_on("py-pandas-flavor")
        depends_on("py-scikit-learn@1.6.1:")
        depends_on("py-scipy@1.15:")
        depends_on("py-seaborn@0.13.2:")
        depends_on("py-statsmodels@0.14.5:")
        depends_on("py-tabulate")
