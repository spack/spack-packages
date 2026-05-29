# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySdk(PythonPackage):
    """OpenTelemetry Python SDK."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_sdk/opentelemetry_sdk-1.41.0.tar.gz"

    version("1.41.0", sha256="7bddf3961131b318fc2d158947971a8e37e38b1cd23470cfb72b624e7cc108bd")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-opentelemetry-api@1.41.0", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.62b0", type=("build", "run"))
    depends_on("py-typing-extensions@4.5:", type=("build", "run"))
