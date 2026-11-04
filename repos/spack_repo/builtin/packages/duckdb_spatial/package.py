# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import platform
import shutil

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbSpatial(Package):
    """Geospatial types and functions for DuckDB.

    This package installs the signed binary that DuckDB publishes, because DuckDB
    does not load an unsigned extension by default.
    """

    homepage = "https://github.com/duckdb/duckdb-spatial"

    maintainers("teaguesterling")

    license("MIT", checked_by="teaguesterling")

    skip_version_audit = ["platform=windows"]

    extension_versions = {
        "2.0.0": {
            "linux": {
                "x86_64": "8d4bf1ab198806f123821d52ff5131745baaa19d5e91bd6b9772db922d31a228",
                "aarch64": "f0bf8e87876af932f529ce0c57015e3ee39954de9c9eb5bc05f5eb9c212f4744",
            },
            "darwin": {
                "x86_64": "fa5ee0e733cf2e8df2812f8ae193734512c80124f5d34c589c62cf799ceb7136",
                "arm64": "16dadc65e6eb5a212160070063b57cc0ded6ebc24cc8c20c401a17a9e0032cee",
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
            "/spatial.duckdb_extension.gz"
        )

    def install(self, spec, prefix):
        directory = join_path(
            prefix.lib.duckdb.extensions, f"v{spec.version}", self.extension_platform
        )
        mkdirp(directory)
        target = join_path(directory, "spatial.duckdb_extension")
        with gzip.open(self.stage.archive_file, "rb") as source, open(target, "wb") as output:
            shutil.copyfileobj(source, output)
