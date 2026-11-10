# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbInet(DuckdbExtensionPackage):
    """Adds support for IP-related data types and functions."""

    homepage = "https://github.com/duckdb/duckdb-inet"

    license("MIT")

    published_binaries(
        "inet",
        "2.0.0",
        {
            "linux_amd64": "afc4efe65dfb5106b18e3ab75753f680bd6eecc5d17ec347a325b3bf0e55cfdd",
            "linux_arm64": "fa189a8adaa657299d05b8f99a181b10223f5063c396514dea06f8219ff646ab",
            "osx_amd64": "9a6d6e2893cc3abf8151bc9788eda398a15ac7ed4ebfc452858f2b41897e46ab",
            "osx_arm64": "2508bb02df9cc85188d00964b9d90a510c0caa8ec33fbb51f71c4cf810d247f2",
        },
    )

    duckdb_patches = True

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-inet.git",
        commit="fe7f60bb60245197680fb07ecd1629a1dc3d91c8",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
