# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbLegacyParser(DuckdbExtensionPackage):
    """Adds the legacy SQL parser to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-legacy-parser"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "db3a894d309dd415c9fcedf44613d4a5554cd862527dfced35c1e360214391ba",
            "linux_arm64": "84198b97cc033ab4a60b6fe43d952fb81d7dba3225832d0a84b498a77d751a67",
            "osx_amd64": "09e8b147341120b6263e3e73fd92059725a82c47914aaa43878fd165452cd7da",
            "osx_arm64": "60163a5bcda16b7fa8099c0da3b4db2aba9a40188fcd84697948141d4bb9605d",
        }
    }
