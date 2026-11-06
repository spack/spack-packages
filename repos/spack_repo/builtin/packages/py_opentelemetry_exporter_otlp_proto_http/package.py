# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterOtlpProtoHttp(PythonPackage):
    """OpenTelemetry Collector Protobuf over HTTP Exporter."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_otlp_proto_http/opentelemetry_exporter_otlp_proto_http-1.44.0.tar.gz"

    version("1.44.0", sha256="c633d7270ad6b57cd4cfbe8b0007a9e2e7c0cb50bd6c50fe2a7b245f721a09d8")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-googleapis-common-protos@1.52", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.15", type=("build", "run"))
    depends_on("py-opentelemetry-proto@1.44.0", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.44", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-common@1.44.0", type=("build", "run"))
    depends_on("py-requests@2.7:", type=("build", "run"))  # upstream pins 2.7
    depends_on("py-typing-extensions@4.5:", type=("build", "run"))
