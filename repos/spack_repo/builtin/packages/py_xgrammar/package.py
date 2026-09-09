# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXgrammar(PythonPackage):
    """Efficient, Flexible and Portable Structured Generation."""

    homepage = "https://github.com/mlc-ai/xgrammar"
    pypi = "xgrammar/xgrammar-0.1.29.tar.gz"

    version("0.2.3", sha256="f76423630ae3ac4e090cb38ce1e30e7bcc69b3dee4d22d94353944386a4c6f18")
    version("0.1.29", sha256="cf195afa81b489eebf35d4c6f37f27136d05420739ab4a6f7f065c938d7e4baa")

    # nanobind's nb_type_get/nb_type_put have hidden visibility and get
    # dropped by GCC's LTO, causing undefined references at link time.
    # See https://github.com/wjakob/nanobind/issues/795.
    patch("no-lto-nanobind.patch", when="@0.1.29")

    depends_on("py-scikit-build-core@0.10:", type="build")
    depends_on("py-nanobind@2.5.0", type="build", when="@0.1.29")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-apache-tvm-ffi@0.1.9:", type=("build", "run"), when="@0.1.34:")
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-torch@1.10:", type=("build", "run"))
    depends_on("py-transformers@4.38:", type=("build", "run"))
    depends_on("py-triton", type=("build", "run"))  # todo(tbouvier) when linux + x86
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-typing-extensions@4.9:", type=("build", "run"))
