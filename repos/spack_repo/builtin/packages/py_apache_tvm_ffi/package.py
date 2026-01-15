# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyApacheTvmFfi(PythonPackage):
    """Open ABI and FFI for Machine Learning Systems"""

    homepage = "https://github.com/apache/tvm-ffi"
    pypi = "apache-tvm-ffi/apache_tvm_ffi-0.1.3.tar.gz"
    git = homepage + ".git"

    license("Apache-2.0")

    version("main", branch="main")
    version("0.1.6", sha256="53088126f7fce11823ddf0fb101e968a90298d79fd68829c0a981f25467a574c")
    version("0.1.5", sha256="21bc35cb9d9fdec54061b802a2b432fd1155d2733da94df8678ff21bab1d9a2f")
    version("0.1.4", sha256="1a6e635b671e962bbc3bf1bc97bfd82e4c0f1bedf27c8d183bb282664974d0d3")
    version("0.1.3", sha256="d33f0bc0d028cddf321d69724c916504272a7f03dfc1d8e507d9d0f88b6f7cbf")
    version("0.1.2", sha256="91f6e4e38572f7ce78c6df810cc16bdd1283fd925010b0e503697934d58bb7e7")
    version("0.1.1", sha256="728ce3f4ae02b89a7147b718f7f670afac3c6d1f96df38d488757274643709fc")
    version("0.1.0", sha256="ba45ebf98bab436442f3ee34c8b9c69e00797ae3529ea3df37a56aa7aa479cf2")

    depends_on("py-typing-extensions@4.5:")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        # https://github.com/apache/tvm-ffi/blob/v0.1.3/pyproject.toml
        depends_on("py-scikit-build-core@0.10.0:")
        depends_on("py-cython@3.0:")
        depends_on("py-setuptools-scm")
        # https://github.com/apache/tvm-ffi/blob/v0.1.0/CMakeLists.txt#L18
        depends_on("cmake@3.18:")
        depends_on("ninja@1.11:")
