# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDuckdb(PythonPackage):
    """DuckDB Python client.

    Split out of the duckdb repository in v1.4.0. The sdist carries a copy of
    the DuckDB sources and links them statically, so this shares nothing with
    the duckdb package; a database written by one is read by the other as long
    as the reader's version is at least the writer's.
    """

    homepage = "https://duckdb.org/docs/stable/clients/python/overview"
    pypi = "duckdb/duckdb-1.5.2.tar.gz"
    git = "https://github.com/duckdb/duckdb-python.git"

    license("MIT")

    version("1.5.5", sha256="72f33ee57ca7595b23957671a2cc7f7fe2be0ecc2d68f63abedcfcaa3a5c1238")
    version("1.5.2", sha256="638da0d5102b6cb6f7d47f83d0600708ac1d3cb46c5e9aaabc845f9ba4d69246")
    version("1.4.5", sha256="783779bde612172b06c250b5f34f7fc29471833545f2894aadedbffbbcc49013")

    depends_on("cxx", type="build")
    depends_on("cmake@3.29:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-scikit-build-core@0.11.4:", type="build")
    depends_on("py-pybind11@2.6:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # An sdist has no git metadata, where the version scheme would
        # otherwise fall back to 0.0.1.dev1.
        env.set("OVERRIDE_GIT_DESCRIBE", f"v{self.spec.version}")
