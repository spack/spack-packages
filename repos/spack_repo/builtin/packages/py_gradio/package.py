# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGradio(PythonPackage):
    """Python library for easily interacting with trained machine learning models"""

    homepage = "https://github.com/gradio-app/gradio"
    pypi = "gradio/gradio-3.36.1.tar.gz"

    license("Apache-2.0")

    version("5.1.0", sha256="d2153668e6de2df7a01bb33f01a074fc7716ec863c40f472d8e439439ef1e153")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-requirements-txt", type="build")
    depends_on("py-hatch-fancy-pypi-readme@22.5.0:", type="build")
    depends_on("py-aiofiles", type=("build", "run"))
    depends_on("py-aiohttp", type=("build", "run"))
    depends_on("py-altair@4.2.0:", type=("build", "run"))
    depends_on("py-fastapi", type=("build", "run"))
    depends_on("py-ffmpy", type=("build", "run"))
    depends_on("py-gradio-client@0.2.7:", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-huggingface-hub@0.14.0:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-markdown-it-py@2.0.0:+linkify", type=("build", "run"))
    depends_on("py-pygments@2.12.0:", type=("build", "run"))
    depends_on("py-mdit-py-plugins@:0.3.3", type=("build", "run"))
    depends_on("py-markupsafe", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-orjson", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("pil", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-python-multipart", type=("build", "run"))
    depends_on("py-pydub", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-semantic-version", type=("build", "run"))
    depends_on("py-uvicorn@0.14.0:", type=("build", "run"))
    depends_on("py-websockets@10.0:", type=("build", "run"))
