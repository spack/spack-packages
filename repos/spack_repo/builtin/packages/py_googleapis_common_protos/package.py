# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGoogleapisCommonProtos(PythonPackage):
    """Common protobufs used in Google APIs."""

    homepage = "https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos"
    pypi = "googleapis_common_protos/googleapis_common_protos-1.70.0.tar.gz"

    license("Apache-2.0")

    version("1.70.0", sha256="0e1b44e0ea153e6594f9f394fef15193a68aaaea2d843f83e2742717ca753257")
    version("1.63.0", sha256="17ad01b11d5f1d0171c06d3ba5c04c54474e883b66b949722b4938ee2694ef4e")
    version("1.58.0", sha256="c727251ec025947d545184ba17e3578840fc3a24a0516a020479edab660457df")
    version("1.56.4", sha256="c25873c47279387cfdcbdafa36149887901d36202cb645a0e4f29686bf6e4417")
    version("1.55.0", sha256="53eb313064738f45d5ac634155ae208e121c963659627b90dfcb61ef514c03e1")

    variant(
        "grpc",
        default=False,
        description="Enable support for gRPC Remote Procedure Call framework.",
    )

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-protobuf@3.22.2:6", when="@1.70:")
        depends_on("py-protobuf@3.19.5:4", when="@1.58:1.63")
        depends_on("py-protobuf@3.15.0:4", when="@1.56:1.57")
        depends_on("py-protobuf@3.12.0:4", when="@1.55")

    conflicts("py-protobuf@4.21.1:4.21.5")

    with when("+grpc"), default_args(type="run"):
        depends_on("py-grpcio@1.44:1")

