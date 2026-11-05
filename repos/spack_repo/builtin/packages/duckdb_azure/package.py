# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAzure(DuckdbExtensionPackage):
    """Adds a filesystem abstraction for Azure blob storage to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-azure"

    license("MIT")
