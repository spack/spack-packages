# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbLegacyParser(DuckdbExtensionPackage):
    """Adds the legacy SQL parser to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-legacy-parser"

    license("MIT")

    published_binaries(
        "legacy_parser",
        "2.0.0",
        {
            "linux_amd64": "2da013c24c51210768122ae601d3576801169a39f7b2840e858bbd711ffcbfad",
            "linux_arm64": "18c349d5924fa3d9e293d8f7d7dad1177a0e082aabcd9ee0ca0ca9e428e1d209",
            "osx_amd64": "114990a9bb1adeafb530af67fc2488693242377cfb38ff5842cc2e711c60560d",
            "osx_arm64": "79487a5abc28d9a17bb58c30e0fc5f158c7ae3a9d4c2081e02563da96690eb59",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-legacy-parser.git",
        commit="bcdf276132fe3a09afcc707c1cdff39096989404",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
