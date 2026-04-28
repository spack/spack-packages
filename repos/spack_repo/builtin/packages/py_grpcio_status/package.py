# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGrpcioStatus(PythonPackage):
    """Status proto mapping for gRPC."""

    homepage = "https://grpc.io/"
    pypi = "grpcio_status/grpcio_status-1.60.1.tar.gz"

    license("Apache-2.0")

    version("1.75.0", sha256="69d5b91be1b8b926f086c1c483519a968c14640773a0ccdd6c04282515dbedf7")
    version("1.62.2", sha256="62e1bfcb02025a1cd73732a2d33672d3e9d0df4d21c12c51e0bbcaf09bab742a")
    version("1.60.1", sha256="61b5aab8989498e8aa142c20b88829ea5d90d18c18c853b9f9e6d407d37bf8b4")
    version("1.56.2", sha256="a046b2c0118df4a5687f4585cca9d3c3bae5c498c4dff055dcb43fb06a1180c8")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-protobuf@6.31.1:6", when="@1.75:")
        depends_on("py-protobuf@4.21.6:")
        for grpcio in ("1.75.0", "1.62.2", "1.60.1", "1.56.2"):
            depends_on(f"py-grpcio@{grpcio}:", when=f"@{grpcio}")
        depends_on("py-googleapis-common-protos@1.5.5:")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/g/grpcio_status/{}-{}.tar.gz"
        if version >= Version("63"):
            name = "grpcio_status"
        else:
            name = "grpcio-status"
        return url.format(name, version)
