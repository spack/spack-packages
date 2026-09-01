# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyStableBaselines3(PythonPackage):
    """PyTorch version of Stable Baselines, implementations of reinforcement
    learning algorithms."""

    homepage = "https://github.com/DLR-RM/stable-baselines3"
    pypi = "stable_baselines3/stable_baselines3-2.9.0.tar.gz"

    license("MIT")

    version("2.9.0", sha256="92b46c6099a0e8f99163ff09e26729e4d0a68b33dc8598626ca13ade3c0b3a61")

    variant("extra", default=False, description="Enable optional features and dependencies")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-gymnasium@0.29.1:1", type=("build", "run"))
    depends_on("py-numpy@1.20:2", type=("build", "run"))
    depends_on("py-torch@2.8:2", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))

    with when("+extra"):
        depends_on("py-opencv-python", type=("build", "run"))
        depends_on("py-pygame-ce", type=("build", "run"))
        depends_on("py-tensorboard@2.9.1:", type=("build", "run"))
        depends_on("py-psutil", type=("build", "run"))
        depends_on("py-tqdm", type=("build", "run"))
        depends_on("py-rich", type=("build", "run"))
        depends_on("py-ale-py@0.9.0:", type=("build", "run"))
        depends_on("py-pillow", type=("build", "run"))
        depends_on("py-pandas", type=("build", "run"))
        depends_on("py-matplotlib", type=("build", "run"))
