# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZstandard(PythonPackage):
    """Python bindings to the Zstandard (zstd) compression library."""

    homepage = "https://github.com/indygreg/python-zstandard"
    pypi = "zstandard/zstandard-0.22.0.tar.gz"

    license("BSD", checked_by="teaguesterling")

    version("0.25.0", sha256="7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b")
    version("0.24.0", sha256="fe3198b81c00032326342d973e526803f183f97aa9e9a98e3f897ebafe21178f")
    version("0.23.0", sha256="b2d8c62d08e7255f68f7a740bae85b3c9b8e5466baa9cbf7f57f1cde0ac6bc09")
    version("0.22.0", sha256="8226a33c542bcb54cd6bd0a366067b610b41713b64c9abec1bc4533d69f51e70")

    depends_on("python@3.9:", when="@0.24:", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools@77:", when="@0.25:", type="build")
    depends_on("py-setuptools", when="@0.24", type="build")
    depends_on("py-setuptools@:68", when="@:0.23", type="build")
    depends_on("py-wheel@0.41.2", when="@0.22", type="build")
    depends_on("py-packaging", when="@0.24:", type="build")

    depends_on("py-cffi@2:", when="@0.25: ^python@3.14:", type=("build", "run"))
    depends_on("py-cffi@1.17:", when="@0.25: ^python@:3.13", type=("build", "run"))
    depends_on("py-cffi@1.17:", when="@0.24 ^python@3.13:", type=("build", "run"))
    depends_on("py-cffi@1.17:", when="@0.23 ^python@3.13:", type=("build", "run"))
    depends_on("py-cffi@1.16:", when="@0.23 ^python@:3.12", type=("build", "run"))
    depends_on("py-cffi@1.16.0:", when="@0.22", type=("build", "run"))

    depends_on("zstd")
