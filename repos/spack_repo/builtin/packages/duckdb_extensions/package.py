# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DuckdbExtensionPackage(Package):
    """Base class for a package that installs one signed DuckDB extension.

    The install step uses DuckDB to get the binary that DuckDB currently publishes for
    this DuckDB version and platform, so the step needs network access. Spack has no
    checksum for the binary, and a later install can get a different binary. DuckDB
    verifies the signature when it loads the extension, and the install step loads it.
    A .info file beside the extension records its origin.
    """

    maintainers("teaguesterling")

    has_code = False

    #: DuckDB extension repository to install from
    repository = "core"

    # A version of an extension package is the DuckDB version that it is for
    version("2.0.0")

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

    def install(self, spec, prefix):
        duckdb = Executable(spec["duckdb"].prefix.bin.duckdb)
        name = self.extension_name
        target = prefix.lib.duckdb.extensions
        # INSTALL writes to the first directory. The others hold extension dependencies.
        directories = [target] + [
            dep.prefix.lib.duckdb.extensions
            for dep in spec.dependencies(deptype="run")
            if isinstance(dep.package, DuckdbExtensionPackage)
        ]
        quoted = ", ".join(f"'{directory}'" for directory in directories)
        setting = f"SET extension_directories=[{quoted}];"
        mkdirp(target)
        duckdb("-c", f"{setting} INSTALL {name} FROM {self.repository};")
        # LOAD fails for a bad signature or a missing dependency. The query fails for an
        # extension that this DuckDB links statically, where LOAD does not read the file.
        duckdb(
            "-c",
            f"{setting} LOAD {name};"
            f" SELECT CASE WHEN starts_with(install_path, '{target}/') THEN 'ok'"
            f" ELSE error('{name} did not load from the prefix: ' || install_path) END"
            f" FROM duckdb_extensions() WHERE extension_name = '{name}';",
        )


class DuckdbExtensions(BundlePackage):
    """Selects core DuckDB extensions, with one variant for each extension.

    The variants exclude extensions that DuckDB links statically, such as json and parquet.
    They also exclude autocomplete and tpch, because a DuckDB build can provide those files.
    """

    homepage = "https://duckdb.org/docs/stable/core_extensions/overview"

    maintainers("teaguesterling")

    version("2.0.0")

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
        depends_on(f"duckdb-{_name.replace('_', '-')}", type="run", when=f"+{_name}")
