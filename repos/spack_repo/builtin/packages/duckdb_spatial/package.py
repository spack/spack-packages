# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbSpatial(DuckdbExtensionPackage):
    """Adds support for working with spatial data and functions."""

    homepage = "https://github.com/duckdb/duckdb-spatial"

    # The binary statically links GEOS, which is LGPL-2.1-or-later
    license("MIT AND LGPL-2.1-or-later")
