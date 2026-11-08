# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.duckdb_extensions.package import (
    DuckdbExtensionPackage,
    published_binaries,
)

from spack.package import *


class DuckdbMysqlScanner(DuckdbExtensionPackage):
    """Adds support for connecting to a MySQL database."""

    homepage = "https://github.com/duckdb/duckdb-mysql"

    license("MIT")

    # From vcpkg.json: libmariadb. vcpkg links its client plugins statically.
    with when("~prebuilt"):
        depends_on("pkgconfig", type="build")
        depends_on("mariadb-c-client+static_plugins", type="build")
    with when("link_dependencies=shared"):
        depends_on("mariadb-c-client+static_plugins", type="link")

    @run_before("install", when="~prebuilt")
    def write_libmariadb_config(self):
        """The CMakeLists sets libmariadb_DIR to an overlay of vcpkg's port, which expects the
        unofficial::libmariadb target that only vcpkg's patched build exports. Replace that
        config with one that names Spack's mariadb-c-client."""
        mariadb = self.spec["mariadb-c-client"]
        include = join_path(mariadb.prefix.include, "mariadb")
        if self._links_shared():
            # libmariadb.so finds its own dependencies through its RUNPATH
            libraries = [self._link_library(mariadb.prefix, "mariadb")]
        else:
            pkgconf = Executable(join_path(self.spec["pkgconfig"].prefix.bin, "pkg-config"))
            # An external node, such as glibc, can have the prefix /usr: never search it
            deps = [dep for dep in mariadb.traverse(deptype="link") if not dep.external]
            pc_dirs = [
                join_path(dep.prefix, lib, "pkgconfig") for dep in deps for lib in ("lib", "lib64")
            ]
            flags = pkgconf(
                "--static",
                "--libs",
                "libmariadb",
                output=str,
                extra_env={"PKG_CONFIG_PATH": ":".join(pc_dirs)},
            ).split()
            # A bare -lssl would let the linker take the host's library, so each -l becomes
            # the static archive from mariadb's own Spack dependencies
            system = {"pthread", "dl", "m", "rt", "resolv"}
            libraries = []
            for name in (f[2:] for f in flags if f.startswith("-l")):
                if name in system:
                    libraries.append(f"-l{name}")
                    continue
                # Spack's mariadb-c-client names its static archive libmariadbclient.a
                lookup = "mariadbclient" if name == "mariadb" else name
                archive = next(
                    (
                        found[0]
                        for dep in deps
                        for found in [
                            find_libraries(
                                f"lib{lookup}", dep.prefix, shared=False, recursive=True
                            )
                        ]
                        if found
                    ),
                    None,
                )
                if archive is None:
                    raise InstallError(f"{self.name}: no static lib{lookup} for -l{name}")
                libraries.append(archive)
        config = join_path(
            self.stage.source_path,
            "extension_source",
            "vcpkg_ports",
            "libmariadb",
            "libmariadb-config.cmake",
        )
        with open(config, "w") as output:
            output.write("set(libmariadb_FOUND 1)\n")
            # The CMakeLists overwrites MYSQL_INCLUDE_DIR after find_package, so add the directory
            # here. A config file runs in the caller's scope, so src/ inherits it.
            output.write(f'include_directories("{include}")\n')
            output.write(f"set(MYSQL_LIBRARIES {' '.join(libraries)})\n")

    published_binaries(
        "mysql_scanner",
        "2.0.0",
        {
            "linux_amd64": "edfc8d927178c32b740064f18f292c3fc67f62de32d6a61874fef7cca3d12591",
            "linux_arm64": "9beb65e9b2c48465f90d37f89191907c128531f770ab11e7ffb198ca94a3ed83",
            "osx_amd64": "722188fad8640c93757e1bc6b5895a77027aaf1e7894a5013d5fd795fa57a46a",
            "osx_arm64": "cbed90305daf0dd5c74f52b8775712d2065fd34763deddba18f11196c69c38ad",
        },
    )

    resource(
        name="extension_source",
        git="https://github.com/duckdb/duckdb-mysql.git",
        commit="f7fc0d42716534aa5ad48626d21ced9807b33967",
        submodules=lambda package: ["database-connector"],
        placement="extension_source",
        when="@2.0.0 ~prebuilt",
    )
