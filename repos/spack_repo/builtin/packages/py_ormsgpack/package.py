# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOrmsgpack(PythonPackage):
    """Fast, correct Python msgpack library supporting dataclasses, datetimes, and numpy."""

    homepage = "https://github.com/ormsgpack/ormsgpack"
    pypi = "ormsgpack/ormsgpack-1.7.0.tar.gz"

    license("Apache-2.0 OR MIT")

    version("1.12.2", sha256="944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33")
    version("1.7.0", sha256="6b4c98839cb7fc2a212037d2258f3a22857155249eb293d45c45cb974cfba834")

    depends_on("py-maturin@1", type="build")
    depends_on("rust@1.81:", type="build", when="@1.9:")
    depends_on("rust@1.70:", type="build")
    depends_on("python@3.10:", type=("build", "run"), when="@1.12:")
    depends_on("python@3.9:", type=("build", "run"))
