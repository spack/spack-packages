# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbExcel(DuckdbExtensionPackage):
    """Adds support for Excel-like format strings."""

    homepage = "https://github.com/duckdb/duckdb-excel"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "84f54851b729093a5c36f9ff1583d964bcc840d0c49c53d1d7fda54f94723304",
            "linux_arm64": "95c02ff97fa76115e66879095058283049510ac94c3d63e24c1f5d5e00809110",
            "osx_amd64": "77af1aea683dd7f7324d9a0ddf09a316f60bf76d90157461607bc3a927d58e71",
            "osx_arm64": "754f0d1008ea4b6989304a5e5b221019a4a522b1d59e0ecf4a467a71505d12dc",
        }
    }
