# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySemanticConventionsAi(PythonPackage):
    """OpenTelemetry Semantic Conventions Extension for Large Language Models."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = (
        "opentelemetry_semantic_conventions_ai/opentelemetry_semantic_conventions_ai-0.5.1.tar.gz"
    )

    version("0.5.1", sha256="153906200d8c1d2f8e09bd78dbef526916023de85ac3dab35912bfafb69ff04c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-sdk@1.38:", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.59b0:", type=("build", "run"))
