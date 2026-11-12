# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFastapiCli(PythonPackage):
    """Run and manage FastAPI apps from the command line with FastAPI CLI."""

    homepage = "https://github.com/fastapi/fastapi-cli"
    pypi = "fastapi_cli/fastapi_cli-0.0.32.tar.gz"

    license("MIT")

    version("0.0.32", sha256="38024d2345275e1b37ce8848727a580d84901b570e96b3256d9d36a9a5039424")

    variant("standard", default=False, description="Install standard dependencies")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")
    depends_on("py-typer@0.16.0:", type=("build", "run"))
    depends_on("py-uvicorn@0.15:+standard", type=("build", "run"))
    depends_on("py-rich-toolkit@0.14.8:", type=("build", "run"))
    depends_on("py-tomli@2:", when="^python@:3.10", type=("build", "run"))

    with when("+standard"):
        depends_on("py-uvicorn@0.15:+standard", type=("build", "run"))
        depends_on("py-fastapi-cloud-cli@0.1.1:", type=("build", "run"))
