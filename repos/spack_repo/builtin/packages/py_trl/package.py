# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrl(PythonPackage):
    """trl is a full stack library where we provide a set of tools to train
    transformer language models and stable diffusion models with Reinforcement
    Learning, from the Supervised Fine-tuning step (SFT), Reward Modeling step
    (RM) to the Proximal Policy Optimization (PPO) step."""

    homepage = "https://github.com/huggingface/trl"
    pypi = "trl/trl-0.7.1.tar.gz"

    license("Apache-2.0")

    version("0.23.1", sha256="9a3025a9e7ea18fa4f3a5e575aa16b914d4ea86334b34689216af54562a460c5")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-accelerate@1.4:", type=("build", "run"))
    depends_on("py-datasets@3:", type=("build", "run"))
    depends_on("py-transformers@4.56.1:", type=("build", "run"))
