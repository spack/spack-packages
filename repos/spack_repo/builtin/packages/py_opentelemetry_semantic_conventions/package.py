# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySemanticConventions(PythonPackage):
    """OpenTelemetry Semantic Conventions."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_semantic_conventions/opentelemetry_semantic_conventions-0.62b0.tar.gz"

    version("0.62b0", sha256="cbfb3c8fc259575cf68a6e1b94083cc35adc4a6b06e8cf431efa0d62606c0097")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-api@1.41.0", type=("build", "run"))
    depends_on("py-typing-extensions@4.5:", type=("build", "run"))
