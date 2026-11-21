# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbTpcds(DuckdbExtensionPackage):
    """Adds TPC-DS data generation and query support."""

    homepage = "https://github.com/duckdb/duckdb"

    license("MIT")

    published_binaries(
        "tpcds",
        "2.0.0",
        {
            "linux_amd64": "42f6b9dbea6841c876cfd5d1511fdb2ff8f23c9c9e2a096459536964a2ea63de",
            "linux_arm64": "d0c569def6bdba3f20120bf6ad0022bcd25bea673b7290f1db3301886c151cef",
            "osx_amd64": "77331708bbbbbce89fc3256f8f9394ab7f72649c7259d2a2d627cce6c6764d7c",
            "osx_arm64": "07ca7df05aa896f028d4b480d9fa4554100dc684fc9f4c6ec2690d8bbff1a5d9",
        },
    )
