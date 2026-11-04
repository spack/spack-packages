# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import gzip
import platform
import shutil

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbVss(Package):
    """Vector similarity search indexes for DuckDB.

    This package installs the signed binary that DuckDB publishes, because DuckDB
    does not load an unsigned extension by default.
    """

    homepage = "https://github.com/duckdb/duckdb-vss"

    maintainers("teaguesterling")

    license("MIT", checked_by="teaguesterling")

    skip_version_audit = ["platform=windows"]

    extension_versions = {
        "2.0.0": {
            "linux": {
                "x86_64": "02d1ae4508e00cf0dae89f713683f4bf0622774eaa4154398945b77134fdfc3a",
                "aarch64": "e4bf5cb45febe9ecaf14fd2daea914d8c8f197e37a58338e3c9db0868064a267",
            },
            "darwin": {
                "x86_64": "b4b4785d221bfde3f48ab9aaf7decf7561d05f4266bb4ec713dcaea990290681",
                "arm64": "4d24e0543efb77376e58297aba11054abefd726207eb98dd57ef112bca146456",
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
            "/vss.duckdb_extension.gz"
        )

    def install(self, spec, prefix):
        directory = join_path(
            prefix.lib.duckdb.extensions, f"v{spec.version}", self.extension_platform
        )
        mkdirp(directory)
        target = join_path(directory, "vss.duckdb_extension")
        with gzip.open(self.stage.archive_file, "rb") as source, open(target, "wb") as output:
            shutil.copyfileobj(source, output)
