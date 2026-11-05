# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAws(DuckdbExtensionPackage):
    """Provides features that depend on the AWS SDK."""

    homepage = "https://github.com/duckdb/duckdb-aws"

    license("MIT")
