# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbYaml(DuckdbCommunityExtensionPackage):
    """Adds support for reading YAML files, and a YAML type."""

    homepage = "https://github.com/teaguesterling/duckdb_yaml"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "43f31b7067ee3f3d97a094c51a0f8a1e7b0318b1c16d89cf8b9ff18e0eb650cc",
            "linux_arm64": "9a40e9dd1fa828c3519dc2c4fbdb367a13ac600d572057d4ce1c4ba5f74a58df",
            "osx_amd64": "1e2fd8b5f50228bbd5e2dd9ed2326320029499dc2c8bd7b685e64e9b396a98f1",
            "osx_arm64": "c5c24a8fd8b97da4fceab861ab0f483b171b7a327f30d71cb71865dc59526be0",
        }
    }
