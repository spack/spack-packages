# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbSqliteScanner(DuckdbExtensionPackage):
    """Adds support for reading and writing SQLite database files."""

    homepage = "https://github.com/duckdb/duckdb-sqlite"

    license("MIT")

    published_binaries(
        "sqlite_scanner",
        "2.0.0",
        {
            "linux_amd64": "59b8a0ba6d7599d4aa584bd24e8b4cc3247076bb174157f43e110e56e6c72e86",
            "linux_arm64": "49b2ff354ea10f797fde7609d2be58e3b141130371e500bb4a94aeee9ef4f3a1",
            "osx_amd64": "453ec5d1b00668c0efa8962ce2cfcf2af65976c2deccb56ce4e4b0c3b8838379",
            "osx_arm64": "0c5b3921d3367525659251c2989398df2c463f05389bba35784a7a45c17d57a7",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-sqlite.git",
        commit="e223dc01493414cef6d5960744f1e048d59fc592",
        submodules=lambda package: ["database-connector"],
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
