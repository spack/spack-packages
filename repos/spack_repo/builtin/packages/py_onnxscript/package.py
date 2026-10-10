# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOnnxscript(PythonPackage):
    """Naturally author ONNX functions and models using a subset of Python.

    Required by torch.onnx.export(..., dynamo=True), the default exporter
    since PyTorch 2.9."""

    homepage = "https://microsoft.github.io/onnxscript/"
    pypi = "onnxscript/onnxscript-0.7.2.tar.gz"
    git = "https://github.com/microsoft/onnxscript.git"

    license("MIT")

    version(
        "0.7.2",
        sha256="2c664f6383d10f332a4d47b2876dcab16dba84909fe703656b19abc281fda165",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@70:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-ml-dtypes")
        depends_on("py-numpy")
        depends_on("py-onnx-ir@0.1.16:1")
        depends_on("py-onnx@1.17:")
        depends_on("py-packaging")
        depends_on("py-typing-extensions@4.10:")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Otherwise setup.py appends a ".dev<date>" suffix to the version
        env.set("ONNX_SCRIPT_RELEASE", "1")
