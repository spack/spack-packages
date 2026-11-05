# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbVss(DuckdbExtensionPackage):
    """Adds indexing support to accelerate Vector Similarity Search."""

    homepage = "https://github.com/duckdb/duckdb-vss"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "5afcd13e9e10061969701fbd9d80bd0512c1071fe6a8ab1c993030fbefe165d1",
            "linux_arm64": "f8b91e90b1e8591c5642ccf37efeaefb2916b5afd10a4a48aa3636c81cf9621c",
            "osx_amd64": "81e5275cda44011bf59fd746d87e47d94b643c5a863c56bd2813ebc28f91647b",
            "osx_arm64": "37b9494c65282f2d4af5f4d0763e53247196b8400f4ba8edc1356827f1b1ff56",
        }
    }
