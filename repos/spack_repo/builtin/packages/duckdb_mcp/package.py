# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbMcp(DuckdbCommunityExtensionPackage):
    """Adds support for the Model Context Protocol."""

    homepage = "https://github.com/teaguesterling/duckdb_mcp"

    license("Apache-2.0")

    extension_name = "duckdb_mcp"

    published_binaries(
        "duckdb_mcp",
        "2.0.0",
        {
            "linux_amd64": "34c764ca5f1d617205b109b47cd4f70bce69d741d0b8b5041e5d2b4aa8223756",
            "linux_arm64": "bf3fb1d1fb54a82f85dcf1773e1e7dee05c60c2c990c07f3c8dfc15761b5094e",
            "osx_arm64": "398d9f2a5373e165736dc9d61d30ff457ac1f72527846c961509bb4d7511e1bf",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_mcp.git",
        commit="6b2b1dc899e1b5834ed6ee2f574e309f445e23b1",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
