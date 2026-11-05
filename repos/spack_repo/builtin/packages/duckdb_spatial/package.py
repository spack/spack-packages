# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbSpatial(DuckdbExtensionPackage):
    """Adds support for working with spatial data and functions."""

    homepage = "https://github.com/duckdb/duckdb-spatial"

    # The binary statically links GEOS, which is LGPL-2.1-or-later
    license("MIT AND LGPL-2.1-or-later")

    checksums = {
        "2.0.0": {
            "linux_amd64": "8ec99d875355200316c743ede176e2cb50d2b712d2fa192ccbf19cc245a8d0bc",
            "linux_arm64": "93e481c254dad497a365edcedcb9788f2acddb536f6a9e631729314641490847",
            "osx_amd64": "869b28053032a953025043067de9fb4bd22fd4e7bc371f50a295493ddb38f2cc",
            "osx_arm64": "212ca75890f576bec4a9ea71f5a10320581fe9886afceb05b1d47944ebcf03f4",
        }
    }
