# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbScalarfs(DuckdbExtensionPackage):
    """Adds virtual filesystems for working with scalars."""

    homepage = "https://github.com/teaguesterling/duckdb_scalarfs"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "fe977cbc52fd43a3c7bcbe2acf83ffd18d7f1788fd1911c6819f9a8a525a1a21",
            "linux_arm64": "4bac3d98be2bb673b0558464c6e8aa37a49aec3531a215c5a40ece485f7572d8",
            "osx_amd64": "51bf70a9ace9c33d571083c2b2803ffd8d365d104a9619b41884228a60c553a3",
            "osx_arm64": "2be319f9633ca64aaa43418108e2c38c29fbebad13ea08a3a7cdd4f7aae01c02",
        }
    }
