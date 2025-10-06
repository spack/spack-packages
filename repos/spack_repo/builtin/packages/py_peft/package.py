# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPeft(PythonPackage):
    """Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of
    pre-trained language models (PLMs) to various downstream applications without
    fine-tuning all the model's parameters."""

    homepage = "https://github.com/huggingface/peft"
    pypi = "peft/peft-0.5.0.tar.gz"

    license("Apache-2.0")

    version("0.5.0", sha256="3cc03049ac6130426d82c22ca54cc6de849e7c6727181393e7751f7f512a9ced")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8.0:", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-packaging@20.0:", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-torch@1.13.0:", type=("build", "run"))
    depends_on("py-transformers", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-accelerate", type=("build", "run"))
    depends_on("py-safetensors", type=("build", "run"))
