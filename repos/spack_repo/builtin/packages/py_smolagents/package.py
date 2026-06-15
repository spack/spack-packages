# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySmolagents(PythonPackage):
    """A barebones library for agents. Agents write python code to call tools or orchestrate
    other agents."""

    homepage = "https://huggingface.co/docs/smolagents"
    git = "https://github.com/huggingface/smolagents.git"
    pypi = "smolagents/smolagents-1.26.0.tar.gz"

    license("Apache-2.0")

    maintainers("thomas-bouvier")

    version("1.26.0", sha256="4ec92313265f9cfbcabfc88e192b4bc4505f8475dc5f33dc872062fc567037bd")

    variant("torch", default=True, description="Add Torch support.")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-huggingface-hub@0.31.2:", type=("build", "run"))
    depends_on("py-requests@2.32.3:", type=("build", "run"))
    depends_on("py-rich@13.9.4:", type=("build", "run"))
    depends_on("py-jinja2@3.1.4:", type=("build", "run"))
    depends_on("py-pillow@10.0.1:", type=("build", "run"))
    depends_on("py-python-dotenv", type=("build", "run"))

    with when("+torch"):
        depends_on("py-torch", type=("build", "run"))
        depends_on("py-torchvision", type=("build", "run"))
        depends_on("py-numpy@1.21.2:", type=("build", "run"))
