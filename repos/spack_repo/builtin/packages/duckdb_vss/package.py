# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbVss(DuckdbExtensionPackage):
    """Adds indexing support to accelerate Vector Similarity Search."""

    homepage = "https://github.com/duckdb/duckdb-vss"

    license("MIT")
