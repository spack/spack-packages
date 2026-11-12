# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RDuckdb(RPackage):
    """DBI Package for the DuckDB Database Management System.

    DuckDB is a high-performance analytical in-process SQL database. This
    package provides a DBI-compliant interface to it, and vendors the DuckDB
    C++ engine sources so that no external DuckDB installation is required."""

    cran = "duckdb"
    homepage = "https://r.duckdb.org/"

    maintainers("emwjacobson")

    license("MIT", checked_by="emwjacobson")

    version("1.5.5", sha256="84b14fb3e1e55af6d2b6a75b0d4d18f80036894d1071cb8a9a870ba13329d3cd")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@4.2.0:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))

    # configure extracts the vendored src/duckdb.tar.xz engine sources.
    depends_on("xz", type="build")
