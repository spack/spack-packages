# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import platform
import shutil

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbHttpfs(Package):
    """HTTP(S) and S3 file system support for DuckDB.

    This package installs the signed binary that DuckDB publishes, because DuckDB
    does not load an unsigned extension by default.
    """

    homepage = "https://github.com/duckdb/duckdb-httpfs"

    maintainers("teaguesterling")

    license("MIT", checked_by="teaguesterling")

    skip_version_audit = ["platform=windows"]

    extension_versions = {
        "2.0.0": {
            "linux": {
                "x86_64": "ee6c7d7e60a5da1b6f6bf6156b4298b55ddce0496a5bfe628bd6ab6d47eb8e3e",
                "aarch64": "f524888fc7d74cc0c6c4a8f7ed5beedac5b12e71cb426503f882c72ce6afbd43",
            },
            "darwin": {
                "x86_64": "75b333cbf8c9a23eaaa9831166527020fd876ed772d1243c0af52027742d0a76",
                "arm64": "6aea2d728cb7eedb978ca264ce190e31284271e9ea4f68b2424bf20806b46638",
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
            "/httpfs.duckdb_extension.gz"
        )

    def install(self, spec, prefix):
        directory = join_path(
            prefix.lib.duckdb.extensions, f"v{spec.version}", self.extension_platform
        )
        mkdirp(directory)
        target = join_path(directory, "httpfs.duckdb_extension")
        with gzip.open(self.stage.archive_file, "rb") as source, open(target, "wb") as output:
            shutil.copyfileobj(source, output)
