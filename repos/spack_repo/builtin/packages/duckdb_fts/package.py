# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbFts(DuckdbExtensionPackage):
    """Adds support for Full-Text Search Indexes."""

    homepage = "https://github.com/duckdb/duckdb-fts"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "d0236578d3758b689c871957ce8654b629b11c8008f7789054a526446c6bf8a3",
            "linux_arm64": "b96ab6ec6b657175ab0c5ea3b6baf2ff1636de22a3ab173762f16f5aaa82ca6b",
            "osx_amd64": "25b271e34fd6e9388fb649654824ce48d1b85f9cd8c1aacf031d43230553b7d9",
            "osx_arm64": "d62cb8678763117e7cd2f5e7825ff97836f31d7d948c28fceb8fe300806bd5ac",
        }
    }
