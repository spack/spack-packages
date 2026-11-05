# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbPostgresScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a Postgres database."""

    homepage = "https://github.com/duckdb/duckdb-postgres"

    license("MIT")
