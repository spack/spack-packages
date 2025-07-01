# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyOpentelemetryApi(PythonPackage):
    """OpenTelemetry Python API"""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_api/opentelemetry_api-1.34.1.tar.gz"

    maintainers("viperML")

    license("Apache-2.0", checked_by="viperML")

    version("1.34.1", sha256="64f0bd06d42824843731d05beea88d4d4b6ae59f9fe347ff7dfa2cc14233bbb3")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4.5.0:")
        # Requires <8.8.0, but @8 is not yet on Spack
        depends_on("py-importlib-metadata@6:8")
