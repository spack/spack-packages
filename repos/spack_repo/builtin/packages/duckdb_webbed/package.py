# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbWebbed(DuckdbCommunityExtensionPackage):
    """Adds support for processing XML and HTML."""

    homepage = "https://github.com/teaguesterling/duckdb_webbed"

    license("MIT")

    source_link_libraries = [("libiconv", "iconv"), ("zlib-api", "z")]

    with when("~prebuilt"):
        depends_on("libiconv", type="build")
        depends_on("libxml2~shared+pic", type="build")
        depends_on("zlib-api", type="build")

    published_binaries(
        "webbed",
        "2.0.0",
        {
            "linux_amd64": "9bc53738760de708fba73bccc6d82893bb0a8abba7eee9d22b551e6611802d26",
            "linux_arm64": "f3482fde1df832b3e82cc8168a3a9d61dd5b770078e81397f785f6bc68d2c208",
            "osx_amd64": "cd03e1e73060b6d60be5505f19c8e2eb4deb5c0ef436fb9bb1483612965364de",
            "osx_arm64": "2d9e0946ffdcb408821f1c79274d94687fba38cc50a920694e3405dc20b7265e",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/teaguesterling/duckdb_webbed.git",
        commit="18c22232ebdb387014f4e024c5e41a2326358c88",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
