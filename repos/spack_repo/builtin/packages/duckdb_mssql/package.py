# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbMssql(DuckdbExtensionPackage):
    """Adds support for connecting to Microsoft SQL Server."""

    homepage = "https://github.com/hugr-lab/mssql-extension"

    license("MIT")

    repository = "community"

    checksums = {
        "2.0.0": {
            "linux_amd64": "473b2980d494df2a0653ec9a8a82588ae102a9ab25d5a2b117a6e9fcd5fc20c5",
            "linux_arm64": "e717f77da19902180ffd22394b9055ffad14fcd9e021c93fb440de8405399cb5",
            "osx_arm64": "901e15176048311f1c9c01cba5944ceba31e7c367327a62b7ae881a7029a4bbe",
        }
    }
