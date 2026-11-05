# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbPostgresScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a Postgres database."""

    homepage = "https://github.com/duckdb/duckdb-postgres"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "39e661c5cfb678c9472f5acd88235f84f3ef4126e7444c7c8a01214d9b291601",
            "linux_arm64": "822cb8a5d336416ff5705a309d2dc99b3fd20e98e019e8c60bd3d6507ea5ceec",
            "osx_amd64": "c49d3bf088cc4f0782a9b10d8914462e2246dda983de645b00e54e21561ed1d1",
            "osx_arm64": "679573480436252e527d8d3f3848aee74adebbe08918fb2c34d21d8fa252e765",
        }
    }
