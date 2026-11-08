# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbExcel(DuckdbExtensionPackage):
    """Adds support for Excel-like format strings."""

    homepage = "https://github.com/duckdb/duckdb-excel"

    license("MIT")

    published_binaries(
        "excel",
        "2.0.0",
        {
            "linux_amd64": "40a170558c7110eed04b631551f9ac13f854747a293986612e9922b6044b3821",
            "linux_arm64": "c404d79e9ad928681db6ccf9dd73723922b02fc1c41a0c4c770baeef8f29911f",
            "osx_amd64": "956e419e082034f54a9b535f7d35aa595a19580bb79a479279f9d588f7e2b847",
            "osx_arm64": "a9e38c4bf55bd482073f2d40c3a0c1334fadfa819ca1b7a0eb599a38936c4fd1",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-excel.git",
        commit="81bb84b115b97cc4edec4827714cac80da0127e1",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
