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

    version("2.26.0", sha256="b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb")
    version("0.27.8", sha256="2483095c7db1eee274cebac79e315a986c4e55207bb4fa7b82d185b3a2ed9536")

    variant("datalib", default=False, description="facilities for data loading")
    variant(
        "wandb",
        default=False,
        description="keeps track of hyperparameters, system metrics, and predictions",
        when="@:0"
    )
    variant("embeddings", default=False, description="represents a text string vector", when="@:0")
    variant("voice", default=False, description="library for proceeding sound", when="@1.68.1:")
    variant(
        "aiohttp",
        default=False,
        description="aiohttp backend for improved concurrency performance",
        when="@1.89.0:"
    )
    variant("realtime", default=False, description="support for Realtime API", when="@1.58:")

    depends_on("python@3.7.1:", type=("build", "run"))
    depends_on("python@3.9:", type=("build", "run"), when="@2.7.2:")
    depends_on("py-setuptools", type="build", when="@:0")
    depends_on("py-hatchling@1.26.3", type="build", when="@1:2")
    depends_on("py-hatch-fancy-pypi-readme", type="build", when="@1:2")
    depends_on("py-requests@2.20:", type=("build", "run"), when="@:0")
    depends_on("py-httpx@0.23.0:0", when="@1:")
    depends_on("py-pydantic@1.9.0:2", when="@1:")
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-tqdm@4:", type=("build", "run"), when="@1.40:")
    depends_on("py-typing-extensions", when="^python@3.7", type=("build", "run"))
    depends_on("py-typing-extensions@4.11:4", type=("build", "run"), when="@1.40:")
    depends_on("py-anyio@3.5.0:4", when="@1.3.8:")
    depends_on("py-distro@1.7.0:1", when="@1:")
    depends_on("py-sniffio", type=("build", "run"), when="@1:")
    depends_on("py-jiter@0.10:0", type=("build", "run"), when="@2.3.0:")
    depends_on("py-aiohttp", type=("build", "run"), when="@:0")

    with when("+datalib"):
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-numpy@1:", when="@1:")
        depends_on("py-pandas@1.2.3:", type=("build", "run"))
        depends_on("py-pandas-stubs@1.1.0.11:", type=("build", "run"))
        depends_on("py-openpyxl@3.0.7:", type=("build", "run"), when="@:0")

    with when("+wandb"):
        depends_on("py-wandb", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-pandas@1.2.3:", type=("build", "run"))
        depends_on("py-pandas-stubs@1.1.0.11:", type=("build", "run"))
        depends_on("py-openpyxl@3.0.7:", type=("build", "run"))

    with when("+aiohttp"):
        depends_on("py-aiohttp", type=("build", "run"))
        depends_on("py-httpx-aiohttp@0.1.9:", type=("build", "run"))

    with when("+realtime"):
        depends_on("py-websockets@13:15", type=("build", "run"))

    with when("+voice"):
        depends_on("py-sounddevice@0.5.1:", type=("build", "run"))
        depends_on("py-numpy@2.0.2", type=("build", "run"))

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
