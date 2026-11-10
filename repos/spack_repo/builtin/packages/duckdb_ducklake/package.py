# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbDucklake(DuckdbExtensionPackage):
    """Adds support for DuckLake, SQL as a Lakehouse Format."""

    homepage = "https://github.com/duckdb/ducklake"

    license("MIT")

    published_binaries(
        "ducklake",
        "2.0.0",
        {
            "linux_amd64": "ff1c730a5d5a7cb14ed9547ba15c259c24805eb4cf12c17727c2a4faffe1ada7",
            "linux_arm64": "9bc52b440b5830fe9d2706bc82ee019530846a57dbb60de8ffd36e84d8f3717e",
            "osx_amd64": "29365d0e3a9dc63f224b50564d11e9c9067b756472ee9b4aae01e6ca6d57cca3",
            "osx_arm64": "493c618c0ae5998409145f8467a885e70ef9d3b6312934b86b306817b27dd38c",
        },
    )

    duckdb_patches = True

    resource(
        name="extension_source",
        git="https://github.com/duckdb/ducklake.git",
        commit="417a9117f590e8141742ac0579d02f6a90162e37",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
