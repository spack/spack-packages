# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbTpcds(DuckdbExtensionPackage):
    """Adds TPC-DS data generation and query support."""

    homepage = "https://github.com/duckdb/duckdb"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "eb370b4558a20454608ed800de0891fcb30f7b3eeed2989a54ca19f447977f60",
            "linux_arm64": "e9b63bd0a73fc8713853b3b5a2301a84031dd0916bb12f4409d46c59652f8c2d",
            "osx_amd64": "9a15b01a45f42c3b1d891143da2bb7f77da3873d6067ff8fe072fae3158adeae",
            "osx_arm64": "7f4b122053bdd75a156a2113809a559277d5a4038150028d7bd9d5bfbd82df30",
        }
    }
