# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryApi(PythonPackage):
    """OpenTelemetry Python API."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_api/opentelemetry_api-1.39.1.tar.gz"

    version("1.41.0", sha256="9421d911326ec12dee8bc933f7839090cad7a3f13fcfb0f9e82f8174dc003c09")
    version("1.39.1", sha256="fbde8c80e1b937a2c61f20347e91c0c18a1940cecf012d62e65a7caf08967c9c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-typing-extensions@4.5:", type=("build", "run"))
    depends_on("py-importlib-metadata@6:8.7", type=("build", "run"))
