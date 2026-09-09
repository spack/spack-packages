# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyModelHostingContainerStandards(PythonPackage):
    """Model Hosting Container Standards."""

    homepage = "https://github.com/aws/model-hosting-container-standards"
    pypi = "model_hosting_container_standards/model_hosting_container_standards-0.1.13.tar.gz"

    version("0.1.16", sha256="d34589633900e53c3ee5f7c78280a7cf7e4f6532c35e763341a262fc85cbe84a")
    version("0.1.13", sha256="27a1333410dde2719286a300a2803e24fdde407baa91894eb845c0f268aa194d")

    depends_on("c", type="build")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-poetry-core@2", type="build")
    depends_on("py-fastapi", type=("build", "run"))
    depends_on("py-starlette@0.49.1:", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-jmespath", type=("build", "run"))
    depends_on("py-httpx", type=("build", "run"))
    depends_on("py-supervisor@4.2:", type=("build", "run"))
