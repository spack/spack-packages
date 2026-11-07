# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import base64
import binascii
import hashlib
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

PEM_BEGIN = "-----BEGIN PUBLIC KEY-----"
PEM_END = "-----END PUBLIC KEY-----"


def extension_public_key(fingerprint):
    """Returns the PEM public key in DUCKDB_EXTENSION_PUBLIC_KEY, after a check of its sha256.

    The spec holds only the sha256, so a different key gets a different hash. The file is
    outside of the spec, and it does not go into a build cache.
    """
    path = os.environ.get("DUCKDB_EXTENSION_PUBLIC_KEY")
    if not path:
        raise InstallError("Set DUCKDB_EXTENSION_PUBLIC_KEY to the path of the PEM public key")
    with open(path) as source:
        lines = source.read().strip().splitlines()
    if len(lines) < 3 or lines[0] != PEM_BEGIN or lines[-1] != PEM_END:
        raise InstallError(f"The file {path} is not one PEM public key")
    try:
        der = base64.b64decode("".join(lines[1:-1]), validate=True)
    except binascii.Error as error:
        raise InstallError(f"The file {path} is not one PEM public key: {error}")
    actual = hashlib.sha256(der).hexdigest()
    if actual != fingerprint:
        raise InstallError(f"The sha256 of the key in {path} is {actual}, not {fingerprint}")
    # An extension signature has 256 bytes, so only RSA-2048 fits
    if len(der) != 294:
        raise InstallError(f"The key in {path} is not an RSA-2048 public key")
    # Build from the verified bytes, so that no other text in the file reaches the C++ header
    body = base64.b64encode(der).decode()
    rows = [body[i : i + 64] for i in range(0, len(body), 64)]
    return "\n".join([PEM_BEGIN, *rows, PEM_END, ""])


