# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbMssql(DuckdbCommunityExtensionPackage):
    """Adds support for connecting to Microsoft SQL Server."""

    homepage = "https://github.com/hugr-lab/mssql-extension"

    license("MIT")

    published_binaries(
        "mssql",
        "2.0.0",
        {
            "linux_amd64": "556e08a5c8c969b0325e1d7dd929309f66954789ad5af624ac0b557cf6ce7ea5",
            "linux_arm64": "15042f71d858844ad20daff0cc36b5c33f264e070b5da575117bfcded7372e9d",
            "osx_arm64": "5f0361a61f0aea8f0f57c4a937782ad6afbbb711fca908d5a7be72ba77276ca5",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/hugr-lab/mssql-extension.git",
        commit="bfd347ffa89dc520eb0fb82c857b3c7af12673dc",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
