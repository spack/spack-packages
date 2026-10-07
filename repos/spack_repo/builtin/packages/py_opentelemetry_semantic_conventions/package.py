# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySemanticConventions(PythonPackage):
    """OpenTelemetry Semantic Conventions."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_semantic_conventions/opentelemetry_semantic_conventions-0.62b0.tar.gz"

    version("0.65b0", sha256="f9b2b81e9d5b64f11bc952075e7e9c7fb0aab075c7fd1c46d597f1b919852d60")
    version("0.62b0", sha256="cbfb3c8fc259575cf68a6e1b94083cc35adc4a6b06e8cf431efa0d62606c0097")

    depends_on("python@3.10:", type=("build", "run"), when="@0.630:")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-api@1.44.0", type=("build", "run"), when="@0.65b0")
    depends_on("py-opentelemetry-api@1.41.0", type=("build", "run"), when="@0.62b0")
    depends_on("py-typing-extensions@4.5:", type=("build", "run"))
