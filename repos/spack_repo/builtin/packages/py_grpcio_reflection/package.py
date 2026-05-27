# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGrpcioReflection(PythonPackage):
    """Standard Protobuf Reflection Service for gRPC."""

    homepage = "https://grpc.io/"
    pypi = "grpcio_reflection/grpcio_reflection-1.78.0.tar.gz"

    version("1.78.0", sha256="e6e60c0b85dbcdf963b4d4d150c0f1d238ba891d805b575c52c0365d07fc0c40")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77.0.1:", type="build")
    depends_on("py-protobuf@6.31.1:6", type=("build", "run"))
    depends_on("py-grpcio@1.78.0", type=("build", "run"))
