# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAvro(DuckdbExtensionPackage):
    """Adds support for reading Avro files."""

    homepage = "https://github.com/duckdb/duckdb-avro"

    license("MIT")
