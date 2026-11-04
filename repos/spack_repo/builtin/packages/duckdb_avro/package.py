# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import platform
import shutil

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbAvro(Package):
    """Read Apache Avro files from DuckDB.

    This package installs the signed binary that DuckDB publishes, because DuckDB
    does not load an unsigned extension by default.
    """

    homepage = "https://github.com/duckdb/duckdb-avro"

    maintainers("teaguesterling")

    license("MIT", checked_by="teaguesterling")

    skip_version_audit = ["platform=windows"]

    extension_versions = {
        "2.0.0": {
            "linux": {
                "x86_64": "35447cb42ade2f723f53416ee336dc9ee30ba3584f290e01165398c80f56fd92",
                "aarch64": "1d240802771737ae14695b9d544ecac170832f38dda9a3edcb674ee1d546c2ca",
            },
            "darwin": {
                "x86_64": "e29f724e10580223bfd16eecab7c4646796f2b8f1a4d97902d46730961142c25",
                "arm64": "680ddca413fb5d17169907581a3ca47920fc67d413e9ee54ab3eb6380d3bd1b6",
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
            "/avro.duckdb_extension.gz"
        )

    def install(self, spec, prefix):
        directory = join_path(
            prefix.lib.duckdb.extensions, f"v{spec.version}", self.extension_platform
        )
        mkdirp(directory)
        target = join_path(directory, "avro.duckdb_extension")
        with gzip.open(self.stage.archive_file, "rb") as source, open(target, "wb") as output:
            shutil.copyfileobj(source, output)
