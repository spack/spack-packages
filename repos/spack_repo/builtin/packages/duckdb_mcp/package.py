# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbMcp(DuckdbCommunityExtensionPackage):
    """Adds support for the Model Context Protocol."""

    homepage = "https://github.com/teaguesterling/duckdb_mcp"

    license("Apache-2.0")

    extension_name = "duckdb_mcp"

    checksums = {
        "2.0.0": {
            "linux_amd64": "ec96c4844a0857000013e9d38bcdcf52155f4d11780164daff59e3a09b8af752",
            "linux_arm64": "769a265f092140348beb2fb2a92aa93ff539ff39236f9445c18d165680a8f2a5",
            "osx_arm64": "b8ade0974877e53bd89f1a13ba569ab77adfc2ba57f2b49c1d5d5140bbf73bec",
        }
    }
