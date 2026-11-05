# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAvro(DuckdbExtensionPackage):
    """Adds support for reading Avro files."""

    homepage = "https://github.com/duckdb/duckdb-avro"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "3f37797ca9a4ef3b5a07e65278c653fe0a32f7edea1498c801022fed49afedc7",
            "linux_arm64": "3e8a61c8ae51851a8c70c49a5972fd3c3302c3ffa798f3286f7dca0746975607",
            "osx_amd64": "30865761c89321826775583a924334a83b9e0b42db2d90d7a0cc312ab99d33d5",
            "osx_arm64": "add62d712421e10adf9ddc8711cf14d2ee382baa14e4281e3d965fe7e5f7779e",
        }
    }
