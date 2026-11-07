# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbCommunityExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbNanoarrow(DuckdbCommunityExtensionPackage):
    """Adds support for the Apache Arrow IPC format.

    This binary has a RUNPATH entry. An install from a build cache has a mode that lets the
    drop_redundant_rpaths hook edit the entry, which makes the signature invalid.
    """

    homepage = "https://github.com/paleolimbot/duckdb-nanoarrow"

    license("MIT")

    with when("+site_signed"):
        depends_on("lz4 libs:=static +pic", type="build")
        depends_on("zstd build_system=cmake", type="build")

    published_binaries(
        "nanoarrow",
        "2.0.0",
        {
            "linux_amd64": "a13cd3c2007fce0f34bda0f2e08d68573a47c2b7b8540f959173d34d646158e9",
            "linux_arm64": "bff5372a4f7d18db78d31b1ec710f09e7ef0a48d7819512e213874c8397dcfb8",
            "osx_amd64": "818d2c65e0fd6034655b7f3f8d38088d4ae38fb60957ed67567d14931bf5b9ed",
            "osx_arm64": "7b529323e6c0db0ee68cf8fb56d452de552a85b0a3d8802dffe3b2ad575929e3",
        },
        repository="community",
    )

    # The extension gets this with CMake FetchContent, with this sha256
    resource(
        name="nanoarrow_c",
        url="https://github.com/apache/arrow-nanoarrow/archive/665794510011c07d4a6932b248608c2c02113796.zip",
        sha256="a81178c68929c74e97cff6b02f9a9f77fc656966ad7dbc4ae858cb45496d6b6f",
        placement="nanoarrow_c",
        when="@2.0.0 +site_signed",
    )

    resource(
        name="extension_source",
        git="https://github.com/paleolimbot/duckdb-nanoarrow.git",
        commit="e390b9b4f8a41e64e41488888defb27d8f1e1421",
        submodules=lambda package: ["arrow-testing"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )

    def site_signed_cmake_args(self):
        source = join_path(self.stage.source_path, "nanoarrow_c")
        return [f"-DFETCHCONTENT_SOURCE_DIR_NANOARROW={source}"]
