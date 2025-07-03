# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySemanticConventions(PythonPackage):
    """OpenTelemetry Semantic Conventions"""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_semantic_conventions/opentelemetry_semantic_conventions-0.55b1.tar.gz"

    maintainers("viperML")

    license("Apache-2.0", checked_by="viperML")

    version("0.55b1", sha256="ef95b1f009159c28d7a7849f5cbc71c4c34c845bb514d66adfdf1b3fff3598b3")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    with default_args(type="run"):
        depends_on("py-opentelemetry-api@1.34.1")
        depends_on("py-typing-extensions@4.5.0:")
