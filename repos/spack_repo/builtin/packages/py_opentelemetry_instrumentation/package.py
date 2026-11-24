# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryInstrumentation(PythonPackage):
    """Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib"
    pypi = "opentelemetry_instrumentation/opentelemetry_instrumentation-0.62b0.tar.gz"

    version("0.62b0", sha256="aa1b0b9ab2e1722c2a8a5384fb016fc28d30bba51826676c8036074790d2861e")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-packaging@18:", type=("build", "run"))
    depends_on("py-wrapt@1:2", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.4:1", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.62b0", type=("build", "run"))
