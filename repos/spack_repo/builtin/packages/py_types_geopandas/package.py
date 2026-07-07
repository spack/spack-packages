# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesGeopandas(PythonPackage):
    """Typing stubs for geopandas."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_geopandas/types_geopandas-1.1.1.20250829.tar.gz"

    license("Apache-2.0")

    version(
        "1.1.1.20250829", sha256="df386c6674052918b299e587e07acddf990110fb39478e0593cdd12e5f20f799"
    )

    depends_on("py-setuptools@77.0.3:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-types-shapely")
        depends_on("py-numpy@1.20:")
        depends_on("py-pandas-stubs")
        depends_on("py-pyproj")
