# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUuidUtils(PythonPackage):
    """Fast, drop-in replacement for Python's uuid module, powered by Rust."""

    homepage = "https://github.com/aminalaee/uuid-utils"
    pypi = "uuid_utils/uuid_utils-0.16.0.tar.gz"

    license("BSD 3-Clause")

    version("0.16.0", sha256="d6902d4375dfba4c9902c736bb82d3c040417b67f7d0fa48910ddfdb1ac95de7")

    depends_on("py-maturin@1", type="build")
    depends_on("rust", type="build")
    depends_on("python@3.10:", type=("build", "run"))
