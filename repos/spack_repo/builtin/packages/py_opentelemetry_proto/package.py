# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOpentelemetryProto(PythonPackage):
    """OpenTelemetry Python Proto."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_proto/opentelemetry_proto-1.44.0.tar.gz"

    version("1.44.0", sha256="c547a79c2f8c0c515d31509154682e5921c7cfd5ca67b70e1f9266e2c3e103f3")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-protobuf@5:7", type=("build", "run"))
