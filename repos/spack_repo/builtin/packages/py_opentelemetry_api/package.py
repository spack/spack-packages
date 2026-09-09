# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryApi(PythonPackage):
    """OpenTelemetry Python API."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_api/opentelemetry_api-1.39.1.tar.gz"

    version("1.44.0", sha256="67647e5e9566edcf421166fdf022b3537f818635daa852b289e34604dc6fb33a")
    version("1.41.0", sha256="9421d911326ec12dee8bc933f7839090cad7a3f13fcfb0f9e82f8174dc003c09")
    version("1.39.1", sha256="fbde8c80e1b937a2c61f20347e91c0c18a1940cecf012d62e65a7caf08967c9c")
    version("1.15.0", sha256="79ab791b4aaad27acc3dc3ba01596db5b5aac2ef75c70622c6038051d6c2cded")

    depends_on("python@3.10:", type=("build", "run"), when="@1.42:")
    depends_on("python@3.9:", type=("build", "run"), when="@1.34:")
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-typing-extensions@4.5:", type=("build", "run"), when="@1.34:")
    depends_on("py-importlib-metadata@6:8.7", type=("build", "run"), when="@1.34:1.41")

    # Historical dependencies
    depends_on("py-setuptools@16:", type=("build", "run"), when="@:1.18")
    depends_on("py-deprecated@1.2.6:", type=("build", "run"), when="@:1.33")
