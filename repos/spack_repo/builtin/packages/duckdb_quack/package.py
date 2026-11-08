# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbQuack(DuckdbExtensionPackage):
    """Adds the DuckDB Quack client and server protocol."""

    homepage = "https://github.com/duckdb/duckdb-quack"

    license("MIT")

    published_binaries(
        "quack",
        "2.0.0",
        {
            "linux_amd64": "f9a5c0d2e0eef0f7546aba4579ab80d75d167cdf48830459faf67378ab2000fe",
            "linux_arm64": "9f7938a11eb9ff8026ccc9c6403ac4a9b1ba347f8c12ecd815f86eea09ed6005",
            "osx_amd64": "7567cb63fe169a2b8332fa950ff24addb6d055950689c24c45a2d9781fc3b9c6",
            "osx_arm64": "d6779fb4adf9835e31f3b34cfdb1444cec1dd3af8f5ca99071271a91bae52cfc",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-quack.git",
        commit="f96420ed46aee9c42064bdb99ddfd1230d6c0086",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
