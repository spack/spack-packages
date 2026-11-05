# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbDucklake(DuckdbExtensionPackage):
    """Adds support for DuckLake, SQL as a Lakehouse Format."""

    homepage = "https://github.com/duckdb/ducklake"

    license("MIT")
