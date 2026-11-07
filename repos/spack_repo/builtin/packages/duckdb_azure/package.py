# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbAzure(DuckdbExtensionPackage):
    """Adds a filesystem abstraction for Azure blob storage to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-azure"

    license("MIT")

    published_binaries(
        "azure",
        "2.0.0",
        {
            "linux_amd64": "14007ba50d04e14e8e4dda3b808458ad8ca30a8d5e3a34c9434ec180c6fb4250",
            "linux_arm64": "9e10a7bef903e747fe92647ba804e6a37c5d82537ca44a8def499ffdc8bbca2b",
            "osx_amd64": "d695793f5c1e64376ce60f609b0dfbad88a8de73071f91ba88aeb64c1b19f265",
            "osx_arm64": "0ba14c30bf590d38a20b2e3849fda45bbd7572565afa315582feddd3c4c38452",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-azure.git",
        commit="906e92458c33309e5d9413e14a85aad7b4d2275f",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
