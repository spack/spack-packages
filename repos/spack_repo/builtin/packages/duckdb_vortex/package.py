# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbVortex(DuckdbExtensionPackage):
    """Adds support for reading and writing files using the Vortex file format."""

    homepage = "https://github.com/vortex-data/duckdb-vortex"

    license("MIT")
