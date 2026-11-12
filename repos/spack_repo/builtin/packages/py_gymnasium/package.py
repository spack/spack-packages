# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGymnasium(PythonPackage):
    """A standard API for reinforcement learning and a diverse set of reference
    environments (formerly Gym)."""

    homepage = "https://github.com/Farama-Foundation/Gymnasium"
    pypi = "gymnasium/gymnasium-1.1.1.tar.gz"

    version("1.1.1", sha256="8bd9ea9bdef32c950a444ff36afc785e1d81051ec32d30435058953c20d2456d")

    license("MIT")

    depends_on("py-setuptools@61:", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-cloudpickle@1.2:", type=("build", "run"))
    depends_on("py-importlib-metadata@4.8:", type=("build", "run"), when="^python@:3.9")
    depends_on("py-typing-extensions@4.3:", type=("build", "run"))
    depends_on("py-farama-notifications@0.0.1:", type=("build", "run"))
