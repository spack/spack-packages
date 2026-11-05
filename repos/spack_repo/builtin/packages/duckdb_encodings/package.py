# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbEncodings(DuckdbExtensionPackage):
    """Converts Unicode encodings to UTF-8."""

    homepage = "https://github.com/duckdb/duckdb-encodings"

    license("MIT")
