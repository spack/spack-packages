# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbVortex(DuckdbExtensionPackage):
    """Adds support for reading and writing files using the Vortex file format."""

    homepage = "https://github.com/vortex-data/duckdb-vortex"

    license("MIT")

    published_binaries(
        "vortex",
        "2.0.0",
        {
            "linux_amd64": "9d5d6c429268188fc2e735947c383bbfa1a9abf09241437a83f0a5bbe089ad95",
            "linux_arm64": "eb1eb304ec9b15a73beccfbc1cb92ea2a9f3b9fdbf5677a7a05c6bf498274b6a",
            "osx_arm64": "03ae00b862c60245c304d094c81151f4fb51d8f822d07becad8373bc6238b419",
        },
    )

    duckdb_patches = True

    resource(
        name="extension_source",
        git="https://github.com/vortex-data/duckdb-vortex.git",
        commit="f56da1b2736ff2032db5c09a540303408c93f195",
        submodules=lambda package: ["vcpkg"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
