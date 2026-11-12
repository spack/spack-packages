# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySpglib(PythonPackage):
    """Python bindings for C library for finding and handling
    crystal symmetries."""

    homepage = "https://spglib.readthedocs.io/en/latest/"
    pypi = "spglib/spglib-1.9.9.18.tar.gz"
    git = "https://github.com/spglib/spglib.git"

    license("BSD-3-Clause")

    version("2.7.0", sha256="c40907a42c9dc45572f46740bf95412f84fb0eda30267e31665d104a4bde6627")
    version("2.0.2", sha256="1d081ec22da4ab4fc3198e9445ddad6dec2261c43927831151d93e39422610aa")
    version("1.16.1", sha256="9fd2fefbd83993b135877a69c498d8ddcf20a9980562b65b800cfb4cdadad003")
    version("1.9.9.18", sha256="cbbb8383320b500dc6100b83d5e914a26a97ef8fc97c82d8921b10220e4126cd")

    depends_on("c", type="build")  # generated

    depends_on("python@3.9:", type=("build", "run"), when="@2.7:")

    with default_args(type="build"):
        depends_on("py-scikit-build-core@0.11:", when="@2.7:")
        depends_on("py-pybind11", when="@2.7:")
        depends_on("cmake@3.25:", when="@2.7:")
        depends_on("py-setuptools-scm", when="@2.7:")

        # Historical
        depends_on("py-setuptools@18.0:", when="@:2.0.2")

    with default_args(type=("build", "run")):
        # https://github.com/spglib/spglib/issues/407
        depends_on("py-numpy@:1", when="@:2.0.2")
        depends_on("py-numpy@1.20:2", when="@2.7:")

        depends_on("py-importlib-resources", when="@2.7: ^python@:3.9")
        depends_on("py-typing-extensions@4.9:", when="@2.7: ^python@:3.12")
