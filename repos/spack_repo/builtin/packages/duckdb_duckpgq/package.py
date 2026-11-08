# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbDuckpgq(DuckdbCommunityExtensionPackage):
    """Adds support for SQL/PGQ and graph algorithms."""

    homepage = "https://github.com/cwida/duckpgq-extension"

    license("MIT")

    published_binaries(
        "duckpgq",
        "2.0.0",
        {
            "linux_amd64": "62bcf9563e04b7740e52dda2c17d77e87f646a21cec1af0c5938cca7eca7b2c9",
            "linux_arm64": "052fd6d69eed34dbd7c9b82f2290c0f336aca514df608cc1a255febe5183b6ab",
            "osx_amd64": "5bedf804c695150cfe5a61cce67048bc43a68069032fbbd82136a597d17081a6",
            "osx_arm64": "c6968007f568c3688f0ec33e2a465d58d4d2727f2532c52d7cfcd645fb744258",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/cwida/duckpgq-extension.git",
        commit="9c11bc192a071c9e44cef16cced90a22d7d7db2c",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
