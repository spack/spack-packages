# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStableBaselines3(PythonPackage):
    """Pytorch version of Stable Baselines, implementations of reinforcement learning algorithms."""

    homepage = "https://github.com/DLR-RM/stable-baselines3"
    pypi = "stable_baselines3/stable_baselines3-2.9.0.tar.gz"

    license("MIT")

    version("2.9.0", sha256="92b46c6099a0e8f99163ff09e26729e4d0a68b33dc8598626ca13ade3c0b3a61")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-gymnasium@0.29.1:1", type=("build", "run"))
    depends_on("py-numpy@1.20:2", type=("build", "run"))
    depends_on("py-torch@2.8:2", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
