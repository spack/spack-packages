# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryExporterPrometheus(PythonPackage):
    """Prometheus Metric Exporter for OpenTelemetry"""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_exporter_prometheus/opentelemetry_exporter_prometheus-0.55b1.tar.gz"

    maintainers("viperML")

    license("Apache-2.0", checked_by="viperML")

    version("0.55b1", sha256="d13ec0b22bf394113ff1ada5da98133a4b051779b803dae183188e26c4bd9ee0")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    with default_args(type="run"):
        depends_on("py-opentelemetry-api@1.34.1")
        depends_on("py-opentelemetry-sdk@1.34.1")
        depends_on("py-prometheus-client@0.5.0:0")
