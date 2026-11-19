# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFastapiCloudCli(PythonPackage):
    """Deploy and manage FastAPI Cloud apps from the command line."""

    homepage = "https://github.com/fastapilabs/fastapi-cloud-cli"
    pypi = "fastapi_cloud_cli/fastapi_cloud_cli-0.26.0.tar.gz"

    license("MIT")

    version("0.26.0", sha256="5fd64c26228c8ead803461e8b58ae64ffd586e960d97ab1fc848efac2d9539be")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")
    depends_on("py-typer@0.16.0:", type=("build", "run"))
    depends_on("py-uvicorn@0.17.6:+standard", type=("build", "run"))
    depends_on("py-rignore@0.5.1:", type=("build", "run"))
    depends_on("py-httpx@0.27.0:", type=("build", "run"))
    depends_on("py-rich-toolkit@0.20.5:", type=("build", "run"))
    depends_on("py-sentry-sdk@2.20.0:", type=("build", "run"))
    depends_on("py-fastar@0.10.0:", type=("build", "run"))
    depends_on("py-detect-installer@0.1.0:", type=("build", "run"))
    depends_on("py-agent-detector@1.1.0:", type=("build", "run"))
