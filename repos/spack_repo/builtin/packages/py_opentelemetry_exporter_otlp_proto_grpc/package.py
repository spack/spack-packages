# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterOtlpProtoGrpc(PythonPackage):
    """OpenTelemetry Collector Protobuf over gRPC Exporter."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_otlp/opentelemetry_exporter_otlp-1.44.0.tar.gz"

    version("1.44.0", sha256="af1cde7c33ea8ed624bf04ac49a885730fe44c1f1ad698656e592c38f70ce106")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-googleapis-common-protos@1.57", type=("build", "run"))
    depends_on("py-grpcio@1.63.2:1", type=("build", "run"), when="^python@:3.12")
    depends_on("py-grpcio@1.66.2:1", type=("build", "run"), when="^python@3.13")
    depends_on("py-grpcio@1.75.1:1", type=("build", "run"), when="^python@3.14:")
    depends_on("py-opentelemetry-api@1.15", type=("build", "run"))
    depends_on("py-opentelemetry-proto@1.44.0", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.44", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-common@1.44.0", type=("build", "run"))
    depends_on("py-typing-extensions@4.6:", type=("build", "run"))
