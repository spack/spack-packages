# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbZipfs(DuckdbExtensionPackage):
    """Adds support for reading files within zip archives."""

    homepage = "https://github.com/isaacbrodsky/duckdb-zipfs"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "df4218e1b3e8fff625fabb0e6f0498c86edb7fd9feb3c107d2e1621534ada9e3",
            "linux_arm64": "d85c51da9fbb8f0d452156ca33ca26de787bf945727769bc19c5a62e009e44f9",
            "osx_amd64": "f3f0a7a3e9f128a59689f4674527edf34c1097bff026fbfc26fdd00f51be29c3",
            "osx_arm64": "88e5ea3e7ca44ec561443827eeaf023578ebb58c31e380c9461f480b576b97ab",
        }
    }
