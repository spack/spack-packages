# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbH3(DuckdbCommunityExtensionPackage):
    """Adds hierarchical hexagonal indexing for geospatial data."""

    homepage = "https://github.com/isaacbrodsky/h3-duckdb"

    license("Apache-2.0")

    published_binaries(
        "h3",
        "2.0.0",
        {
            "linux_amd64": "7514dc2834ca9c0af0962b796470a54c706ec69c82df4fb3cde1666045f41c2b",
            "linux_arm64": "ec3e8124984b60c258131589ef22aaaa1877b2b2033a05a3a5901be32d01d7f4",
            "osx_arm64": "8cefdcdc32c7de808549eed8725cf10b4bdd3641d8fc3ab2df30d004784db393",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/isaacbrodsky/h3-duckdb.git",
        commit="ae1c424773752f775e0549971818454f61255291",
        submodules=lambda package: ["h3"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
