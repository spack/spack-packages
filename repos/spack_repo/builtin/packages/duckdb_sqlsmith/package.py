# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbSqlsmith(DuckdbExtensionPackage):
    """Adds the SQLsmith query generator to DuckDB."""

    homepage = "https://github.com/duckdb/duckdb-sqlsmith"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "0ef28de8f0fede6bc4e6fec59f0e90023ba7b7ab9cca1b6f67c22701bf0e966f",
            "linux_arm64": "5529e3734ed06adf2970406e8fe95bf9342a1cdb06ff8d759c67046ddac3ed21",
            "osx_amd64": "875f43dac05154d60ecca3469fed394ad23ca204f91a923bc89fb094c9c3f3ff",
            "osx_arm64": "43b34a8d67a7d8eaa268740794f1b0e73d02acb4da6f26be2ebf9769334e5e48",
        }
    }
