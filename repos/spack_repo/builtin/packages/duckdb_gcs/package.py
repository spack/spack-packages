# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbGcs(DuckdbCommunityExtensionPackage):
    """Adds support for Google Cloud Storage."""

    homepage = "https://github.com/northpolesec/duckdb-gcs"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "e1821ed714e6eec7271a18fe31f214b45e8cd17e6e41c1d23d77677bf7b688bc",
            "linux_arm64": "5398cd2378610e7c52a56e838eab39ee8e553aea37b652d94fcec88fe8f2d647",
            "osx_amd64": "0f6797bf4af090cc11940c1102f5efb832f36a966e645324a9bf7dcd3d946643",
            "osx_arm64": "c1f7682df6c39dcd15f3ff198bbac704e67948f89a1cf003b0b2fdc686520402",
        }
    }
