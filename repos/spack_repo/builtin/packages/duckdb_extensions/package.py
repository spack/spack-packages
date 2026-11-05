# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import gzip
import hashlib
import os
import urllib.request
from typing import Dict

from spack_repo.builtin.build_systems.bundle import BundlePackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


def _sha256(source):
    digest = hashlib.sha256()
    for chunk in iter(lambda: source.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


class DuckdbExtensionPackage(Package):
    """Base class for a package that installs one signed DuckDB extension.

    The install step uses DuckDB to get the binary that DuckDB publishes for this DuckDB
    version and platform, so the step needs network access. DuckDB downloads over HTTP,
    and it verifies the signature when it installs and loads the extension. A signature
    does not stop a network attacker who serves an older signed binary, so this class
    also checks the sha256 of the binary before the first load:

    * +pinned compares with the checksums attribute. An install fails if DuckDB publishes
      a new binary, until the package has the new checksum. This is the default here.
    * ~pinned gets whichever binary is current, and compares with an HTTPS download of
      the same file. Two installs of one spec can get different binaries.
    """

    maintainers("teaguesterling")

    has_code = False

    #: DuckDB extension repository to install from
    repository = "core"

    #: sha256 of the decompressed binary, by DuckDB version and DuckDB platform
    checksums: Dict[str, Dict[str, str]] = {}

    # A version of an extension package is the DuckDB version that it is for
    version("2.0.0")

    variant("pinned", default=True, description="Require the binary that the package records")

    # DuckDB finds these extensions in a view only through DUCKDB_EXTENSION_DIRECTORIES
    extends("duckdb+extension_env")
    depends_on("duckdb@2.0.0", when="@2.0.0")

    @property
    def extension_name(self):
        return self.name[len("duckdb-") :].replace("-", "_")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.append_path(
            "DUCKDB_EXTENSION_DIRECTORIES", self.prefix.lib.duckdb.extensions, separator=";"
        )

    def _published_sha256(self, platform):
        host = {"core": "extensions", "community": "community-extensions"}[self.repository]
        url = (
            f"https://{host}.duckdb.org/v{self.version}/{platform}/"
            f"{self.extension_name}.duckdb_extension.gz"
        )
        # The server refuses the default user agent of urllib
        request = urllib.request.Request(url, headers={"User-Agent": "Spack"})
        with urllib.request.urlopen(request) as response, gzip.open(response) as source:
            return _sha256(source)

    def _check_binary(self, binary):
        platform = os.path.basename(os.path.dirname(binary))
        if self.spec.satisfies("+pinned"):
            expected = self.checksums.get(str(self.version), {}).get(platform)
            if not expected:
                raise InstallError(
                    f"{self.name} has no checksum for {platform}. Use ~pinned to skip the pin."
                )
        else:
            expected = self._published_sha256(platform)
        with open(binary, "rb") as source:
            actual = _sha256(source)
        if actual != expected:
            raise InstallError(
                f"{self.name}: the binary for {platform} has sha256 {actual}, expected {expected}."
                " DuckDB can republish a binary. Use ~pinned to accept the current binary."
            )

    def _setting(self):
        # INSTALL writes to the first directory. The others hold extension dependencies.
        directories = [self.prefix.lib.duckdb.extensions] + [
            dep.prefix.lib.duckdb.extensions
            for dep in self.spec.dependencies(deptype="run")
            if isinstance(dep.package, DuckdbExtensionPackage)
        ]
        quoted = ", ".join(f"'{directory}'" for directory in directories)
        return f"SET extension_directories=[{quoted}];"

    def _check_load(self, duckdb):
        # LOAD fails for a bad signature or a missing dependency. The query fails for an
        # extension that this DuckDB links statically, where LOAD does not read the file.
        name = self.extension_name
        duckdb(
            "-c",
            f"{self._setting()} LOAD {name};"
            f" SELECT CASE WHEN starts_with(install_path, '{self.prefix}/') THEN 'ok'"
            f" ELSE error('{name} did not load from the prefix: ' || install_path) END"
            f" FROM duckdb_extensions() WHERE extension_name = '{name}';",
        )

    def install(self, spec, prefix):
        duckdb = Executable(spec["duckdb"].prefix.bin.duckdb)
        name = self.extension_name
        target = prefix.lib.duckdb.extensions
        mkdirp(target)
        duckdb("-c", f"{self._setting()} INSTALL {name} FROM {self.repository};")
        (binary,) = glob.glob(join_path(target, "*", "*", f"{name}.duckdb_extension"))
        self._check_binary(binary)
        self._check_load(duckdb)
        # After this step, the drop_redundant_rpaths hook removes a RUNPATH entry for a directory
        # that does not exist, which makes the signature invalid. It skips a read-only file.
        os.chmod(binary, 0o444)

    def test_load(self):
        """check that DuckDB accepts the installed extension, after the Spack hooks have run"""
        self._check_load(which(self.spec["duckdb"].prefix.bin.duckdb))


class DuckdbCommunityExtensionPackage(DuckdbExtensionPackage):
    """Base class for a package that installs one signed DuckDB community extension.

    DuckDB replaces a community binary at the same URL for each release of the extension,
    so a pin soon has no binary that can satisfy it. Thus ~pinned is the default here.
    """

    repository = "community"

    variant("pinned", default=False, description="Require the binary that the package records")


class DuckdbExtensions(BundlePackage):
    """Selects core DuckDB extensions, with one variant for each extension.

    The variants exclude extensions that DuckDB links statically, such as json and parquet.
    They also exclude autocomplete and tpch, because a DuckDB build can provide those files.
    """

    homepage = "https://duckdb.org/docs/stable/core_extensions/overview"

    maintainers("teaguesterling")

    version("2.0.0")

    variant("pinned", default=True, description="Require the binaries that the packages record")

    depends_on("duckdb@2.0.0+extension_env", type="run", when="@2.0.0")

    for _name in (
        "avro",
        "aws",
        "azure",
        "delta",
        "ducklake",
        "encodings",
        "excel",
        "fts",
        "httpfs",
        "iceberg",
        "inet",
        "lance",
        "legacy_parser",
        "mysql_scanner",
        "postgres_scanner",
        "quack",
        "spatial",
        "sqlite_scanner",
        "sqlsmith",
        "tpcds",
        "unity_catalog",
        "vortex",
        "vss",
    ):
        variant(_name, default=_name == "httpfs", description=f"Install the {_name} extension")
        for _pin in ("+pinned", "~pinned"):
            depends_on(
                f"duckdb-{_name.replace('_', '-')}{_pin}", type="run", when=f"+{_name} {_pin}"
            )
