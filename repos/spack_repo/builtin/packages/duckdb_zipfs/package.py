# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbZipfs(DuckdbCommunityExtensionPackage):
    """Adds support for reading files within zip archives."""

    homepage = "https://github.com/isaacbrodsky/duckdb-zipfs"

    license("MIT")

    published_binaries(
        "zipfs",
        "2.0.0",
        {
            "linux_amd64": "5444fdc6a0447131d1b9c13a18d180a271610a7ec97023dbb5846c1f5bbba0b2",
            "linux_arm64": "8bc5fdf53d4cd48509f98218c1f6f8e21d28f0917a1925e30cb62ede1b5c2400",
            "osx_amd64": "6629102f7794a0326c0360b54936a05af9fc08d5560d35a5926109e49fc1923b",
            "osx_arm64": "489df1de70189c2a6e250acfb32066db29a49541ad091f3459a9220d18be8df3",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/isaacbrodsky/duckdb-zipfs.git",
        commit="fd9fec45453caef9bd1a89a7f6d92e421da63ca8",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
