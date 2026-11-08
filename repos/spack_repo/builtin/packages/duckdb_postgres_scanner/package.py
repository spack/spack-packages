# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbPostgresScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a Postgres database."""

    homepage = "https://github.com/duckdb/duckdb-postgres"

    license("MIT")

    site_signed_link_libraries = [
        ("postgresql", "pgcommon_shlib"),
        ("postgresql", "pgport_shlib"),
        ("openssl", "ssl"),
        ("openssl", "crypto"),
        ("zlib-api", "z"),
    ]

    with when("+site_signed"):
        depends_on("postgresql", type="build")
        depends_on("zlib-api", type="build")

    published_binaries(
        "postgres_scanner",
        "2.0.0",
        {
            "linux_amd64": "54b3d751cafc9ffa439886b1607d0ee758dab4dc070f0171e779b95f2f3e554f",
            "linux_arm64": "afe7f2bd798b61e4c2e1f96deedaa70a21d15eebc8cd9470beb923951d0ce58a",
            "osx_amd64": "be095bd7b33b970467d09ac0ab8f84ba2e75b2368857a3b07eab6f5096c20a93",
            "osx_arm64": "496a338695582a99db2826597affc03307a4d7ed7b92c972e261adfe40f03fe3",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-postgres.git",
        commit="c0f5a3c0c4b68b02afbf669d36d7f0e503985c88",
        submodules=lambda package: ["database-connector"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
