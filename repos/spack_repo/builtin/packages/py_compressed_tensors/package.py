# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCompressedTensors(PythonPackage):
    """Library for utilization of compressed safetensors of neural network models."""

    homepage = "https://github.com/vllm-project/compressed-tensors"
    pypi = "compressed-tensors/compressed-tensors-0.13.0.tar.gz"

    version("0.13.0", sha256="23893824d3498ea3f1a829f14a8fa85f9a5e76a34c711a038b8d7c619ca9a67c")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm@8.2.0", type="build")
    depends_on("py-torch@1.7:", type=("build", "run"))
    depends_on("py-transformers@:4", type=("build", "run"))
    depends_on("py-pydantic@2:", type=("build", "run"))
    depends_on("py-loguru", type=("build", "run"))
