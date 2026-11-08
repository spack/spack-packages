# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import gzip
import hashlib
import os
import re
import shutil
import urllib.request
from typing import List, Tuple

from spack_repo.builtin.build_systems.bundle import BundlePackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


def _sha256(source):
    digest = hashlib.sha256()
    for chunk in iter(lambda: source.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest()


#: Libraries that a signed binary can need on Linux, because every system has them
_SYSTEM_LIBRARY = re.compile(
    r"^(libc|libm|libdl|libpthread|librt|libutil|libresolv|libgcc_s|libstdc\+\+|ld-linux.*)\.so"
)

#: The spec that selects each platform that DuckDB publishes for
_PLATFORM_SPECS = {
    "linux_amd64": "platform=linux target=x86_64:",
    "linux_arm64": "platform=linux target=aarch64:",
    "osx_amd64": "platform=darwin target=x86_64:",
    "osx_arm64": "platform=darwin target=aarch64:",
}


#: The host of each DuckDB extension repository
_REPOSITORY_HOSTS = {
    "core": "extensions.duckdb.org",
    "community": "community-extensions.duckdb.org",
}


def published_binaries(name, version, checksums, repository="core"):
    """Declares the published binary for each platform, with the sha256 of the .gz file"""
    host = _REPOSITORY_HOSTS[repository]
    for platform, sha256 in checksums.items():
        resource(
            name="published_binary",
            url=f"https://{host}/v{version}/{platform}/{name}.duckdb_extension.gz",
            sha256=sha256,
            expand=False,
            placement="published_binary",
            when=f"@{version} +prebuilt {_PLATFORM_SPECS[platform]}",
        )


def _install_info(repository, url, full_path, version):
    """Returns the content of the .info file that DuckDB writes beside an installed extension.

    src/include/duckdb/storage/serialization/extension_install_info.json in DuckDB lists the
    fields. This omits the etag and the key fingerprint, which DuckDB does not need to load
    the extension. DuckDB does not write the origin of a core extension, because it is the default.
    """

    def varint(value):
        encoded = bytearray()
        while value > 0x7F:
            encoded.append(value & 0x7F | 0x80)
            value >>= 7
        encoded.append(value)
        return bytes(encoded)

    def text(value):
        return varint(len(value.encode())) + value.encode()

    fields = {100: varint(1), 101: text(full_path), 102: text(url), 103: text(version)}
    if repository == "community":
        fields[105] = varint(1)
    fields[106] = text(repository)
    return b"".join(f.to_bytes(2, "little") + v for f, v in fields.items()) + b"\xff\xff"


class DuckdbExtensionBase(Package):
    """Common base class for a package that installs one DuckDB extension.

    A numbered version is the version of DuckDB that the binary is for. Spack fetches the
    binary and verifies its sha256, so a mirror can supply it. DuckDB verifies the signature
    when it loads the extension.

    @latest gets the binary that DuckDB currently publishes for the version of DuckDB in the
    spec, so the install step needs network access. DuckDB downloads over HTTP. A signature
    does not stop a network attacker who serves an older signed binary, so this class compares
    the file with an HTTPS download of the same file. This does not protect against a bad
    binary at the origin, because both downloads get it. Two installs of one spec can get
    different binaries.

    ~prebuilt builds the extension from source, and does not sign it. This needs duckdb
    trust_unsigned_extension_directories=store: that duckdb loads an unsigned extension only if
    its real path is in the store of the duckdb. A build cache can move the store, because no
    signature becomes invalid. A copy of the file outside the store does not load.

    ~prebuilt +site_signed builds the extension from source, and signs it with a key of your own.
    The file then loads from any place:

    * Build duckdb with extension_keys=...,site and extension_key=<sha256>, where the
      sha256 is of the DER public key. Set DUCKDB_EXTENSION_PUBLIC_KEY for that build.
    * Set DUCKDB_EXTENSION_PRIVATE_KEY to the path of the RSA-2048 private key. This key
      does not go into the spec, the prefix or a build cache. The build of the extension runs
      as the same user, so its code can obtain this key. Thus code that you build can sign
      other code that this DuckDB will load. Use one key for one level of trust.

    In both source builds, a recipe declares the static Spack packages that its extension needs.
    CMake does not look on the host for a library. An extension with a dependency that is not
    declared fails in its build, or in a check of what the binary links.

    For an air gap, put numbered versions and ~prebuilt sources in a mirror, or install
    from a build cache that a connected host made. These installs do not use the network.
    """

    maintainers("teaguesterling")

    # The source of DuckDB. Spack needs a main archive to fetch resources, and ~prebuilt
    # needs its build system for extensions.
    url = "https://github.com/duckdb/duckdb/archive/refs/tags/v2.0.0.tar.gz"

    #: DuckDB extension repository to install from
    repository = "core"

    #: Dependencies whose static library ~prebuilt must link, which CMake does not find itself.
    #: Each is a dependency name and a library name.
    source_link_libraries: List[Tuple[str, str]] = []

    def source_cmake_args(self):
        """Returns other CMake arguments for ~prebuilt, such as a source directory for a
        CMake FetchContent declaration that a resource supplies"""
        return []

    #: True if DuckDB has patches for this extension, in .github/patches/extensions
    duckdb_patches = False

    # A version of an extension package is the DuckDB version that it is for
    version("2.0.0", sha256="7e89053255046bfb26afbd7f524a2fb84df7dbef496aa911ea35e4a1182fdc00")
    version("latest")

    variant(
        "prebuilt",
        default=True,
        sticky=True,
        description="Install the binary that DuckDB publishes and signs, not a build from source",
    )
    variant(
        "site_signed",
        default=False,
        sticky=True,
        description="Sign the build with DUCKDB_EXTENSION_PRIVATE_KEY, so it loads from any place",
        when="~prebuilt",
    )
    variant(
        "link_dependencies",
        default="static",
        values=("static", "shared"),
        description="Link the libraries of Spack dependencies statically, or as shared libraries"
        " that the extension finds through its RUNPATH",
        when="~prebuilt",
    )
    conflicts(
        "link_dependencies=shared",
        when="+site_signed",
        msg="A build cache rewrites the RUNPATH of a shared link, which makes a signature invalid",
    )
    # DuckDB finds these extensions in a view only through DUCKDB_EXTENSION_DIRECTORIES
    extends("duckdb+extension_env")
    depends_on("duckdb@2.0.0", when="@2.0.0")
    depends_on("duckdb extension_keys=site", when="+site_signed")
    depends_on("duckdb trust_unsigned_extension_directories=store", when="~prebuilt ~site_signed")

    conflicts("~prebuilt", when="@latest", msg="@latest is a binary that DuckDB publishes")

    with when("~prebuilt"):
        depends_on("c", type="build")
        depends_on("cxx", type="build")
        depends_on("cmake", type="build")
        depends_on("gmake", type="build")
        depends_on("openssl", type="build")
        depends_on("python", type="build")
    depends_on("openssl", type="link", when="link_dependencies=shared")

    def _links_shared(self):
        return self.spec.satisfies("link_dependencies=shared")

    def _link_library(self, prefix, library):
        """Returns the file of a library to link: the static archive, or with
        link_dependencies=shared the shared library if there is one. Some libraries, such as
        pgcommon_shlib of postgresql, are only static archives."""
        for shared in (True, False) if self._links_shared() else (False,):
            found = find_libraries(f"lib{library}", prefix, shared=shared, recursive=True)
            if found:
                return found[0]
        raise InstallError(f"{self.name}: no lib{library} in {prefix}")

    @property
    def has_code(self):
        return not self.spec.satisfies("@latest")

    @property
    def extension_name(self):
        return self.name[len("duckdb-") :].replace("-", "_")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # The wrappers of Spack add a RUNPATH with the prefix. A build cache rewrites that path
        # when it relocates a file, and this makes the signature invalid.
        if self.spec.satisfies("~prebuilt") and not self._links_shared():
            for name in ("RPATH_DIRS", "STORE_RPATH_DIRS", "COMPILER_EXTRA_RPATHS"):
                env.set(f"SPACK_{name}", "")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.append_path(
            "DUCKDB_EXTENSION_DIRECTORIES", self.prefix.lib.duckdb.extensions, separator=";"
        )

    def _published_sha256(self, platform):
        url = (
            f"https://{_REPOSITORY_HOSTS[self.repository]}/v{self.spec['duckdb'].version}/{platform}/"
            f"{self.extension_name}.duckdb_extension.gz"
        )
        # The server refuses the default user agent of urllib
        request = urllib.request.Request(url, headers={"User-Agent": "Spack"})
        with urllib.request.urlopen(request) as response, gzip.open(response) as source:
            return _sha256(source)

    def _check_binary(self, binary):
        platform = os.path.basename(os.path.dirname(binary))
        expected = self._published_sha256(platform)
        with open(binary, "rb") as source:
            actual = _sha256(source)
        if actual != expected:
            raise InstallError(
                f"{self.name}: the binary for {platform} has sha256 {actual},"
                f" but the HTTPS copy has {expected}."
            )
        tty.msg(f"{self.name}: accepted the binary for {platform}, with sha256 {actual}")

    def _setting(self):
        # INSTALL writes to the first directory. The others hold extension dependencies.
        directories = [self.prefix.lib.duckdb.extensions] + [
            dep.prefix.lib.duckdb.extensions
            for dep in self.spec.dependencies(deptype="run")
            if isinstance(dep.package, DuckdbExtensionBase)
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

    def _check_portable(self, binary):
        """Fails if the binary links a library that Spack would have to relocate.

        A signature prevents any later edit, so such a binary breaks in a build cache. The build
        can also find unsuitable libraries on the host: a build of httpfs linked the host curl,
        loaded without error, and then failed on every HTTP read.
        """
        if not self.spec.satisfies("platform=linux"):
            return
        with open(binary, "rb") as source:
            elf = parse_elf(source, interpreter=False, dynamic_section=True)
        needed = [name.decode() for name in elf.dt_needed_strs]
        external = [name for name in needed if not _SYSTEM_LIBRARY.match(name)]
        if self._links_shared():
            self._check_runpath(binary, elf, external)
            return
        if external or elf.has_rpath:
            raise InstallError(
                f"{self.name} links {external or 'a RUNPATH'}. A source build needs an extension"
                " with no shared dependencies. The recipe must declare static dependencies."
            )

    def _check_runpath(self, binary, elf, external):
        """Fails if a shared library that the binary needs is not in a prefix of a dependency.

        The host must not supply a library. A build cache rewrites a RUNPATH entry only if it
        is in the store.
        """
        runpath = elf.dt_rpath_str.decode().split(":") if elf.has_rpath else []
        # The wrappers also add the lib directories of this prefix
        prefixes = [dep.prefix for dep in self.spec.traverse()]
        outside = [d for d in runpath if d and not any(d.startswith(f"{p}/") for p in prefixes)]
        if outside:
            raise InstallError(
                f"{self.name} has RUNPATH entries outside its dependencies: {outside}"
            )
        missing = [
            name
            for name in external
            if not any(os.path.exists(join_path(d, name)) for d in runpath if d)
        ]
        if missing:
            raise InstallError(
                f"{self.name} links {missing}, which no RUNPATH entry holds. The recipe must"
                " declare these dependencies with a link type."
            )

    def _remove_store_paths(self, binary):
        """Replaces each prefix in the binary with a path of the same length that does not exist.

        A static library can hold the path of its prefix, such as OPENSSLDIR. A build cache
        rewrites those paths when it relocates a file, which makes a signature invalid. So this
        must occur before the signature, and a relocation then has nothing to rewrite. A build
        cache does not relocate an external package, and its prefix can be /usr, so this skips it.
        """
        with open(binary, "rb") as source:
            content = source.read()
        size = len(content)
        for node in self.spec.traverse():
            if not node.external:
                prefix = node.prefix.encode()
                content = content.replace(prefix, b"/nonexistent".ljust(len(prefix), b"/"))
        if len(content) != size:
            raise InstallError(f"{self.name}: a prefix is shorter than its replacement")
        with open(binary, "wb") as output:
            output.write(content)

    def _sign(self, key, source, target, build_dir):
        """Replaces the empty signature in source, as scripts/extension-upload-single.sh does"""
        openssl = Executable(self.spec["openssl"].prefix.bin.openssl)
        der_file = join_path(build_dir, "public.der")
        openssl("pkey", "-in", key, "-pubout", "-outform", "DER", "-out", der_file)
        with open(der_file, "rb") as public_key:
            der = public_key.read()
        actual = hashlib.sha256(der).hexdigest()
        expected = self.spec["duckdb"].variants["extension_key"].value
        if actual != expected:
            raise InstallError(f"The sha256 of the key in {key} is {actual}, not {expected}")
        with open(source, "rb") as binary:
            content = binary.read()[:-256]
        chunks = range(0, len(content), 1024 * 1024)
        hashes = b"".join(hashlib.sha256(content[i : i + 1024 * 1024]).digest() for i in chunks)
        digest = join_path(build_dir, "extension.sha256")
        with open(digest, "wb") as output:
            output.write(hashlib.sha256(hashes).digest())
        signature_file = join_path(build_dir, "extension.sig")
        openssl(
            "pkeyutl",
            "-sign",
            "-inkey",
            key,
            "-pkeyopt",
            "digest:sha256",
            "-in",
            digest,
            "-out",
            signature_file,
        )
        with open(signature_file, "rb") as signature_input:
            signature = signature_input.read()
        if len(signature) != 256:
            raise InstallError(f"The key in {key} is not an RSA-2048 key")
        with open(target, "wb") as output:
            output.write(content + signature)

    def _install_from_source(self, spec, prefix):
        # This keeps the path out of the build environment and its logs, but it is not a boundary.
        # The build runs as the same user, so it can read /proc/<parent>/environ, and then the key.
        key = os.environ.pop("DUCKDB_EXTENSION_PRIVATE_KEY", None)
        if not spec.satisfies("+site_signed"):
            key = None
        elif not key:
            raise InstallError("Set DUCKDB_EXTENSION_PRIVATE_KEY to the path of the private key")
        name = self.extension_name
        source_dir = self.stage.source_path
        extension_dir = join_path(source_dir, "extension_source")
        if self.duckdb_patches:
            patch_files = glob.glob(join_path(source_dir, ".github/patches/extensions", name, "*"))
            with working_dir(extension_dir):
                for patch_file in sorted(f for f in patch_files if f.endswith(".patch")):
                    Executable("patch")("-p1", "-i", patch_file)
        build_dir = join_path(source_dir, "spack-extension-build")
        mkdirp(build_dir)
        config = join_path(build_dir, "extension.cmake")
        with open(config, "w") as output:
            if os.path.isdir(extension_dir):
                output.write(f"duckdb_extension_load({name} SOURCE_DIR {extension_dir})\n")
            else:
                output.write(f"duckdb_extension_load({name})\n")

        # A signature prevents a later edit, so dependencies must be static. project() resets this
        # setting, so it must apply after project(). The host must not supply a library.
        # With link_dependencies=shared, there is no signature, and a build cache rewrites the
        # RUNPATH. Then CMake can take the shared library of a dependency.
        static_first = join_path(build_dir, "static_first.cmake")
        with open(static_first, "w") as output:
            if not self._links_shared():
                output.write('set(CMAKE_FIND_LIBRARY_SUFFIXES ".a" ".so")\n')

        # The extension links the static library of DuckDB, so nothing compiles DuckDB here
        lib = spec["duckdb"].prefix.lib
        archives = [os.path.basename(a)[3:-2] for a in glob.glob(join_path(lib, "libduckdb_*.a"))]
        libraries = " ".join(f"-l{a}" for a in archives if a != "duckdb_static")
        # These go at the end of the link line, because the linker reads a static library in order
        late_libraries = " ".join(
            self._link_library(spec[dep].prefix, library)
            for dep, library in self.source_link_libraries
        )
        with working_dir(build_dir):
            Executable(spec["cmake"].prefix.bin.cmake)(
                source_dir,
                "-DCMAKE_BUILD_TYPE=Release",
                f"-DOVERRIDE_GIT_DESCRIBE=v{self.version}",
                f"-DDUCKDB_EXTENSION_CONFIGS={config}",
                "-DBUILD_EXTENSIONS_ONLY=TRUE",
                "-DBUILD_SHELL=FALSE",
                "-DBUILD_UNITTESTS=FALSE",
                # The default profile adds -march=x86-64-v3, whatever the target of the spec
                "-DDUCKDB_OPTIMIZATION_PROFILE=NONE",
                f"-DCMAKE_PROJECT_INCLUDE={static_first}",
                "-DCMAKE_IGNORE_PREFIX_PATH=/;/usr;/usr/local",
                "-DCMAKE_SKIP_RPATH=ON",
                # A build that downloads during CMake fails in an air gap, and it gets code that
                # no recipe declared. So a download fails here too, and a resource supplies it.
                "-DFETCHCONTENT_FULLY_DISCONNECTED=ON",
                f"-DCMAKE_CXX_STANDARD_LIBRARIES={late_libraries}",
                *self.source_cmake_args(),
                f"-DCMAKE_SHARED_LINKER_FLAGS=-L{lib}",
                f"-DDUCKDB_EXTRA_LINK_FLAGS=-Wl,--start-group {libraries} -Wl,--end-group",
            )
            make(f"{name}_loadable_extension")
            with open("duckdb_platform_out") as platform_file:
                platform = platform_file.read().strip()
            target_dir = join_path(prefix.lib.duckdb.extensions, f"v{self.version}", platform)
            mkdirp(target_dir)
            binary = join_path(target_dir, f"{name}.duckdb_extension")
            built = join_path("extension", name, f"{name}.duckdb_extension")
            self._check_portable(built)
            if key is None:
                # No signature, so a build cache can rewrite the store paths
                install(built, binary)
                return binary
            self._remove_store_paths(built)
            self._sign(key, built, binary, build_dir)
        return binary

    def _install_fetched(self, spec, prefix):
        """Installs the binary that Spack fetched and verified.

        INSTALL trusts only the core keys for a local file. So this puts the binary where INSTALL
        would, with the .info file that records its origin. DuckDB uses that origin to select
        the signing keys, and it verifies the signature at each load.
        """
        name = self.extension_name
        archives = glob.glob(join_path(self.stage.source_path, "published_binary", "*.gz"))
        if len(archives) != 1:
            raise InstallError(f"{self.name}@{self.version} has no binary here. Use @latest.")
        local = join_path(self.stage.source_path, f"{name}.duckdb_extension")
        with gzip.open(archives[0], "rb") as source, open(local, "wb") as output:
            shutil.copyfileobj(source, output)
        # The footer has eight fields of 32 bytes, and then the signature of 256 bytes.
        # DuckDB refuses a .info file with a version that is different from the footer.
        with open(local, "rb") as source:
            source.seek(-512, os.SEEK_END)
            footer = source.read(256)
        platform, extension_version = (
            footer[offset : offset + 32].rstrip(b"\0").decode() for offset in (192, 128)
        )
        target_dir = join_path(prefix.lib.duckdb.extensions, f"v{self.version}", platform)
        mkdirp(target_dir)
        binary = join_path(target_dir, f"{name}.duckdb_extension")
        shutil.move(local, binary)
        url = f"http://{_REPOSITORY_HOSTS[self.repository]}"
        full_path = f"{url}/v{self.version}/{platform}/{name}.duckdb_extension.gz"
        with open(f"{binary}.info", "wb") as output:
            output.write(_install_info(self.repository, url, full_path, extension_version))
        return binary

    def _install_published(self, spec, prefix):
        """Installs the binary that DuckDB fetches, with a check of the file"""
        name = self.extension_name
        target = prefix.lib.duckdb.extensions
        mkdirp(target)
        Executable(spec["duckdb"].prefix.bin.duckdb)(
            "-c", f"{self._setting()} INSTALL {name} FROM {self.repository};"
        )
        (binary,) = glob.glob(join_path(target, "*", "*", f"{name}.duckdb_extension"))
        self._check_binary(binary)
        return binary

    def install(self, spec, prefix):
        if spec.satisfies("~prebuilt"):
            binary = self._install_from_source(spec, prefix)
        elif spec.satisfies("@latest"):
            binary = self._install_published(spec, prefix)
        else:
            binary = self._install_fetched(spec, prefix)
        self._check_load(Executable(spec["duckdb"].prefix.bin.duckdb))
        # After this step, the drop_redundant_rpaths hook removes a RUNPATH entry for a directory
        # that does not exist, which makes the signature invalid. It skips a read-only file.
        os.chmod(binary, 0o444)

    def test_load(self):
        """check that DuckDB accepts the installed extension, after the Spack hooks have run"""
        self._check_load(which(self.spec["duckdb"].prefix.bin.duckdb))


class DuckdbExtensionPackage(DuckdbExtensionBase):
    """Base class for a package that installs one DuckDB core extension."""

    depends_on("duckdb extension_keys=core", when="+prebuilt")


class DuckdbCommunityExtensionPackage(DuckdbExtensionBase):
    """Base class for a package that installs one DuckDB community extension.

    DuckDB replaces a community binary at the same URL for each release of the extension,
    so the sha256 of a numbered version soon fails unless a mirror has that binary. Thus
    @latest is the default here.
    """

    repository = "community"

    version("latest", preferred=True)

    depends_on("duckdb extension_keys=community", when="+prebuilt")


class DuckdbExtensions(BundlePackage):
    """Selects core DuckDB extensions, with one variant for each extension.

    The variants exclude extensions that DuckDB links statically, such as json and parquet.
    They also exclude autocomplete and tpch, because a DuckDB build can provide those files.

    To use the extensions, install them in an environment with a view:

        spack:
          specs:
          - duckdb-extensions@2.0.0 +httpfs +fts +spatial
          view: true

    DuckDB finds them through DUCKDB_EXTENSION_DIRECTORIES. duckdb+extension_env sets this
    variable when you activate the environment, or when you use spack load.

    * @2.0.0 installs the binaries that DuckDB published. It works from a mirror.
    * @latest installs the binaries that DuckDB publishes now, so it needs network access.
    * ~prebuilt builds each extension from source, with no signature. The duckdb in the spec
      loads these files only from its own store: see trust_unsigned_extension_directories.
    * ~prebuilt +site_signed builds each extension from source and signs it with your key. The
      duckdb in the spec must trust that key: see its extension_keys and extension_key variants.

    The base class DuckdbExtensionBase describes each mode and its limits.
    """

    homepage = "https://duckdb.org/docs/stable/core_extensions/overview"

    maintainers("teaguesterling")

    version("2.0.0")
    version("latest")

    variant(
        "prebuilt",
        default=True,
        sticky=True,
        description="Install the binaries that DuckDB publishes, not builds from source",
    )
    variant(
        "site_signed",
        default=False,
        sticky=True,
        description="Sign the builds with your own key, so they load from any place",
        when="~prebuilt",
    )
    depends_on("duckdb+extension_env", type="run")
    depends_on("duckdb@2.0.0", type="run", when="@2.0.0")

    conflicts("~prebuilt", when="@latest", msg="@latest is a binary that DuckDB publishes")

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
        _package = f"duckdb-{_name.replace('_', '-')}"
        for _when in ("@2.0.0", "@latest", "+prebuilt", "~prebuilt ~site_signed", "+site_signed"):
            depends_on(f"{_package}{_when}", type="run", when=f"+{_name} {_when}")
