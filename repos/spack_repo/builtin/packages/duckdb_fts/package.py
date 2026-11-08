# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbFts(DuckdbExtensionPackage):
    """Adds support for Full-Text Search Indexes."""

    homepage = "https://github.com/duckdb/duckdb-fts"

    license("MIT")

    published_binaries(
        "fts",
        "2.0.0",
        {
            "linux_amd64": "9172520652ce609d163cf30645f382b197f2c7294448a816c77d62b0f029d96e",
            "linux_arm64": "d233d2311825da4d9b6efb45edd52b126b18134c7d7083b1e58f6d450ebdabee",
            "osx_amd64": "9b9fe0d2925953f9b2ebb60f5914d5224b49e72fa36849b8372f80c980b7e454",
            "osx_arm64": "fa5eef362e1f004d19c08d76ed4ec47d181d8feb07ca3b528f3058ee8945362b",
        },
    )

    duckdb_patches = True

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-fts.git",
        commit="2266e67d01c737cb65114e77c7c672e58869a635",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
