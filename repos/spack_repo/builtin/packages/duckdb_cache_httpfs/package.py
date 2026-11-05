# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbCacheHttpfs(DuckdbCommunityExtensionPackage):
    """Adds a read cache for the httpfs filesystem."""

    homepage = "https://github.com/dentiny/duck-read-cache-fs"

    license("MIT")

    site_signed_link_libraries = [("openssl", "ssl"), ("openssl", "crypto"), ("zlib-api", "z")]

    with when("+site_signed"):
        depends_on("curl~nghttp2", type="build")
        depends_on("zlib-api", type="build")

    published_binaries(
        "cache_httpfs",
        "2.0.0",
        {
            "linux_amd64": "4f777b4aefea484b876ae6a4f5187ac3331a2e6d98aa09afef84a34a8f652601",
            "linux_arm64": "5a9b2ef5aff677420a4dffc3026462c056d86b3f21cd989e66043a2f8cec381c",
            "osx_amd64": "e686b4064a26b9e5ad9eaa2fb3efc7a11e118a97f15a3a7af5deaeee54545f8e",
            "osx_arm64": "f009f84905395add4c486329f6c43a60f90668c92b8e92c22271e0071462e6af",
        },
        repository="community",
    )

    resource(
        name="extension_source",
        git="https://github.com/dentiny/duck-read-cache-fs.git",
        commit="62191f711413bb3cf50257b60dd4b44b2de0e3a0",
        submodules=lambda package: ["duckdb-httpfs"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
