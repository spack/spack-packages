# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbQuack(DuckdbExtensionPackage):
    """Adds the DuckDB Quack client and server protocol."""

    homepage = "https://github.com/duckdb/duckdb-quack"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "9c893bd543ec2c5253d0c47d5614f90a1bfa1791c735dc6bbcea4e8bd3811a97",
            "linux_arm64": "f3e30e7533f53e2b935ec29b59f87cb26ec3afaacb9880e9072426a6d16ced9e",
            "osx_amd64": "f34e0cf0a876bd4f08d842b79cbd38645b2e7b341911054e6b129b449a777e56",
            "osx_arm64": "ef547f01cb30412aa6dbade59bdd5254ed897ba4f113a1700e3e01e00a747935",
        }
    }
