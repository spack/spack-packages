# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySafetensors(PythonPackage):
    """Fast and Safe Tensor serialization."""

    homepage = "https://github.com/huggingface/safetensors"
    pypi = "safetensors/safetensors-0.3.1.tar.gz"

    maintainers("thomas-bouvier")

    version("0.6.2", sha256="43ff2aa0e6fa2dc3ea5524ac7ad93a9839256b8703761e76e2d0b2a3fa4f15d9")
    version("0.4.5", sha256="d73de19682deabb02524b3d5d1f8b3aaba94c72f1bbfc7911b9b9d5d391c0310")
    version("0.4.3", sha256="2f85fc50c4e07a21e95c24e07460fe6f7e2859d0ce88092838352b798ce711c2")
    version("0.3.1", sha256="571da56ff8d0bec8ae54923b621cda98d36dcef10feb36fd492c4d0c2cd0e869")

    depends_on("c", type="build")

    depends_on("python@3.9:", when="@0.6:", type=("build", "run"))
    # Build errors with python@3.14
    depends_on("python@3.7:3.13", when="@:0.4.5", type=("build", "run"))
    # Based on PyPI wheel availability
    depends_on("python@3.7:3.12", when="@:0.4.3", type=("build", "run"))
    depends_on("py-maturin@1", type="build", when="@0.4.3:")

    # Historical dependencies
    depends_on("py-setuptools", when="@0.3.1", type="build")
    depends_on("py-setuptools-rust", when="@0.3.1", type="build")
