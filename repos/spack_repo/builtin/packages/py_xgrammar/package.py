# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXgrammar(PythonPackage):
    """Efficient, Flexible and Portable Structured Generation."""

    homepage = "https://github.com/mlc-ai/xgrammar"
    pypi = "xgrammar/xgrammar-0.1.29.tar.gz"

    version("0.1.29", sha256="cf195afa81b489eebf35d4c6f37f27136d05420739ab4a6f7f065c938d7e4baa")

    depends_on("py-scikit-build-core@0.10:", type="build")
    depends_on("py-nanobind@2.5.0", type="build", when="@0.1.29")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-torch@1.10:", type=("build", "run"))
    depends_on("py-transformers@4.38:", type=("build", "run"))
    depends_on("py-triton", type=("build", "run"))  # todo(tbouvier) when linux + x86
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-typing-extensions@4.9:", type=("build", "run"))
