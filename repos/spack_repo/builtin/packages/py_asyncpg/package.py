# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAsyncpg(PythonPackage):
    """A fast PostgreSQL Database Client Library for Python/asyncio."""

    homepage = "https://github.com/MagicStack/asyncpg"
    pypi = "asyncpg/asyncpg-0.31.0.tar.gz"

    version("0.31.0", sha256="c989386c83940bfbd787180f2b1519415e2d3d6277a70d9d0f0145ac73500735")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@77.0.3:", type="build")
    depends_on("py-cython@3.2.1:3", type="build")

    depends_on("py-async-timeout@4.0.3:", when="^python@:3.10", type=("build", "run"))
