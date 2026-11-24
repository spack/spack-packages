# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTf2onnx(PythonPackage):
    """Tensorflow to ONNX converter"""

    homepage = "https://github.com/onnx/tensorflow-onnx"
    pypi = "tf2onnx/tf2onnx-1.17.0.tar.gz"
    git = "https://github.com/onnx/tensorflow-onnx.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("1.17.0", sha256="998dc1841d5e2405226d985f28287570569034b7609924a52fb297b42462c1c1")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@77:")

    with default_args(type=("build", "run")):
        depends_on("py-tensorflow")
        depends_on("py-numpy@1.23.5:")
        depends_on("py-onnx@1.14.0:")
        depends_on("py-requests")
        depends_on("py-flatbuffers@1.12:")
        depends_on("py-protobuf@3.20:")
