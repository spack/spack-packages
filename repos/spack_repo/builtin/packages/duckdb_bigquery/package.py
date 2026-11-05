# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbCommunityExtensionPackage

from spack.package import *


class DuckdbBigquery(DuckdbCommunityExtensionPackage):
    """Adds support for querying Google BigQuery."""

    homepage = "https://github.com/hafenkran/duckdb-bigquery"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "97aca2d0506cb32d906ddbe5e8f1b5b2cc353c5330d7eabf79feafa173e6d866",
            "linux_arm64": "89551ede0984dc460b8910d9b2bcae254c420734e6f10b5cb5d3b537bf171da1",
            "osx_amd64": "a38a92bd77b5097cd9afeffa3b3a551fd1c3b98ff1ae2561e733dd846da115fc",
            "osx_arm64": "db9caf61c4ef06679399608648dd2658b84c4eb352832cffd5d34659260462ad",
        }
    }
