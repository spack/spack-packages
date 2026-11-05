# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbH3(DuckdbExtensionPackage):
    """Adds hierarchical hexagonal indexing for geospatial data."""

    homepage = "https://github.com/isaacbrodsky/h3-duckdb"

    license("Apache-2.0")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "abba3f5702e6917804a1e05be20013b51d2174e296b175f0a3fdfc2eeffd6352",
            "linux_arm64": "603841a52d3ebefe7c9acfa60bbc967af21965e88d1dd462c938686300e82c3c",
            "osx_arm64": "a033fe68f9a30afa9ae78b0bff431b10fd0b979977827863e12ba40ddf8463a7",
        }
    }
