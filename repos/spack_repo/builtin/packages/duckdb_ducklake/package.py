# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbDucklake(DuckdbExtensionPackage):
    """Adds support for DuckLake, SQL as a Lakehouse Format."""

    homepage = "https://github.com/duckdb/ducklake"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "4b497cf95d768004d34a97e7098d33f687e994dc523945948c321af25061b39b",
            "linux_arm64": "cfbcc71196d1e7b37e55ea25aeea9a46ae1c05ac1366f2fc760db5a0c9448356",
            "osx_amd64": "16d3c496d4c7924d1b28bfc30cafd54f35074060c460e800580bc5a02c68e9fd",
            "osx_arm64": "78736bf48c045548444dd31ce8e5176dfbcb8df4eb58d8518ce93cb40c3a39bc",
        }
    }
