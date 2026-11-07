# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbSpatial(DuckdbExtensionPackage):
    """Adds support for working with spatial data and functions."""

    homepage = "https://github.com/duckdb/duckdb-spatial"

    # The binary statically links GEOS, which is LGPL-2.1-or-later
    license("MIT AND LGPL-2.1-or-later")

    published_binaries(
        "spatial",
        "2.0.0",
        {
            "linux_amd64": "8d4bf1ab198806f123821d52ff5131745baaa19d5e91bd6b9772db922d31a228",
            "linux_arm64": "f0bf8e87876af932f529ce0c57015e3ee39954de9c9eb5bc05f5eb9c212f4744",
            "osx_amd64": "fa5ee0e733cf2e8df2812f8ae193734512c80124f5d34c589c62cf799ceb7136",
            "osx_arm64": "16dadc65e6eb5a212160070063b57cc0ded6ebc24cc8c20c401a17a9e0032cee",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-spatial.git",
        commit="a3dbcd1781ec26c3a1be9bd622be05b376d6f47a",
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
