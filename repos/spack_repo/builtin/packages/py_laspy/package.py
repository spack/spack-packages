# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLaspy(PythonPackage):
    """Native Python ASPRS LAS read/write library."""

    homepage = "https://github.com/laspy/laspy"
    pypi = "laspy/laspy-2.0.3.tar.gz"

    license("BSD-2-Clause")

    version("2.6.1", sha256="ce9cb9a18528b2a2b985583df40a4dea68cdda7995e47e4b00b6d48df0e88daa")
    version("2.6.0", sha256="9f1b9f2598a7e7f55aef94d030c6fab99c68bed751ca66fe11f017e43c260294")
    version("2.5.4", sha256="eebdbf3379afbc0b24e7e4812fac567bff880d1e851f70175d22375aaecdf7e1")
    version("2.2.0", sha256="69d36f01acecd719cbe3c3cf58353f247f391ccadb1da37731d45bfe919685df")
    version("2.0.3", sha256="95c6367bc3a7c1e0d8dc118ae4a6b038bf9e8ad3e60741ecb8d59c36d32f822a")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    # https://github.com/laspy/laspy/pull/313
    depends_on("py-numpy@:1", when="@:2.5.3", type=("build", "run"))
