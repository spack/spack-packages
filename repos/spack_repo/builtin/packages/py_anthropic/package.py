# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAnthropic(PythonPackage):
    """The official Python library for the anthropic API."""

    homepage = "https://github.com/anthropics/anthropic-sdk-python"
    pypi = "anthropic/anthropic-0.85.0.tar.gz"

    version("0.85.0", sha256="d45b2f38a1efb1a5d15515a426b272179a0d18783efa2bb4c3925fa773eb50b9")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling@1.26.3", type="build")
    depends_on("py-hatch-fancy-pypi-readme", type="build")
    depends_on("py-httpx@0.25:0", type=("build", "run"))
    depends_on("py-pydantic@1.9:2", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:4", type=("build", "run"))
    depends_on("py-anyio@3.5:4", type=("build", "run"))
    depends_on("py-distro@1.7:1", type=("build", "run"))
    depends_on("py-sniffio", type=("build", "run"))
    depends_on("py-jiter@0.4:0", type=("build", "run"))
    depends_on("py-docstring-parser@0.15:0", type=("build", "run"))
