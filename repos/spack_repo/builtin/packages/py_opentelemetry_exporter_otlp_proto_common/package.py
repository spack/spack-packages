# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterOtlpProtoCommon(PythonPackage):
    """OpenTelemetry Protobuf encoding."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_otlp_proto_common/opentelemetry_exporter_otlp_proto_common-1.44.0.tar.gz"

    version("1.44.0", sha256="dc87a5a5bc58f149a56d1547e4691588fa12994cdc3bc039a694ccb3375862ac")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-opentelemetry-proto@1.44.0", type=("build", "run"))
