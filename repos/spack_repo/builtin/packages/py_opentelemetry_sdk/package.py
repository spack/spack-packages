# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetrySdk(PythonPackage):
    """OpenTelemetry Python SDK"""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_sdk/opentelemetry_sdk-1.34.1.tar.gz"

    maintainers("viperML")

    license("Apache-2.0", checked_by="viperML")

    version("1.34.1", sha256="8091db0d763fcd6098d4781bbc80ff0971f94e260739aa6afe6fd379cdf3aa4d")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-opentelemetry-api@1.34.1", when="@1.34.1")
