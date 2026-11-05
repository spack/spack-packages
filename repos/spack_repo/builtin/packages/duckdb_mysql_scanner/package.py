# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbMysqlScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a MySQL database."""

    homepage = "https://github.com/duckdb/duckdb-mysql"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "6055f1a59dc527df795afccbf59279500d1ddc239608dd310c3eba0e98d1a11c",
            "linux_arm64": "eb43e136ce866049284bac5352838408c9cd88c48f1aa19065b63af4733c600c",
            "osx_amd64": "57eee2fd66bf7daa615b5753d00bafc96442019dcdab3de4bc729089109c0509",
            "osx_arm64": "3824ed8ae938ce77aeccfd5a5a7906d640760ad3edc2d876a8b81ede2395dccc",
        }
    }
