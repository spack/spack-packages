# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterOtlp(PythonPackage):
    """OpenTelemetry Collector Exporters."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_otlp/opentelemetry_exporter_otlp-1.44.0.tar.gz"

    version("1.44.0", sha256="af1cde7c33ea8ed624bf04ac49a885730fe44c1f1ad698656e592c38f70ce106")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-exporter-otlp-proto-grpc@1.44.0", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-http@1.44.0", type=("build", "run"))