class Duckdb(CMakePackage):
    """DuckDB is an in-process SQL OLAP Database Management System."""

    homepage = "https://duckdb.org"
    url = "https://github.com/duckdb/duckdb/archive/refs/tags/v2.0.0.tar.gz"
    git = "https://github.com/duckdb/duckdb.git"

    license("MIT")
    maintainers("glentner", "teaguesterling")

    extendable = True

    version("master", branch="master")
    version("2.0.0", sha256="7e89053255046bfb26afbd7f524a2fb84df7dbef496aa911ea35e4a1182fdc00")
    version("1.5.6", sha256="1fadcbe9e69e1470f9093b6bcde08daf477d729c449e59a807f45c346622099b")
    version("1.5.5", sha256="f33155ff962e6e1e08fd1e9caffa487d4325aa60999e2eabc76feff534d6558b")
    version("1.5.4", sha256="99c36e4bf415f295e19ed67401adb72e075e63e6a0dc3a14312c986e29781fd0")
    version("1.5.2", sha256="6d8612fc87115cf4d3512a934ada5d1669db29378b4cc8e226fdfa8f5c537385")
    version("1.5.1", sha256="2de9901f05d445e6a24b79127fd70f2e4fbd552b44dc1dc668aca07fbf97f716")
    version("1.5.0", sha256="fb039699c5a91dec9876540aed7904b6b4e713b800014840dbf641168147a556")
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
    # v2.0.0 removed the ICU library and always statically links the icu extension
    variant("icu", default=False, description="Compile with bundled ICU library", when="@:1.5")
    variant("extension_autoload", default=False, description="Enable extension auto-loading")
    variant("extension_autoinstall", default=False, description="Enable extension auto-installing")
    variant("extension_repo", default=True, description="Copy extensions to prefix")
    variant(
        "extension_directories",
        default="none",
        values=str,
        description="Extra directory to search for extensions, after ~/.duckdb/extensions",
        when="@1.5:",
    )
    variant(
        "extension_env",
        default=False,
        description="Also search DUCKDB_EXTENSION_DIRECTORIES, set to the prefix or view on load",
        when="@2.0.0",
    )

    variant(
        "extension_keys",
        values=("core", "community", "site"),
        default="core,community",
        multi=True,
        description="Which signing keys to trust for extensions",
        when="@2.0.0",
    )
    variant(
        "extension_key",
        default="none",
        values=str,
        description="sha256 of the DER public key to trust for site, as DuckDB reports it",
        when="@2.0.0 extension_keys=site",
    )
    conflicts(
        "extension_key=none",
        when="extension_keys=site",
        msg="extension_keys=site needs extension_key=<sha256 of the public key>",
    )

    variant(
        "trust_unsigned_extension_directories",
        default="none",
        values=("none", "store"),
        description="Load an unsigned extension if its real path is in the store of this duckdb",
        when="@2.0.0",
    )
    # A service that runs SQL from others, as a user that can write files where others put them,
    # must not use this: such a file can be a store, and LOAD can then run its code.
    variant(
        "trust_owned_spack_stores",
        default=False,
        description="Also load an unsigned extension from a Spack store that only root or the user"
        " can write, such as a user store that chains to this one",
        when="@2.0.0 trust_unsigned_extension_directories=store",
    )

    # Extensions that a version always links statically. An extension package must not provide
    # these. Update this table for each new version, and check the duckdb-extensions variants.
    builtin_extensions = {"@2.0.0": ["core_functions", "icu", "json", "parquet", "shell"]}

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
    # The Python client moved to the duckdb/duckdb-python repository in v1.4.0
    variant("python", default=True, description="Build with Python driver", when="@:1.3")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("python@3.7:", type="build")
    depends_on("openssl", when="+httpfs")
    depends_on("icu4c", when="@:1.5 ~icu")

    # Also turns off the automatic install by default, which fails for an extension that is
    # only in a later search directory. An explicit INSTALL still works.
    patch("extension_env.patch", when="@2.0.0 +extension_env")

    patch("extension_trust.patch", when="@2.0.0 trust_unsigned_extension_directories=store")

    # A build with the default keys does not need this patch
    for _keys in (
        "core",
        "community",
        "site",
        "core,site",
        "community,site",
        "core,community,site",
    ):
        patch("extension_keys.patch", when=f"@2.0.0 extension_keys:={_keys}")

    with when("+python"):
        extends("python")
        depends_on("py-pip", type="build")
        depends_on("py-setuptools-scm", type="build")

    def patch(self):
        keys = self.spec.variants.get("extension_keys")
        if keys is None or set(keys.value) == {"core", "community"}:
            return
        lines = ["#pragma once"]
        for name in ("core", "community"):
            lines.append(f"#define DUCKDB_EXTENSION_KEYS_{name.upper()} {int(name in keys.value)}")
        if "site" in keys.value:
            pem = extension_public_key(self.spec.variants["extension_key"].value)
            lines.append(f'#define DUCKDB_EXTENSION_KEYS_SITE R"({pem})"')
        with open("src/include/duckdb/main/extension_keys.hpp", "w") as header:
            header.write("\n".join(lines) + "\n")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+python"):
            env.set("SETUPTOOLS_SCM_PRETEND_VERSION", f"{self.spec.version}")
            env.set("PIP_PREFIX", self.prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+extension_env"):
            env.append_path(
                "DUCKDB_EXTENSION_DIRECTORIES", self.prefix.lib.duckdb.extensions, separator=";"
            )

    #: The commit of each release. A release archive has no git metadata, so the build would
    #: report the placeholder 0123456789 as its source_id. A client that links libduckdb, such
    #: as r-duckdb, compares this commit with the commit of its own headers.
    release_commits = {"2.0.0": "d54cbbe3df17e8e5ce68312f483b4155836112aa"}

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
        if self.spec.satisfies("@2:"):
            # The default profile adds -march=x86-64-v3 or armv8-a, whatever the target of the
            # spec. NONE leaves the target flags to the compiler wrapper of Spack.
            args.append(self.define("DUCKDB_OPTIMIZATION_PROFILE", "NONE"))
        commit = self.release_commits.get(str(self.spec.version))
        if commit:
            args.append(self.define("GIT_COMMIT_HASH", commit))
        if self.spec.satisfies("@1.5:"):
            extension_directory = self.spec.variants["extension_directories"].value
            if extension_directory != "none":
                # The first directory is where INSTALL writes, so keep the writable default first
                args.append(
                    self.define(
                        "EXTENSION_DIRECTORIES", ["~/.duckdb/extensions", extension_directory]
                    )
                )
        if self.spec.satisfies("trust_unsigned_extension_directories=store"):
            # The root of the store that holds the code that loads, found at load time. An
            # extension that loads another extension has its own copy of that code. A
            # downstream store of the user did not exist when this duckdb was built.
            directories = ["$SPACK_STORE"]
            if self.spec.satisfies("+trust_owned_spack_stores"):
                directories.append("$OWNED_SPACK_STORE")
            args.append(self.define("TRUSTED_EXTENSION_DIRECTORIES", directories))
        if self.spec.satisfies("+python"):
            args.append(self.define("BUILD_PYTHON", "1"))
        if self.spec.satisfies("+tpce"):
            args.append(self.define("BUILD_TPCE", "1"))
        return args

    def test_builtin_extensions(self):
        """check which extensions this version links statically"""
        for when, names in self.builtin_extensions.items():
            if self.spec.satisfies(when):
                break
        else:
            raise SkipTest("This version has no record of its built-in extensions")
        # The query fails on a difference, so that the test does not depend on the output format
        duckdb = which(self.prefix.bin.duckdb)
        duckdb(
            "-c",
            f"SELECT CASE WHEN found = {sorted(names)} AND versions = ['v{self.spec.version}']"
            " THEN 'ok' ELSE error('Built-in extensions differ: ' || found::VARCHAR"
            " || ' at ' || versions::VARCHAR) END FROM (SELECT list_sort(list(extension_name))"
            " AS found, list_distinct(list(extension_version)) AS versions"
            " FROM duckdb_extensions() WHERE install_mode = 'STATICALLY_LINKED');",
        )
