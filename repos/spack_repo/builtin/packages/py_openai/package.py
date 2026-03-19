# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpenai(PythonPackage):
    """The OpenAI Python library provides convenient access to the OpenAI API
    from applications written in the Python language. It includes a pre-defined
    set of classes for API resources that initialize themselves dynamically from
    API responses which makes it compatible with a wide range of versions of the
    OpenAI API."""

    homepage = "https://github.com/openai/openai-python"
    pypi = "openai/openai-0.27.8.tar.gz"

    tags = ["e4s"]

    license("MIT")

    version("2.29.0", sha256="32d09eb2f661b38d3edd7d7e1a2943d1633f572596febe64c0cd370c86d52bec")
    version("0.27.8", sha256="2483095c7db1eee274cebac79e315a986c4e55207bb4fa7b82d185b3a2ed9536")

    variant("datalib", default=False, description="facilities for data loading")
    variant(
        "wandb",
        default=False,
        description="keeps track of hyperparameters, system metrics, and predictions",
    )
    variant("embeddings", default=False, description="represents a text string vector")

    depends_on("python@3.9:", when="@2.8:", type=("build", "run"))
    depends_on("python@3.8:", when="@1.54:", type=("build", "run"))
    depends_on("python@3.7.1:", type=("build", "run"))
    depends_on("py-hatchling@1.26.3", when="@1.67:", type="build")
    depends_on("py-hatchling", when="@1:", type="build")
    depends_on("py-hatch-fancy-pypi-readme", when="@1:", type="build")

    depends_on("py-httpx@0.23:0", type=("build", "run"))
    depends_on("py-pydantic@1.9:2", type=("build", "run"))
    depends_on("py-typing-extensions@4.11:4", when="@1.40:", type=("build", "run"))
    depends_on("py-typing-extensions@4.7:4", when="@1.6:1.39", type=("build", "run"))
    depends_on("py-typing-extensions@4.5:4", when="@:1.5", type=("build", "run"))
    depends_on("py-anyio@3.5:4", when="@1.4:", type=("build", "run"))
    depends_on("py-anyio@3.5:3", when="@:1.3", type=("build", "run"))
    depends_on("py-distro@1.7:1", when="@1:", type=("build", "run"))
    depends_on("py-sniffio", when="@1.4:", type=("build", "run"))
    depends_on("py-tqdm@5:", when="@1:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-jiter@0.10:0", when="@2.3:", type=("build", "run"))
    depends_on("py-jiter@0.4:0", when="@1.40:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-setuptools", when="@0", type="build")
    depends_on("py-requests@2.20:", when="@0", type=("build", "run"))
    depends_on("py-aiohttp", when="@0", type=("build", "run"))

    with when("+datalib"):
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-pandas@1.2.3:", type=("build", "run"))
        depends_on("py-pandas-stubs@1.1.0.11:", type=("build", "run"))
        depends_on("py-openpyxl@3.0.7:", type=("build", "run"))

    with when("+wandb"):
        depends_on("py-wandb", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-pandas@1.2.3:", type=("build", "run"))
        depends_on("py-pandas-stubs@1.1.0.11:", type=("build", "run"))
        depends_on("py-openpyxl@3.0.7:", type=("build", "run"))

    with when("+embeddings"):
        depends_on("py-scikit-learn@1.0.2:", type=("build", "run"))
        depends_on("py-tenacity@8.0.1:", type=("build", "run"))
        depends_on("py-matplotlib", type=("build", "run"))
        depends_on("py-plotly", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-scipy", type=("build", "run"))
        depends_on("py-pandas@1.2.3:", type=("build", "run"))
        depends_on("py-pandas-stubs@1.1.0.11:", type=("build", "run"))
        depends_on("py-openpyxl@3.0.7:", type=("build", "run"))
