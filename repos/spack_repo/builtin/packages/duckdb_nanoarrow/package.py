# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbNanoarrow(DuckdbCommunityExtensionPackage):
    """Adds support for the Apache Arrow IPC format."""

    homepage = "https://github.com/paleolimbot/duckdb-nanoarrow"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "90938f61850c1507ab4cf2453831e85daa73cdf712664ffc525ca82fbd0b8825",
            "linux_arm64": "ff5218a03e4f23160c65963499c671ca2bef16ecc41e728a8f6ec5486dccadb2",
            "osx_amd64": "2c68da600bb02a5e9437d8e63628acc1d7fd552d05f3a6a68de377ac308ef06b",
            "osx_arm64": "3b1eff88f62eaa3b2f2098d27ed58bb0809edf98368a1f5b18654e95f6284283",
        }
    }
