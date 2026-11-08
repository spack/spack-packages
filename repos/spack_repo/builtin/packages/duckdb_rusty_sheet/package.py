# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbRustySheet(DuckdbCommunityExtensionPackage):
    """Adds a reader for Excel, WPS and OpenDocument spreadsheets."""

    homepage = "https://github.com/redraiment/rusty-sheet"

    license("MIT")

    published_binaries(
        "rusty_sheet",
        "2.0.0",
        {
            "linux_amd64": "ae98e980da6fb1cd77641d761979f850b57a0103406d9cb3907c3e703ab96fac",
            "linux_arm64": "eb2fa0b21782cd84d39dc0037b30dc9b94b99d6647366a079138770d3106f817",
            "osx_amd64": "cde85dd9f0ddef792b4126fe8c71c4144845be0b957b014f65ae248262a0b1b8",
            "osx_arm64": "e3fe29d63c2f2197007cbbbccdf3aa39d991bf761505e5f84e600a6d2524f4d8",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/redraiment/rusty-sheet.git",
        commit="40dfb2862ca8f595fa83a4fe79d2ff9ef3084ca4",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
