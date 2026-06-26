# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOrmsgpack(PythonPackage):
    """Fast, correct Python msgpack library supporting dataclasses, datetimes, and numpy."""

    homepage = "https://github.com/ormsgpack/ormsgpack"
    pypi = "ormsgpack/ormsgpack-1.12.2.tar.gz"

    license("Apache-2.0 OR MIT")

    version("1.12.2", sha256="944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33")

    depends_on("py-maturin@1", type="build")
    depends_on("rust@1.81:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
