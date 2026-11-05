# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbEncodings(DuckdbExtensionPackage):
    """Converts Unicode encodings to UTF-8."""

    homepage = "https://github.com/duckdb/duckdb-encodings"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "0ad735a8d700cb4edf03cf98c9f7168a3dc08d85b08214fbb2ee970055265a36",
            "linux_arm64": "24fb3ab6046d9cc476199bc1c42b4f9a43e90e8955333bde06c80498d7d6c871",
            "osx_amd64": "c9a869c0e0873a08ecc1f1fecc163ed2d1a8c558d9b045844a44313e39d141b8",
            "osx_arm64": "79c9e2ec36d0e26cf4a222420647b5650be41d44c635925a5dd5d2ffc1e0f6c3",
        }
    }
