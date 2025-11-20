# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMurmurhash(PythonPackage):
    """Cython bindings for MurmurHash."""

    homepage = "https://github.com/explosion/murmurhash"
    pypi = "murmurhash/murmurhash-1.0.2.tar.gz"

    license("MIT")

    version("1.0.15", sha256="58e2b27b7847f9e2a6edf10b47a8c8dd70a4705f45dccb7bf76aeadacf56ba01")
    version("1.0.10", sha256="5282aab1317804c6ebd6dd7f69f15ba9075aee671c44a34be2bde0f1b11ef88a")
    version("1.0.2", sha256="c7a646f6b07b033642b4f52ae2e45efd8b80780b3b90e8092a0cec935fbf81e2")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.6:3.14", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel@0.32", type="build", when="@1.0.2")
    depends_on("py-cython@0.25:", type="build")
    depends_on("py-cython@3.1:", type="build", when="@1.0.15:")
