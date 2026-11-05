# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbVortex(DuckdbExtensionPackage):
    """Adds support for reading and writing files using the Vortex file format."""

    homepage = "https://github.com/vortex-data/duckdb-vortex"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "4e04613ca366178fffd39b52eee88fcdffd656506435c38e17a5999b06b655e6",
            "linux_arm64": "d7062b5459660181a1bfbb981e2f0d24c46697145d08bca14ecc92a37fbcbdbf",
            "osx_arm64": "8485abe7be357227deaaffd3161fee2585e719313fc1078ef2c66c83fe9f9466",
        }
    }
