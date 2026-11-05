# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbEncodings(DuckdbExtensionPackage):
    """Converts Unicode encodings to UTF-8."""

    homepage = "https://github.com/duckdb/duckdb-encodings"

    license("MIT")

    published_binaries(
        "encodings",
        "2.0.0",
        {
            "linux_amd64": "5e84d13f1c3512814b8ebf226c71b1fb1dc3376395048f220f6abce8c720033c",
            "linux_arm64": "565985e41b92604f6e62208af08e8811e12aeda9730d0aaac5a3d93407eaccab",
            "osx_amd64": "ee4a9069cef1e93fe3bdb32ae6d7edb213b884b2431a3ec38c16a085e4685dab",
            "osx_arm64": "5c9e8094973f2628ba852dc8b148307ea22007c2b37d2c5f65ec12c0ab2ba46f",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-encodings.git",
        commit="2d1447a890302d9dff23ac7c8119ddce53ee65ff",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
