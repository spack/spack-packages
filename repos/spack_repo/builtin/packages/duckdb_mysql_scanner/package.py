# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbMysqlScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a MySQL database."""

    homepage = "https://github.com/duckdb/duckdb-mysql"

    license("MIT")

    published_binaries(
        "mysql_scanner",
        "2.0.0",
        {
            "linux_amd64": "edfc8d927178c32b740064f18f292c3fc67f62de32d6a61874fef7cca3d12591",
            "linux_arm64": "9beb65e9b2c48465f90d37f89191907c128531f770ab11e7ffb198ca94a3ed83",
            "osx_amd64": "722188fad8640c93757e1bc6b5895a77027aaf1e7894a5013d5fd795fa57a46a",
            "osx_arm64": "cbed90305daf0dd5c74f52b8775712d2065fd34763deddba18f11196c69c38ad",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-mysql.git",
        commit="f7fc0d42716534aa5ad48626d21ced9807b33967",
        submodules=lambda package: ["database-connector"],
        placement="extension_source",
        when="@2.0.0 +site_signed",
    )
