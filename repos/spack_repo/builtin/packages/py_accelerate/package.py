# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAccelerate(PythonPackage):
    """A simple way to train and use PyTorch models with multi-GPU, TPU, mixed-precision."""

    homepage = "https://github.com/huggingface/accelerate"
    pypi = "accelerate/accelerate-0.16.0.tar.gz"

    maintainers("meyersbs")

    license("Apache-2.0")

    version("1.12.0", sha256="70988c352feb481887077d2ab845125024b2a137a5090d6d7a32b57d03a45df6")
    version("1.10.1", sha256="3dea89e433420e4bfac0369cae7e36dcd6a56adfcfd38cdda145c6225eab5df8")
    version("0.21.0", sha256="e2959a0bf74d97c0b3c0e036ed96065142a060242281d27970d4c4e34f11ca59")
    version("0.16.0", sha256="d13e30f3e6debfb46cada7b931af85560619b6a6a839d0cafeeab6ed7c6a498d")

    depends_on("python@3.8:", when="@0.21:", type=("build", "run"))
    depends_on("python@3.9:", when="@1.10.1:", type=("build", "run"))
    depends_on("python@3.10:", when="@1.12:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.17:2", when="@:1.10.1", type=("build", "run"))
    depends_on("py-numpy@1.17:", when="@1.12:", type=("build", "run"))

    depends_on("py-packaging@20:", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))

    depends_on("py-torch@1.4:", type=("build", "run"))
    depends_on("py-torch@1.10:", when="@0.21:", type=("build", "run"))
    depends_on("py-torch@2:", when="@1.10.1:", type=("build", "run"))

    depends_on("py-huggingface-hub@0.21:", when="@1.10.1:", type=("build", "run"))
    depends_on("py-safetensors@0.4.3:", when="@1.10.1:", type=("build", "run"))
