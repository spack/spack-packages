# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbUnityCatalog(DuckdbExtensionPackage):
    """Adds support for connecting to Unity Catalog."""

    homepage = "https://github.com/duckdb/unity_catalog"

    license("MIT")

    published_binaries(
        "unity_catalog",
        "2.0.0",
        {
            "linux_amd64": "948d60b90d45c958173db5a1e40992fbe047e0e023b64483235c79c2c52ee8c3",
            "linux_arm64": "93aaeab253b3b26626f7e1ee162add17ba169739a9ebef9fc091ccb19e457d50",
            "osx_amd64": "954cfd20ed17f3dc309d18a6137cb9c2000df687baf7960087547c8e4eb17af4",
            "osx_arm64": "20e979f23c3d354141d783089c400dd2b030a953ecc67767116fc45ab8b7662c",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/unity_catalog.git",
        commit="cc59382f5292997293a57c2ab336c9aa97c05f2d",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
