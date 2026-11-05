# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import DuckdbExtensionPackage

from spack.package import *


class DuckdbAws(DuckdbExtensionPackage):
    """Provides features that depend on the AWS SDK."""

    homepage = "https://github.com/duckdb/duckdb-aws"

    license("MIT")

    checksums = {
        "2.0.0": {
            "linux_amd64": "25737495d8957052cd3a468c1a9c2f09f289a6fb098ab0a31ae22f6bf50bc55d",
            "linux_arm64": "33b055e1e9a4c1c1a0590ba74571e5f62121fbc9e9fa52e89e796916ac8b0c6a",
            "osx_amd64": "c25dc171e7311ae1e6ac68edc775423bc8021c714e05167389022dde5798af4e",
            "osx_arm64": "2a4c7b58b70d6a4f77947b2ddaaa7e095d279c499e1036f4edaa2f4fc2d304a6",
        }
    }
