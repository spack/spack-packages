# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbLegacyParser(DuckdbExtensionPackage):
    """Adds the legacy SQL parser to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-legacy-parser"

    license("MIT")
