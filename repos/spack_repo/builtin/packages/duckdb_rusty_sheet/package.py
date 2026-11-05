# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbRustySheet(DuckdbExtensionPackage):
    """Adds a reader for Excel, WPS and OpenDocument spreadsheets."""

    homepage = "https://github.com/redraiment/rusty-sheet"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "7b034cedb2f7909a04cd4b49912ee84467f933b316824d1a453db34bad753b28",
            "linux_arm64": "ea515e69f2b6fc2e1bc5990a99240123e8d8dbb38f2c39221f6506013f2d1123",
            "osx_amd64": "148466fe383eee2c59d5e43bd4053d8c7dc52ff485a66ecb81e627118683d4f6",
            "osx_arm64": "cb5a7766ebed3bd6ea98cdf664053d5e3c77252a3f7bee379c89ecfa38e794e1",
        }
    }
