# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import pathlib
import re

from spack_repo.builtin.build_systems import autotools
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Binutils(AutotoolsPackage, GNUMirrorPackage):
    """GNU binutils, which contain the linker, assembler, objdump and others"""

    homepage = "https://www.gnu.org/software/binutils/"
    gnu_mirror_path = "binutils/binutils-2.28.tar.bz2"

    maintainers("alalazo")

    tags = ["build-tools", "core-packages"]

    executables = ["^nm$", "^readelf$"]

    license(
        "GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later",
        checked_by="tgamblin",
    )
    version("2.46.0", sha256="0f3152632a2a9ce066f20963e9bb40af7cf85b9b6c409ed892fd0676e84ecd12")
    version("2.45.1", sha256="860daddec9085cb4011279136fc8ad29eb533e9446d7524af7f517dd18f00224")
    version("2.45", sha256="1393f90db70c2ebd785fb434d6127f8888c559d5eeb9c006c354b203bab3473e")
    version("2.44", sha256="f66390a661faa117d00fab2e79cf2dc9d097b42cc296bf3f8677d1e7b452dc3a")
    version("2.43.1", sha256="becaac5d295e037587b63a42fad57fe3d9d7b83f478eb24b67f9eec5d0f1872f")
    version("2.43", sha256="fed3c3077f0df7a4a1aa47b080b8c53277593ccbb4e5e78b73ffb4e3f265e750")
    version("2.42", sha256="aa54850ebda5064c72cd4ec2d9b056c294252991486350d9a97ab2a6dfdfaf12")
    version("2.41", sha256="a4c4bec052f7b8370024e60389e194377f3f48b56618418ea51067f67aaab30b")
    version("2.40", sha256="f8298eb153a4b37d112e945aa5cb2850040bcf26a3ea65b5a715c83afe05e48a")
    version("2.39", sha256="da24a84fef220102dd24042df06fdea851c2614a5377f86effa28f33b7b16148")
    version("2.38", sha256="070ec71cf077a6a58e0b959f05a09a35015378c2d8a51e90f3aeabfe30590ef8")
    version("2.37", sha256="67fc1a4030d08ee877a4867d3dcab35828148f87e1fd05da6db585ed5a166bd4")
    version("2.36.1", sha256="5b4bd2e79e30ce8db0abd76dd2c2eae14a94ce212cfc59d3c37d23e24bc6d7a3")
    version("2.35.2", sha256="cfa7644dbecf4591e136eb407c1c1da16578bd2b03f0c2e8acdceba194bb9d61")
    version("2.35.1", sha256="320e7a1d0f46fcd9f413f1046e216cbe23bb2bce6deb6c6a63304425e48b1942")
    version("2.35", sha256="7d24660f87093670738e58bcc7b7b06f121c0fcb0ca8fc44368d675a5ef9cff7")
    version("2.34", sha256="89f010078b6cf69c23c27897d686055ab89b198dddf819efb0a4f2c38a0b36e6")
    version("2.33.1", sha256="0cb4843da15a65a953907c96bad658283f3c4419d6bcc56bf2789db16306adb2")
    version("2.32", sha256="de38b15c902eb2725eac6af21183a5f34ea4634cb0bcef19612b50e5ed31072d")
    version("2.31.1", sha256="ffcc382695bf947da6135e7436b8ed52d991cf270db897190f19d6f9838564d0")
    version("2.30", sha256="efeade848067e9a03f1918b1da0d37aaffa0b0127a06b5e9236229851d9d0c09")

    variant("plugins", default=True, description="enable plugins, needed for gold linker")
    # When you build ld.gold you automatically get ld, even when you add the
    # --disable-ld flag
    variant("gold", default=False, when="+ld", description="build the gold linker")
    variant("libiberty", default=False, description="Also install libiberty.")
    variant("nls", default=False, description="Enable Native Language Support")
    variant("headers", default=False, description="Install extra headers (e.g. ELF)")
    variant("lto", default=False, description="Enable lto.")
    variant(
        "pgo",
        default=False,
        description="Build with profile-guided optimization (slow)",
        when="@2.37:",
    )
    variant("ld", default=False, description="Enable ld.")
    variant("gas", default=False, description="Enable as assembler.")
    variant("interwork", default=False, description="Enable interwork.")
    variant("gprofng", default=False, description="Enable gprofng.", when="@2.39:")
    variant(
        "libs",
        default="shared,static",
        values=("shared", "static"),
        multi=True,
        description="Build shared libs, static libs or both",
    )
    variant(
        "compress_debug_sections",
        default="zlib",
        values=(conditional("zstd", when="@2.40:"), "zlib", "none"),
        description="Enable debug section compression by default in ld, gas, gold.",
    )
    variant(
        "debuginfod",
        default=False,
        description="Enable debuginfod HTTP server support for readelf and objdump",
        when="@2.34:",
    )

    # 2.36 is missing some dependencies, this patch allows a parallel build.
    # https://sourceware.org/bugzilla/show_bug.cgi?id=27482
    patch("parallel-build-2.36.patch", when="@2.36")
    patch("gold-gcc4.patch", when="@2.42 %gcc@:4.8.5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # compression libs for debug symbols.
    depends_on("zstd@1.4.0:", when="@2.40:")
    depends_on("zlib-api")

    depends_on("elfutils+debuginfod", when="+debuginfod")

    # pkg-config is used to locate zstd, libdebuginfod
    depends_on("pkgconfig", type="build")
    depends_on("diffutils", type="build")

    depends_on("gettext", when="+nls")

    # PGO runs tests, which requires `runtest` from dejagnu
    depends_on("dejagnu", when="+pgo", type="build")

    # 2.34:2.40 needs makeinfo due to a bug, see:
    # https://sourceware.org/bugzilla/show_bug.cgi?id=25491
    # https://sourceware.org/bugzilla/show_bug.cgi?id=28909
    depends_on("texinfo", type="build", when="@2.34:2.40")

    # gprofng requires bison
    depends_on("bison@3.0.4:", type="build", when="+gprofng")

    with when("platform=darwin"):
        conflicts("+gold", msg="Binutils cannot build linkers on macOS")
        # 2.41 doesn't seem to have any problems.
        conflicts(
            "libs=shared",
            when="@2.37:2.40,2.42:",
            msg="https://github.com/spack/spack/issues/35817",
        )

    conflicts(
        "~lto", when="+pgo", msg="Profile-guided optimization enables link-time optimization"
    )

    # When you build binutils with ~ld and +gas and load it in your PATH, you
    # may end up with incompatibilities between a potentially older system ld
    # and a recent assembler. For instance the linker on ubuntu 16.04 from
    # binutils 2.26 and the assembler from binutils 2.36.1 will result in:
    # "unable to initialize decompress status for section .debug_info"
    # when compiling with debug symbols on gcc.
    conflicts("+gas", "~ld", msg="Assembler not always compatible with system ld")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"GNU (nm|readelf).* (\S+)", output)
        return Version(match.group(2)).dotted.up_to(3) if match else None

    @classmethod
    def determine_variants(cls, exes, version_str):
        bin_dir = pathlib.Path(exes[0]).parent
        include_dir = bin_dir.parent / "include"
        plugin_h = include_dir / "plugin-api.h"

        variants = "+gold" if find(str(bin_dir), "gold", recursive=False) else "~gold"
        if find(str(include_dir), str(plugin_h), recursive=False):
            variants += "+headers"
        else:
            variants += "~headers"

        return variants

    def flag_handler(self, name, flags):
        spec = self.spec

        # Set -O3 -g0 by default when using gcc or clang, since it improves performance
        # a bit and significantly reduces install size
        if name in ("cflags", "cxxflags") and self.compiler.name in ("gcc", "clang"):
            flags.insert(0, "-g0")
            flags.insert(0, "-O3")

        # Use a separate variable for injecting flags. This way, installing
        # `binutils cflags='-O2'` will still work as expected.
        iflags = []
        # To ignore the errors of narrowing conversions for
        # the Fujitsu compiler
        if name == "cxxflags" and (
            spec.satisfies("@:2.31.1") and self.compiler.name in ("fj", "clang", "apple-clang")
        ):
            iflags.append("-Wno-narrowing")
        elif name == "cflags":
            if spec.satisfies("@:2.34 %gcc@10:") or spec.satisfies("%cce"):
                iflags.append("-fcommon")
        elif name == "ldflags":
            if spec.satisfies("%cce") or spec.satisfies("@2.38 %gcc"):
                iflags.append("-Wl,-z,notext")
        return (iflags, None, flags)

    def test_binaries(self):
        """check versions reported by binaries"""
        binaries = [
            "ar",
            "c++filt",
            "coffdump",
            "dlltool",
            "elfedit",
            "gprof",
            "ld",
            "nm",
            "objdump",
            "ranlib",
            "readelf",
            "size",
            "strings",
        ]

        # Since versions can have mixed separator characters after the minor
        # version, just check the first two components
        version = str(self.spec.version.up_to(2))
        for _bin in binaries:
            reason = "checking version of {0} is {1}".format(_bin, version)
            with test_part(self, "test_binaries_{0}".format(_bin), purpose=reason):
                installed_exe = join_path(self.prefix.bin, _bin)
                if not os.path.exists(installed_exe):
                    raise SkipTest("{0} is not installed".format(_bin))

                exe = which(installed_exe)
                out = exe("--version", output=str.split, error=str.split)
                assert version in out


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def configure_args(self):
        known_targets = {"x86_64": "x86_64", "aarch64": "aarch64", "ppc64le": "powerpc"}
        known_platforms = {"linux": "linux-gnu", "darwin": "apple-darwin"}

        family = str(self.spec.target.family)
        platform = self.spec.platform

        if family in known_targets and platform in known_platforms:
            targets = "{}-{}".format(known_targets[family], known_platforms[platform])
        else:
            targets = "all"

        args = [
            "--disable-dependency-tracking",
            "--disable-werror",
            "--enable-64-bit-bfd",
            "--enable-deterministic-archives",
            "--enable-multilib",
            "--enable-pic",
            "--enable-targets={}".format(targets),
            "--with-sysroot=/",
            "--with-system-zlib",
            *self.enable_or_disable("gas"),
            *self.enable_or_disable("gold"),
            *self.enable_or_disable("gprofng"),
            *self.enable_or_disable("install-libiberty", variant="libiberty"),
            *self.enable_or_disable("interwork"),
            *self.enable_or_disable("ld"),
            *self.enable_or_disable("libs"),
            *self.enable_or_disable("lto"),
            *self.enable_or_disable("nls"),
            *self.enable_or_disable("plugins"),
            *self.with_or_without("debuginfod"),
        ]
        if self.spec.satisfies("+pgo"):
            args.append("--enable-pgo-build=lto")
        else:
            args.append("--disable-pgo-build")

        # Compressed debug symbols by default. Note that the "default" flag only applies
        # to 2.40: but since it is ignored in earlier versions, that is not a problem.
        if self.spec.satisfies("compress_debug_sections=zlib"):
            args.append("--enable-compressed-debug-sections=all")
            args.append("--enable-default-compressed-debug-sections-algorithm=zlib")
        elif self.spec.satisfies("compress_debug_sections=zstd"):
            args.append("--enable-compressed-debug-sections=all")
            args.append("--enable-default-compressed-debug-sections-algorithm=zstd")

        # To avoid namespace collisions with Darwin/BSD system tools,
        # prefix executables with "g", e.g., gar, gnm; see Homebrew
        # https://github.com/Homebrew/homebrew-core/blob/master/Formula/binutils.rb
        if self.spec.satisfies("platform=darwin"):
            args.append("--program-prefix=g")

        return args

    @run_after("install", when="+headers")
    def install_headers(self):
        # some packages (like TAU) need the ELF headers, so install them
        # as a subdirectory in include/extras
        extradir = join_path(self.prefix.include, "extra")
        mkdirp(extradir)
        # grab the full binutils set of headers
        install_tree("include", extradir)
        # also grab the headers from the bfd directory
        install(join_path(self.build_directory, "bfd", "*.h"), extradir)

    def flag_handler(self, name, flags):
        spec = self.spec
        if name == "ldflags":
            if spec.satisfies("%cce"):
                flags.append("-Wl,-z,muldefs")
        elif name == "ldlibs":
            if "+nls" in self.spec and "intl" in self.spec["gettext"].libs.names:
                flags.append("-lintl")
        return self.build_system_flags(name, flags)
