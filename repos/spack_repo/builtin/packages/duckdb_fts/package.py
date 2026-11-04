# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import platform
import shutil

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbFts(Package):
    """Full-text search indexes for DuckDB.

    This package installs the signed binary that DuckDB publishes, because DuckDB
    does not load an unsigned extension by default.
    """

    homepage = "https://github.com/duckdb/duckdb-fts"

    maintainers("teaguesterling")

    license("MIT", checked_by="teaguesterling")

    skip_version_audit = ["platform=windows"]

    extension_versions = {
        "2.0.0": {
            "linux": {
                "x86_64": "9172520652ce609d163cf30645f382b197f2c7294448a816c77d62b0f029d96e",
                "aarch64": "d233d2311825da4d9b6efb45edd52b126b18134c7d7083b1e58f6d450ebdabee",
            },
            "darwin": {
                "x86_64": "9b9fe0d2925953f9b2ebb60f5914d5224b49e72fa36849b8372f80c980b7e454",
                "arm64": "fa5eef362e1f004d19c08d76ed4ec47d181d8feb07ca3b528f3058ee8945362b",
            },
        }
    }

    extension_platforms = {
        "linux": {"x86_64": "linux_amd64", "aarch64": "linux_arm64"},
        "darwin": {"x86_64": "osx_amd64", "arm64": "osx_arm64"},
    }

    system = platform.system().lower()
    machine = platform.machine().lower()

    for ver in extension_versions:
        if system in extension_versions[ver] and machine in extension_versions[ver][system]:
            version(ver, sha256=extension_versions[ver][system][machine], expand=False)
            depends_on(f"duckdb@{ver}", when=f"@{ver}")

    # DuckDB finds this package in a view only through DUCKDB_EXTENSION_DIRECTORIES
    extends("duckdb+extension_env")

    @property
    def extension_platform(self):
        return self.extension_platforms[self.system][self.machine]

    def url_for_version(self, version):
        return (
            f"http://extensions.duckdb.org/v{version}/{self.extension_platform}"
            "/fts.duckdb_extension.gz"
        )

    def install(self, spec, prefix):
        directory = join_path(
            prefix.lib.duckdb.extensions, f"v{spec.version}", self.extension_platform
        )
        mkdirp(directory)
        target = join_path(directory, "fts.duckdb_extension")
        with gzip.open(self.stage.archive_file, "rb") as source, open(target, "wb") as output:
            shutil.copyfileobj(source, output)
