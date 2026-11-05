# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbSqliteScanner(DuckdbExtensionPackage):
    """Adds support for reading and writing SQLite database files."""

    homepage = "https://github.com/duckdb/duckdb-sqlite"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "8d66f0661fe4da3b60fb1ef69caaefb102248dfa5a234a8671fed5b4edca441b",
            "linux_arm64": "c2dc454512553bc09b075172893189435281e6d7ea6297dd211fbc93db985050",
            "osx_amd64": "711883be1c8da29b86bdcab4cb535f950fe7ba472dc49255bf68fbb9ec5caec2",
            "osx_arm64": "752176198a7aca3aee3f32136938e7fb390c7d80b8536d4d5c7f08d111213540",
        }
    }
