# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RDuckdb(RPackage):
    """DBI Package for the DuckDB Database Management System.

    DuckDB is a high-performance analytical in-process SQL database. This
    package provides a DBI-compliant interface to it, and vendors the DuckDB
    C++ engine sources so that no external DuckDB installation is required.
    From 2.0.0, engine=shared (the default) links libduckdb of the duckdb package
    instead, and engine=standalone builds the copy in the package."""

    cran = "duckdb"
    homepage = "https://r.duckdb.org/"

    maintainers("emwjacobson")

    license("MIT", checked_by="emwjacobson")

    version("2.0.0", sha256="23db64ca8054c7984dba06958ae9d530579cb7430831ac4f503f33a44f013741")
    version("1.5.5", sha256="84b14fb3e1e55af6d2b6a75b0d4d18f80036894d1071cb8a9a870ba13329d3cd")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@4.2.0:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))

    variant(
        "engine",
        default="shared",
        values=("shared", "standalone"),
        description="Link libduckdb of the duckdb package, or build the engine in the package",
        when="@2:",
    )

    # configure extracts the vendored src/duckdb.tar.xz engine sources.
    depends_on("xz", type="build", when="@:1")

    # configure checks that libduckdb has the commit of the headers in the package
    depends_on("duckdb@2.0.0", type=("build", "link", "run"), when="@2.0.0 engine=shared")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("engine=shared"):
            env.set("DUCKDB_R_USE_SYSTEM_LIB", "1")
            env.set("DUCKDB_R_LIB_DIR", self.spec["duckdb"].prefix.lib)
