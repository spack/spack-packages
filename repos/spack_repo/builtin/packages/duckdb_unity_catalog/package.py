# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbUnityCatalog(DuckdbExtensionPackage):
    """Adds support for connecting to Unity Catalog."""

    homepage = "https://github.com/duckdb/unity_catalog"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "9d2c61676e606729066f6ab9520a7557cf6542534aee9cb26402195987d4bd87",
            "linux_arm64": "1ac1b3a1b69a65236733f40a454e0b72515d7c1e0768704a92ae0db1d157f504",
            "osx_amd64": "a22bfb935ad1f5fb308892d5876a1cdfc83d90fc982b5a12410d67189939aa16",
            "osx_arm64": "07659c9b7f0fda5ec5d7c2a5fac1f1f451b03d28f0eb3f4d1910239881ebbc4d",
        }
    }
