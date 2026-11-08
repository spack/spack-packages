# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbDelta(DuckdbExtensionPackage):
    """Adds support for Delta Lake."""

    homepage = "https://github.com/duckdb/duckdb-delta"

    license("MIT")

    published_binaries(
        "delta",
        "2.0.0",
        {
            "linux_amd64": "418d8f21fe10a6f49d200d76b745fc7f1ca916daa5d404b18c46e0f51cffcc7d",
            "linux_arm64": "7dc29ad733d7967984096f4dfd715c3f3404d43ac11b53350ad73fa42b8b90d3",
            "osx_amd64": "2860ad9152ec9aae39cec2f57c14a70af9f40a6530db25d82e7d279b336d6434",
            "osx_arm64": "4396f8cb5fe223214adf5c3be5edbfccf5d599ca877ccdcbb6a2c5adb5552423",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-delta.git",
        commit="9dcfb65b99fcafaa068222c2490abc143da4cc8e",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
