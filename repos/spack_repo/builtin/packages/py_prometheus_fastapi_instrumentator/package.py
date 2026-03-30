# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPrometheusFastapiInstrumentator(PythonPackage):
    """Instrument your FastAPI app with Prometheus metrics."""

    homepage = "https://github.com/trallnag/prometheus-fastapi-instrumentator"
    pypi = "prometheus_fastapi_instrumentator/prometheus_fastapi_instrumentator-7.1.0.tar.gz"

    version("7.1.0", sha256="be7cd61eeea4e5912aeccb4261c6631b3f227d8924542d79eaf5af3f439cbe5e")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-poetry-core@2:", type="build")
    depends_on("py-starlette@0.30:0", type=("build", "run"))
    depends_on("py-prometheus-client@0.8:0", type=("build", "run"))
