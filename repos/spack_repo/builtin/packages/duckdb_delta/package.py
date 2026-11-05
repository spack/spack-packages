# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbDelta(DuckdbExtensionPackage):
    """Adds support for Delta Lake."""

    homepage = "https://github.com/duckdb/duckdb-delta"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "b5752785d55c13f46c834ecef2a28281e889d53663f0a264f3ae65453e54a0a3",
            "linux_arm64": "2fdb5dd97200d8bed562456cdea5821d41191b3255c3fb115c08e14aa3566b74",
            "osx_amd64": "2c8ebdd076adb927eabdb9c113274668fd63054d87c3a3820b8aa40f8e1e1bbc",
            "osx_arm64": "ac23fdd1d3f09ea150b488cfc514c050fc7c6b6e0e40cd71989575bed49e4c29",
        }
    }
