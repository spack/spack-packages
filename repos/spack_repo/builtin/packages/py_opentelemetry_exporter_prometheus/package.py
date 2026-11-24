# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterPrometheus(PythonPackage):
    """Prometheus Metric Exporter for OpenTelemetry."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_prometheus/opentelemetry_exporter_prometheus-0.62b0.tar.gz"

    version("0.62b0", sha256="4d1106566a9b3e8dff028e69e9f2dc90723e6b431c900ff8c72982fcf11dbae5")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-api@1.12:1", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.41:1", type=("build", "run"))
    depends_on("py-prometheus-client@0.5:0", type=("build", "run"))
