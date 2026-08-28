# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesRasterio(PythonPackage):
    """Typing stubs for rasterio."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_rasterio/types_rasterio-1.5.0.20260810.tar.gz"

    license("Apache-2.0")

    version(
        "1.5.0.20260810", sha256="45e2e43dc5c97eeaf2f3c9f8b89b3d269914d1cf2a0a2c32e6fe029ee79dd5e6"
    )

    depends_on("py-setuptools@82.0.1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:")
        depends_on("py-numpy@2:")
        depends_on("py-click@8:")
