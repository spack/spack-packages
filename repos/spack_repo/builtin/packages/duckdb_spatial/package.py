# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbSpatial(DuckdbExtensionPackage):
    """Adds support for working with spatial data and functions."""

    homepage = "https://github.com/duckdb/duckdb-spatial"

    # The binary statically links GEOS, which is LGPL-2.1-or-later
    license("MIT AND LGPL-2.1-or-later")

    # From vcpkg.json and the CMakeLists: GDAL (network, geos), PROJ, GEOS, expat, sqlite3 with
    # rtree, zlib, and for network access openssl and curl. Spack's gdal builds only shared
    # libraries, so a source build links them as shared libraries.
    conflicts(
        "link_dependencies=static",
        when="~prebuilt",
        msg="Spack's gdal builds only shared libraries; use link_dependencies=shared",
    )
    with when("link_dependencies=shared"):
        # The vcpkg overlay pins gdal 3.12.4. GDAL 3.13 changed the VSIVirtualHandle Read and
        # Write signatures that src/spatial/modules/gdal/gdal_module.cpp overrides. arrow is
        # a default of gdal that spatial does not use, and a long build.
        depends_on("gdal@3.12.4~arrow+curl+expat+geos+sqlite3", type="link")
        # src/spatial/modules/proj/proj_db.c embeds proj.db from PROJ 9.1.1 (layout 1.2), and
        # the vcpkg overlay pins proj 9.1.1. PROJ 9.7 needs layout 1.6 and refuses it, so LOAD
        # fails with "Could not set proj.db path".
        depends_on("proj@9.1.1", type="link")
        depends_on("geos+shared", type="link")
        depends_on("expat+shared", type="link")
        depends_on("sqlite+rtree", type="link")
        depends_on("zlib-api", type="link")
        depends_on("openssl", type="link")
        depends_on("curl", type="link")

    @run_before("install", when="~prebuilt")
    def adapt_to_spack_gdal_and_sqlite(self):
        # OGRRegisterAllInternal() registers GDAL's built-in drivers. A static GDAL, as vcpkg
        # builds it, resolves it at link time. A shared libgdal does not export it, so LOAD
        # fails with "undefined symbol". OGRRegisterAll() registers the same drivers and also
        # loads plugins from GDAL_DRIVER_PATH, which Spack's gdal does not use.
        modules = join_path(
            self.stage.source_path, "extension_source", "src", "spatial", "modules"
        )
        filter_file(
            r"OGRRegisterAllInternal\(\);",
            "OGRRegisterAll();",
            join_path(modules, "gdal", "gdal_module.cpp"),
        )
        # The embedded proj.db opens through memvfs with a "file:" URI. vcpkg's sqlite3 port
        # compiles SQLITE_USE_URI=1; Spack's sqlite does not, so turn URIs on at run time, which
        # SQLite allows before sqlite3_initialize().
        filter_file(
            r"^(\s*)sqlite3_initialize\(\);",
            r"\1sqlite3_config(SQLITE_CONFIG_URI, 1); sqlite3_initialize();",
            join_path(modules, "proj", "proj_module.cpp"),
        )

    def source_cmake_args(self):
        # The CMakeLists asks for unofficial::sqlite3::sqlite3, a target that only vcpkg's sqlite3
        # port defines. Point it at Spack's sqlite.
        sqlite = self.spec["sqlite"]
        config_dir = join_path(self.stage.path, "unofficial-sqlite3")
        mkdirp(config_dir)
        library = find_libraries("libsqlite3", sqlite.prefix, shared=True, recursive=True)[0]
        with open(join_path(config_dir, "unofficial-sqlite3-config.cmake"), "w") as output:
            output.write("if(NOT TARGET unofficial::sqlite3::sqlite3)\n")
            output.write("  add_library(unofficial::sqlite3::sqlite3 UNKNOWN IMPORTED)\n")
            output.write("  set_target_properties(unofficial::sqlite3::sqlite3 PROPERTIES\n")
            output.write(f'    IMPORTED_LOCATION "{library}"\n')
            output.write(f'    INTERFACE_INCLUDE_DIRECTORIES "{sqlite.prefix.include}")\n')
            output.write("endif()\n")
            output.write("set(unofficial-sqlite3_FOUND 1)\n")
        return [f"-Dunofficial-sqlite3_DIR={config_dir}"]

    published_binaries(
        "spatial",
        "2.0.0",
        {
            "linux_amd64": "8d4bf1ab198806f123821d52ff5131745baaa19d5e91bd6b9772db922d31a228",
            "linux_arm64": "f0bf8e87876af932f529ce0c57015e3ee39954de9c9eb5bc05f5eb9c212f4744",
            "osx_amd64": "fa5ee0e733cf2e8df2812f8ae193734512c80124f5d34c589c62cf799ceb7136",
            "osx_arm64": "16dadc65e6eb5a212160070063b57cc0ded6ebc24cc8c20c401a17a9e0032cee",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-spatial.git",
        commit="a3dbcd1781ec26c3a1be9bd622be05b376d6f47a",
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
