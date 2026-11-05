# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbPlinkingDuck(DuckdbCommunityExtensionPackage):
    """Adds support for PLINK 2 genomics file formats."""

    homepage = "https://github.com/teaguesterling/plinking_duck"

    license("MIT")

    published_binaries(
        "plinking_duck",
        "2.0.0",
        {
            "linux_amd64": "2e82af1000e2bd57360536c39916e737581562df2805674e19e1cb29e2ea8834",
            "linux_arm64": "f1ec5e2092332b69677eb5e7480b8d79e9aa76d20ac5434f7ce7dac46bbfaefa",
            "osx_amd64": "e126532cd7652ff66acc84f2c21eaafd6462fe8645fdf98ab73fed42b98532cf",
            "osx_arm64": "2a9e007c20939758fb7617b13f1a4faae58e9381237237010fdbdd32445e1fa0",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/plinking_duck.git",
        commit="73daba06dd3ad4ab4d0a1a32b33bd18f6fa48db9",
        submodules=lambda package: ["third_party/plink-ng"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
