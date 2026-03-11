# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScikitOptimize(PythonPackage):
    """Scikit-Optimize, or skopt, is a simple and efficient library to
    minimize (very) expensive and noisy black-box functions. It implements
    several methods for sequential model-based optimization. skopt aims to
    be accessible and easy to use in many contexts.

    The library is built on top of NumPy, SciPy and Scikit-Learn."""

    homepage = "https://scikit-optimize.readthedocs.io"
    pypi = "scikit-optimize/scikit_optimize-0.10.2.tar.gz"
    git = "https://github.com/holgern/scikit-optimize.git"

    maintainers("liuyangzhuan")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("0.10.2", sha256="00a3d91bf9015e292b6e7aaefe7e6cb95e8d25ce19adafd2cd88849e1a0b0da0")
    version("0.9.0", sha256="77d8c9e64947fc9f5cc05bbc6aed7b8a9907871ae26fe11997fd67be90f26008")
    version("0.5.2", sha256="1d7657a4b8ef9aa6d81e49b369c677c584e83269f11710557741d3b3f8fa0a75")
    variant("plots", default=True, description="Build with plot support from py-matplotlib")

    depends_on("py-setuptools@61.2:", when="@0.10.2:", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.20.3:", when="@0.10.2:", type=("build", "run"))
    depends_on("py-numpy@1.13.3:", when="@0.9:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy@1.1.0:", when="@0.10.2:", type=("build", "run"))
    depends_on("py-scipy@0.19.1:", when="@0.9:", type=("build", "run"))
    depends_on("py-scipy@0.14:", type=("build", "run"))
    depends_on("py-scikit-learn@1.0.0:", when="@0.10.2:", type=("build", "run"))
    depends_on("py-scikit-learn@0.20:", when="@0.9:", type=("build", "run"))
    depends_on("py-scikit-learn@0.19.1:", type=("build", "run"))
    depends_on("py-pyaml@16.9:", when="@0.9:", type=("build", "run"))
    depends_on("py-joblib@0.11:", when="@0.9:", type=("build", "run"))

    depends_on("py-matplotlib", when="+plots")
    depends_on("py-matplotlib@2:", when="@0.9:+plots")

    def url_for_version(self, version):
        url = "https://pypi.org/packages/source/s/scikit-optimize/scikit{}optimize-{}.tar.gz"
        if version < Version("0.10.2"):
            separator = "-"
        else:
            separator = "_"
        return url.format(separator, version)
