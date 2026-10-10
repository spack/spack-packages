# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOnnxIr(PythonPackage):
    """Efficient in-memory representation for ONNX."""

    homepage = "https://onnx.ai/ir-py"
    pypi = "onnx-ir/onnx_ir-1.0.0.tar.gz"
    git = "https://github.com/onnx/ir-py.git"

    license("Apache-2.0")

    version(
        "1.0.0",
        sha256="9e261f25fde8da9612ae5cb43b3b374d5ff469c04af0363cad588b2bb000b812",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-onnx@1.16:")
        depends_on("py-typing-extensions@4.10:")
        depends_on("py-ml-dtypes@0.5:")
        depends_on("py-sympy@1.13:")
