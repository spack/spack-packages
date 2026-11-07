# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbAws(DuckdbExtensionPackage):
    """Provides features that depend on the AWS SDK."""

    homepage = "https://github.com/duckdb/duckdb-aws"

    license("MIT")

    published_binaries(
        "aws",
        "2.0.0",
        {
            "linux_amd64": "f6e8b47c1f0aba8313fd571dc179ecf766c8c6c88842b04efbe54b5d9340f7bc",
            "linux_arm64": "73c715031b8e47c6e29700697d7df654517d53d9e26442b1e672d1672bfe767d",
            "osx_amd64": "f0af72ba63505c34d61d93b7f504b7f58f5df33a33c06abc6604e574acca2415",
            "osx_arm64": "957801b0fba913fc3f493a9fdd7bb9f1c22950247e8ee25f1a9d81138b71cb5a",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-aws.git",
        commit="16ae9c135300f750478d648c2496f2952a6f2827",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
