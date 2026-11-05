# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbDuckpgq(DuckdbCommunityExtensionPackage):
    """Adds support for SQL/PGQ and graph algorithms."""

    homepage = "https://github.com/cwida/duckpgq-extension"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "4bcbed6acaf0cba2abbce90ece60198911fcb6229fae07d7263d7f60a2badc59",
            "linux_arm64": "d01ddb39dc519c765386a39891805bbbc3afee829a55015b2adec153a769b916",
            "osx_amd64": "35d02af0e8cd1cf8779d3b134c60db7bef396414a73cca032130ce383dbcc229",
            "osx_arm64": "4ebefd0fe88d4b31ca6ca89a6fcb77b2343dd8dda032ee7df74310cedddc5faf",
        }
    }
