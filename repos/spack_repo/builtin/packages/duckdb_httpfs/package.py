# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbHttpfs(DuckdbExtensionPackage):
    """Adds support for reading and writing files over a HTTP(S) connection."""

    homepage = "https://github.com/duckdb/duckdb-httpfs"

    license("MIT")
