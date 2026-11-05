# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbIceberg(DuckdbExtensionPackage):
    """Adds support for Apache Iceberg."""

    homepage = "https://github.com/duckdb/duckdb-iceberg"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "b93676e544e5c6843915fb3392e3b3c35859c065fa6ace7a26cb46ca4394e56d",
            "linux_arm64": "5616c30201099564326826d223aeea19b59f15744a981b074a906fb2b9dd4f44",
            "osx_amd64": "fe374b1bb4f676a6900ca2428ac4b2d3caba7fca5ef1e47080c6e960ceecdbf6",
            "osx_arm64": "30afc5f75b29497cd3a56f92e7b55febafbcca2e9c0846bb78599518094e55a7",
        }
    }

    # The iceberg extension loads avro when it initializes
    depends_on("duckdb-avro+pinned", type=("build", "run"), when="+pinned")
    depends_on("duckdb-avro~pinned", type=("build", "run"), when="~pinned")
