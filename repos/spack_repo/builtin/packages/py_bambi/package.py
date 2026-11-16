# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBambi(PythonPackage):
    """BAyesian Model Building Interface in Python."""

    homepage = "https://bambinos.github.io/bambi/"
    pypi = "bambi/bambi-0.21.0.tar.gz"
    git = "https://github.com/bambinos/bambi.git"

    license("MIT")

    version("0.21.0", sha256="68c096406d9426c2d244512b373c2f3b0123a553faf22ddf500b2a2400b60e85")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:")

        depends_on("py-arviz-plots@1")
        depends_on("py-formulae@0.6")
        depends_on("py-graphviz")
        depends_on("py-matplotlib@3.9:")
        depends_on("py-pandas@1:")
        depends_on("py-pytensor@3")
        depends_on("py-pymc@6")
        depends_on("py-seaborn@0.13.2:0.13")
        depends_on("py-sparse@0.17")
