# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbLance(DuckdbExtensionPackage):
    """Adds support for querying Lance datasets."""

    homepage = "https://github.com/lance-format/lance-duckdb"

    license("Apache-2.0")
