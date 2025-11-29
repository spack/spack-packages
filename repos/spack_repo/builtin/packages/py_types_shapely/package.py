# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesShapely(PythonPackage):
    """Typing stubs for shapely."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_shapely/types_shapely-2.1.0.20250917.tar.gz"

    license("Apache-2.0")

    version(
        "2.1.0.20250917", sha256="5c56670742105aebe40c16414390d35fcaa55d6f774d328c1a18273ab0e2134a"
    )

    depends_on("py-setuptools@77.0.3:", type="build")
    depends_on("py-numpy@1.20:", type=("build", "run"))
