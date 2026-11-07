# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbGcs(DuckdbCommunityExtensionPackage):
    """Adds support for Google Cloud Storage."""

    homepage = "https://github.com/northpolesec/duckdb-gcs"

    license("MIT")

    published_binaries(
        "gcs",
        "2.0.0",
        {
            "linux_amd64": "9c8d26732031ce4f9229b45d40a7c23e95021992a1397318c335617d0f211117",
            "linux_arm64": "c959b182a85112b98c7e49b2fb91af46a8f6ed83f21b0930b53f8cad7db7450f",
            "osx_amd64": "9b5ce254b3ea085701b4b346125383d040025ead6eb85eb7205a3cbf6f0a0e08",
            "osx_arm64": "1a01ebb6aae74973e67873bb674a58dbed1e7ded84e454905a9a8864a8917a99",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/northpolesec/duckdb-gcs.git",
        commit="f55eef6635f5b613d7cb90a98fe2ed7afcd0f0c8",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
