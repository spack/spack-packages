# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbMysqlScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a MySQL database."""

    homepage = "https://github.com/duckdb/duckdb-mysql"

    license("MIT")
