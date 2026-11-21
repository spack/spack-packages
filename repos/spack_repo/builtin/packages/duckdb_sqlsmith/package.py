# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbSqlsmith(DuckdbExtensionPackage):
    """Adds the SQLsmith query generator to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-sqlsmith"

    license("MIT")

    published_binaries(
        "sqlsmith",
        "2.0.0",
        {
            "linux_amd64": "d2fac70a1dd483667fe4e475bbf9e5a85a38c05b3a23345e68e79486bda5a8de",
            "linux_arm64": "eb67d2555775438a268312cd24ecfcadd2189c22b93beba2c065654e2936c3dc",
            "osx_amd64": "d26f22c046da8606a3662c4b0301ad0fcdac800a486bb0817e121acdc0958a3c",
            "osx_arm64": "2040fcb751fda3533165956f09a1b942c433efed8f268ea7d97120d45a1f32a8",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-sqlsmith.git",
        commit="00c4e5796c4e3e1f98ff4adec55d87326d2d2f3c",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
