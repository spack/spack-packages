# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbScalarfs(DuckdbCommunityExtensionPackage):
    """Adds virtual filesystems for working with scalars."""

    homepage = "https://github.com/teaguesterling/duckdb_scalarfs"

    license("MIT")

    published_binaries(
        "scalarfs",
        "2.0.0",
        {
            "linux_amd64": "2b4cf5c18ca7a6e241001b9ffb770d0a5f4e4cd37ae8ea584a87c6d876b4faa7",
            "linux_arm64": "dc1a690bee889f91e92a12971f4264c907a788239890b6d756c723e612cdcf1b",
            "osx_amd64": "cf28ffe1913654c05addcc3aaf57da4a46468c4b2f0f7eb1512906740b3fa769",
            "osx_arm64": "341bc42dfb377ec9343e208b990a1513db0405b55d31dd76e586165be05487fb",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_scalarfs.git",
        commit="16a2637eaab656d3b94e7a25f612573f8e056769",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
