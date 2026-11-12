# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNestAsyncio2(PythonPackage):
    """Patch asyncio to allow nested event loops."""

    homepage = "https://github.com/Chaoses-Ib/nest-asyncio2"
    pypi = "nest_asyncio2/nest_asyncio2-1.7.2.tar.gz"

    license("BSD-2-Clause")

    version("1.7.2", sha256="1921d70b92cc4612c374928d081552efb59b83d91b2b789d935c665fa01729a8")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@3.4.3: +toml", type="build")
