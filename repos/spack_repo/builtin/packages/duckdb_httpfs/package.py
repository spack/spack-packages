# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbHttpfs(DuckdbExtensionPackage):
    """Adds support for reading and writing files over a HTTP(S) connection."""

    homepage = "https://github.com/duckdb/duckdb-httpfs"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "77e6c429aa04f25da7962572f12b19113e0ce46080fa1365ad66017aadcdb68d",
            "linux_arm64": "53f7aea1a0448ea62ef9b63f95da37c5766070084f14f14110e275e76382e7b2",
            "osx_amd64": "0bfd8ca53a2ce0434ee52f99b7d1695098b8c1c0557128f7c3d5d06b0881badf",
            "osx_arm64": "c2d72a98ad081bf4d62c908b8d9f60b70ab1b83faa9141fc7e7d53526658761d",
        }
    }
