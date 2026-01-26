# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Duckdb(CMakePackage):
    """DuckDB is an in-process SQL OLAP Database Management System."""

    homepage = "https://duckdb.org"
    url = "https://github.com/duckdb/duckdb/archive/refs/tags/v0.9.2.tar.gz"
    git = "https://github.com/duckdb/duckdb.git"

    license("MIT")
    maintainers("glentner", "teaguesterling")

    version("master", branch="master")
    version("1.4.4", sha256="43645e15419c6539bae6915ba397de6569e4a7ca0d502be95d653a78fdb0bece")
    version("1.4.3", sha256="b6a2afd09d9cf07e50d5cd07077df7f7697b61cca2eb00754f5adf89a1ae6c64")
    version("1.4.2", sha256="43193b3661e0f6dce8a1ad9144bbd21c42601fe0e84efee7b3577a4bb160965c")
    version("1.4.1", sha256="91e55efe2c1627c4432d620ee9d2ffcd72f954699e76d7dab523348a7dfbb00a")
    version("1.4.0", sha256="c06d08577555b3f80d19a6e09eec6c2e200b8d0165db4cd775aac97473e53dfc")
    version("1.3.2", sha256="a10b388e516f6d9cc5d571fa55f14c936b73a2ca17400a76aae6c3f1cc2e20cb")
    version("1.3.0", sha256="9c8c5ac0d26f2a97d81867485cf501fd0491ad6ecaf593118cc6122f2fc8924c")
    version("1.2.2", sha256="99387810537dd3f90454e5620ab624405d7f2e0d997aa1e3999316b7969592ed")
    version("1.2.1", sha256="481a05d59cb8eaf4d78e5495ab0c99ed53e3b41e84aeaf24eef4144f2c60d1cc")
    version("1.2.0", sha256="f22c97e18c071fa8e43b5e150c03c6ab4bcc510cca6e6b50cbe13af8535fa701")
    version("1.1.3", sha256="2aea0af898ad753fee82b776fea1bf78ccbc9648986e7f7a87372df5e74cdb98")
    version("1.1.2", sha256="a3319a64c390ed0454c869b2e4fc0af2413cd49f55cd0f1400aaed9069cdbc4c")
    version("1.1.1", sha256="a764cef80287ccfd8555884d8facbe962154e7c747043c0842cd07873b4d6752")
    version("1.1.0", sha256="d9be2c6d3a5ebe2b3d33044fb2cb535bb0bd972a27ae38c4de5e1b4caa4bf68d")

    # Build Options
    variant("icu", default=False, description="Compile with bundled ICU library")
    variant("extension_autoload", default=False, description="Enable extension auto-loading")
    variant("extension_autoinstall", default=False, description="Enable extension auto-installing")
    variant("extension_repo", default=True, description="Copy extensions to prefix")

    # Extensions
    variant("autocomplete", default=True, description="Include autocomplete for CLI in build")
    variant("json", default=True, description="Include JSON support in build")
    variant("parquet", default=True, description="Include parquent support in build")
    variant("tpce", default=False, description="Include TPCE in build")
    variant("tpch", default=False, description="Include TPCH in build")

    # FTS and HTTPFS were moved to an out-of-tree extension in v1.2.0
    variant(
        "fts",
        default=True,
        description="Include FTS (full text search) support in build",
        when="@:1.1",
    )
    variant(
        "httpfs", default=True, description="Include HTTPFS (& S3) support in build", when="@:1.1"
    )

    # APIs
    variant("python", default=True, description="Build with Python driver")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python@3.7:")
    depends_on("openssl", when="+httpfs")
    depends_on("icu4c", when="~icu")

    with when("+python"):
        extends("python")
        depends_on("py-pip", type="build")
        depends_on("py-setuptools-scm", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+python"):
            env.set("SETUPTOOLS_SCM_PRETEND_VERSION", f"{self.spec.version}")
            env.set("PIP_PREFIX", self.prefix)

    def cmake_args(self):
        extensions = ("autocomplete", "icu", "json", "parquet", "tpch", "fts", "httpfs")
        args = [
            self.define(
                "BUILD_EXTENSIONS", [ext for ext in extensions if self.spec.satisfies(f"+{ext}")]
            ),
            self.define("OVERRIDE_GIT_DESCRIBE", f"v{self.spec.version}"),
            self.define("LOCAL_EXTENSION_REPO", self.prefix.lib.duckdb.extensions),
            self.define("ENABLE_EXTENSION_AUTOLOADING", "1"),  # string, not boolean
            self.define("ENABLE_EXTENSION_AUTOINSTALL", "1"),  # string, not boolean
        ]
        if self.spec.satisfies("+python"):
            args.append(self.define("BUILD_PYTHON", "1"))
        if self.spec.satisfies("+tpce"):
            args.append(self.define("BUILD_TPCE", "1"))
        return args
