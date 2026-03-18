# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMbstrdecoder(PythonPackage):
    """mbstrdecoder is a Python library for multi-byte character string decoder."""

    homepage = "https://github.com/thombashi/mbstrdecoder"
    pypi = "mbstrdecoder/mbstrdecoder-1.1.4.tar.gz"

    license("MIT")

    version("1.1.4", sha256="8105ef9cf6b7d7d69fe7fd6b68a2d8f281ca9b365d7a9b670be376b2e6c81b21")

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")

    depends_on("py-chardet@3.0.4:5", type=("build", "run"))
