# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbBigquery(DuckdbCommunityExtensionPackage):
    """Adds support for querying Google BigQuery."""

    homepage = "https://github.com/hafenkran/duckdb-bigquery"

    license("MIT")

    published_binaries(
        "bigquery",
        "2.0.0",
        {
            "linux_amd64": "3c7ff5ca51ddb747802127c52922de19ece4d6efb2db3398500561f673223da5",
            "linux_arm64": "43457c596f704384af7c8c5716909ca3f55b6b40541c2b148ce172c441367443",
            "osx_amd64": "745c829bcb54aae2464f743ed1930de31719725b30f69fb74e0760ff683312f6",
            "osx_arm64": "ce242f3cf06d9256f6635caae1ff9c90120f11f3ce22db53498715e57702fdd8",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/hafenkran/duckdb-bigquery.git",
        commit="5439a6a58439af4c05064f80a28b159c5a1424e7",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
