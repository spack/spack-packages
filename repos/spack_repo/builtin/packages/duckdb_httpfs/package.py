# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbHttpfs(DuckdbExtensionPackage):
    """Adds support for reading and writing files over a HTTP(S) connection."""

    homepage = "https://github.com/duckdb/duckdb-httpfs"

    license("MIT")

    source_link_libraries = [("zlib-api", "z")]

    with when("~prebuilt"):
        depends_on("curl~nghttp2", type="build")
        depends_on("zlib-api", type="build")
    with when("link_dependencies=shared"):
        depends_on("curl", type="link")
        depends_on("zlib-api", type="link")

    published_binaries(
        "httpfs",
        "2.0.0",
        {
            "linux_amd64": "ee6c7d7e60a5da1b6f6bf6156b4298b55ddce0496a5bfe628bd6ab6d47eb8e3e",
            "linux_arm64": "f524888fc7d74cc0c6c4a8f7ed5beedac5b12e71cb426503f882c72ce6afbd43",
            "osx_amd64": "75b333cbf8c9a23eaaa9831166527020fd876ed772d1243c0af52027742d0a76",
            "osx_arm64": "6aea2d728cb7eedb978ca264ce190e31284271e9ea4f68b2424bf20806b46638",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-httpfs.git",
        commit="77392a72077a85897db2519fae11e2c0da972b8a",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
