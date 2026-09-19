# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFormulae(PythonPackage):
    """Formulas for mixed-effects models in Python."""

    homepage = "https://bambinos.github.io/formulae"
    pypi = "formulae/formulae-0.7.0.tar.gz"
    git = "https://github.com/bambinos/formulae.git"

    license("MIT", checked_by="github_user1")

    version("0.7.0", sha256="c4b644adced7ae0627fc13fc8413b547e3477c2d046ed4704146ec7024ae6081")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.16:")
        depends_on("py-packaging")
        depends_on("py-pandas@1:")
        depends_on("py-scipy@1.5.4:")
