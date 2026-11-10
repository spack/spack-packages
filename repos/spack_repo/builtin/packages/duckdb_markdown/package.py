# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbMarkdown(DuckdbCommunityExtensionPackage):
    """Adds support for reading and writing Markdown files."""

    homepage = "https://github.com/teaguesterling/duckdb_markdown"

    license("MIT")

    published_binaries(
        "markdown",
        "2.0.0",
        {
            "linux_amd64": "3570f1965bb0049865020e40c812444c96b7cb347a6be894c4d01565cdb03a57",
            "linux_arm64": "7e106f957d56a2012718b86e71f49f64a37d4d28bf185e393ea4f2f8d194bb5f",
            "osx_amd64": "ac133ee56544d7e095eafbf327d23d5a7270489698b6ac9ce33320ce7f96239b",
            "osx_arm64": "a879bc2c0b58fde9bb11c4f19112ba60f1c0ede59d6001204f37bb1a638dd1ca",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_markdown.git",
        commit="6fc7013de640191ea5248897df3b60a7bc07db67",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
