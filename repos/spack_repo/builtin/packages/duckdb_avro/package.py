# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbAvro(DuckdbExtensionPackage):
    """Adds support for reading Avro files."""

    homepage = "https://github.com/duckdb/duckdb-avro"

    license("MIT")

    with when("+site_signed"):
        depends_on("jansson~shared", type="build")
        depends_on("snappy~shared+pic", type="build")
        depends_on("xz", type="build")
        depends_on("zlib-api", type="build")

    published_binaries(
        "avro",
        "2.0.0",
        {
            "linux_amd64": "35447cb42ade2f723f53416ee336dc9ee30ba3584f290e01165398c80f56fd92",
            "linux_arm64": "1d240802771737ae14695b9d544ecac170832f38dda9a3edcb674ee1d546c2ca",
            "osx_amd64": "e29f724e10580223bfd16eecab7c4646796f2b8f1a4d97902d46730961142c25",
            "osx_arm64": "680ddca413fb5d17169907581a3ca47920fc67d413e9ee54ab3eb6380d3bd1b6",
        },
    )

    duckdb_patches = True

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-avro.git",
        commit="345c3f4e821940233b0b889e815582e5a5a33dfe",
        submodules=lambda package: ["third_party/avro-c"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
