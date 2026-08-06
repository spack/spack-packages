# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOmegaconf(PythonPackage):
    """A hierarchical configuration system, with support for merging configurations from
    multiple sources (YAML config files, dataclasses/objects and CLI arguments)
    providing a consistent API regardless of how the configuration was created.
    """

    homepage = "https://github.com/omry/omegaconf"
    pypi = "omegaconf/omegaconf-2.3.1.tar.gz"

    maintainers("calebrob6")

    license("BSD-3-Clause")

    version("2.3.1", sha256="e5e7de64aeebeddaf8e6d3f7a783b32ac2a01c0fbd9c878012caecb891a1f42a")
    version("2.3.0", sha256="d5d4b6d29955cc50ad50c46dc269bcd92c6e00f5f90d23ab5fee7bfca4ba4cc7")
    version("2.2.2", sha256="65c85b2a84669a570c70f2df00de3cebcd9b47a8587d3c53b1aa5766bb096f77")
    with default_args(deprecated=True):
        version("2.1.0", sha256="a08aec03a63c66449b550b85d70238f4dee9c6c4a0541d6a98845dcfeb12439d")

    # https://github.com/omry/omegaconf/releases#release-v2.1.0
    conflicts("python@3.10:", when="@:2.1", msg="Use Omegaconf >= 2.2.2 for Python 3.10 and newer")

    # https://github.com/omry/omegaconf/releases#release-v2.3.0
    conflicts("python@3.11:", when="@:2.2", msg="Use Omegaconf >= 2.3.x for Python 3.11 and newer")

    with default_args(type="build"):
        depends_on("py-setuptools@59.6:")
        depends_on("py-setuptools@59.6:80", when="@:2.3.0")
        depends_on("py-pytest-runner", when="@2.1")
        depends_on("java")

    depends_on("py-antlr4-python3-runtime@4.9", when="@2.2.2:", type=("build", "run"))
    depends_on("py-antlr4-python3-runtime@4.8", when="@2.1", type=("build", "run"))
    depends_on("py-pyyaml@5.1:", type=("build", "run"))
