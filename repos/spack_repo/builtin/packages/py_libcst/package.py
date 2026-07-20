# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLibcst(PythonPackage):
    """A Concrete Syntax Tree (CST) parser and serializer library for Python."""

    homepage = "https://github.com/Instagram/LibCST"
    pypi = "libcst/libcst-0.4.9.tar.gz"

    license("Apache-2.0")

    version("1.8.6", sha256="f729c37c9317126da9475bdd06a7208eb52fcbd180a6341648b45a56b4ba708b")
    version("0.4.9", sha256="01786c403348f76f274dbaf3888ae237ffb73e6ed6973e65eba5c1fc389861dd")

    depends_on("python@3.9:", type=("build", "run"), when="@1.2.0:")

    with default_args(type="build"):
        depends_on("py-setuptools-rust", type="build")
        depends_on("py-setuptools-scm", type="build")
        depends_on("py-setuptools", type="build")
        depends_on("rust", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-pyyaml@6.0.3:", when="@1.8.6: ^python@3.14:")
        depends_on("py-pyyaml-ft@8:", when="@1.8: ^python@3.13")
        depends_on("py-pyyaml@5.2:", when="^python@:3.12")

        depends_on("py-typing-extensions", when="@1.8: ^python@:3.9")
        depends_on("py-typing-extensions@3.7.4.2:", when="@:1.2")
        depends_on("py-typing-inspect@0.4:", when="@:1.2")
