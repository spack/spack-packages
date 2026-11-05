# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbIceberg(DuckdbExtensionPackage):
    """Adds support for Apache Iceberg."""

    homepage = "https://github.com/duckdb/duckdb-iceberg"

    license("MIT")

    # The iceberg extension loads avro when it initializes
    depends_on("duckdb-avro", type=("build", "run"))
