# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDocket(PythonPackage):
    """A distributed background task system for Python functions."""

    homepage = "https://github.com/chrisguidry/docket"
    pypi = "pydocket/pydocket-0.16.6.tar.gz"

    license("MIT")

    version("0.16.6", sha256="b96c96ad7692827214ed4ff25fcf941ec38371314db5dcc1ae792b3e9d3a0294")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-cloudpickle@3.1.1:", type=("build", "run"))
    depends_on("py-exceptiongroup@1.2:", when="^python@:3.10", type=("build", "run"))
    depends_on("py-fakeredis@2.32.1: +lua", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.33.0:", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-prometheus@0.60b0:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.60b0:", type=("build", "run"))
    depends_on("py-prometheus-client@0.21.1:", type=("build", "run"))
    depends_on("py-key-value-aio@0.3: +memory +redis", type=("build", "run"))
    depends_on("py-python-json-logger@2.0.7:", type=("build", "run"))
    depends_on("py-redis@5:", type=("build", "run"))
    depends_on("py-rich@13.9.4:", type=("build", "run"))
    depends_on("py-typer@0.15.1:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12:", type=("build", "run"))
