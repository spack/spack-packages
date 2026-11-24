# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWhenever(PythonPackage):
    """Modern datetime library for Python."""

    homepage = "https://github.com/ariebovenberg/whenever"
    pypi = "whenever/whenever-0.9.5.tar.gz"

    license("MIT")

    version("0.9.5", sha256="9d8f2fbc70acdab98a99b81a2ac594ebd4cc68d5b3506b990729a5f0b04d0083")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-rust", type="build")

    depends_on("py-tzdata@2020.1:", when="platform=windows", type=("build", "run"))
    # Waiting for when="not platform="
    depends_on("py-tzlocal@4:", when="platform=windows", type=("build", "run"))
    depends_on("py-tzlocal@4:", when="platform=cray", type=("build", "run"))
    depends_on("py-tzlocal@4:", when="platform=solaris", type=("build", "run"))
