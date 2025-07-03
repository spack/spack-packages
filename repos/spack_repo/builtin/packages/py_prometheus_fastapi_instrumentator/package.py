# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPrometheusFastapiInstrumentator(PythonPackage):
    """Instrument your FastAPI with Prometheus metrics."""

    pypi = "prometheus-fastapi-instrumentator/prometheus_fastapi_instrumentator-7.0.0.tar.gz"

    license("MIT")

    version("7.0.0", sha256="5ba67c9212719f244ad7942d75ded80693b26331ee5dfc1e7571e4794a9ccbed")

    depends_on("py-poetry-core", type="build")
    depends_on("py-prometheus-client@0.8.0:1", type=["build", "run"])
    depends_on("py-starlette@0.30.0:1", type=["build", "run"])
