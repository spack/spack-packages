# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbUrlpattern(DuckdbCommunityExtensionPackage):
    """Adds the WHATWG URLPattern API for matching URLs."""

    homepage = "https://github.com/teaguesterling/duckdb_urlpattern"

    license("MIT")

    published_binaries(
        "urlpattern",
        "2.0.0",
        {
            "linux_amd64": "9c9fcbfbf101e849fdd447918f6a1d4f5951fdc84256461bac5d6544e97b5188",
            "linux_arm64": "79b0b494e70d7e1bbc38b45cb418708b4ec5d10483c8276e8c6b2e1685d13415",
            "osx_amd64": "7af127c7b0397661ea794125c2cb1274d109bcf2395261c97ed6ea7825e4c5b2",
            "osx_arm64": "7009bcc1a079b21c10f16a9b5290584c008ebdb2fde821e14065c92253fe5da0",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_urlpattern.git",
        commit="0e14b580454ea92ff0120bdbac9ab836c407bd1b",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
