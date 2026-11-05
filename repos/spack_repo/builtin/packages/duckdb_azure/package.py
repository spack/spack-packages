# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAzure(DuckdbExtensionPackage):
    """Adds a filesystem abstraction for Azure blob storage to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-azure"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "5f89669dad1b57f1bfa6753a979d67d09dd07ede87dbfef9ccc2b1acd3b06b7c",
            "linux_arm64": "37e60f4f53c755967c7c90d0b4ac915603e728f260a9510d0a67d0a1e50e2994",
            "osx_amd64": "4790574483daf8633683d58f717e8a3791ba55fd6e984e35834af0ebac204fe1",
            "osx_arm64": "8b7496bc3649d5e58f4de1ab30ba5b32350826404648503a1d9be46c111e098f",
        }
    }
