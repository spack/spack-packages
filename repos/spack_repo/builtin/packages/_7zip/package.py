# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os
import re

from spack_repo.builtin.build_systems import makefile, nmake
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack_repo.builtin.build_systems.nmake import NMakePackage

from spack.package import *


class _7zip(MakefilePackage, NMakePackage):
    """7-Zip is a file archiver with a high compression ratio"""

    homepage = "https://www.7-zip.org/"
    url = "https://github.com/ip7z/7zip/releases/download/26.05/7z2605-src.tar.xz"
    list_url = "https://github.com/ip7z/7zip/releases"
    tags = ["windows"]

    executables = ["^7z$", "^7zz$"]

    license("LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause")

    version("26.05", sha256="0b6080b8c3e7a579161d2d495224c0e51c467576cb4c7048b0ab485ef44cc22e")
    version("21.07", sha256="213d594407cb8efcba36610b152ca4921eda14163310b43903d13e68313e1e39")

    build_system("makefile", conditional("nmake", when="platform=windows"), default="makefile")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # The makefiles for Linux and macOS are only tested from 26.05 on
    conflicts("build_system=makefile", when="@:21")

    with when("build_system=nmake"):
        variant(
            "link_type",
            default="shared",
            description="build shared and/or static libraries",
            values=("static", "shared"),
            multi=True,
        )

        # TODO: Patch on WinSDK version 10.0.20348.0 when SDK is introduced to Spack
        # This patch solves a known bug in that SDK version on the 7zip side
        # right now patch for all versions to prevent build errors
        patch("noexcept_typedef.patch")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--help", output=str, error=str)
        # "7-Zip 21.07 (x64) : ..." or "7-Zip (z) 26.05 (arm64) : ..."
        match = re.search(r"7-Zip (?:\([a-z]+\) )?([0-9]+\.[0-9]+)", output)
        return match.group(1) if match else None

    def url_for_version(self, version):
        ver_str = str(version).replace(".", "")
        if version <= Version("21.07"):
            return f"https://downloads.sourceforge.net/project/sevenzip/7-Zip/{version}/7z{ver_str}-src.tar.xz"
        return f"https://github.com/ip7z/7zip/releases/download/{version}/7z{ver_str}-src.tar.xz"


class MakefileBuilder(makefile.MakefileBuilder):
    """Builds 7zz, the standalone console program with all formats, as 7-Zip's readme says."""

    @property
    def build_directory(self):
        return join_path(self.pkg.stage.source_path, "CPP", "7zip", "Bundles", "Alone2")

    @property
    def makefile_name(self):
        """The makefile for the compiler, without assembler, which on x86 needs asmc or uasm."""
        if self.spec.satisfies("platform=darwin"):
            arch = "arm64" if self.spec.satisfies("target=aarch64:") else "x64"
            return f"cmpl_mac_{arch}.mak"
        if self.spec.satisfies("%c=gcc"):
            return "cmpl_gcc.mak"
        return "cmpl_clang.mak"

    def build(self, pkg, spec, prefix):
        with working_dir(self.build_directory):
            make(
                "-f",
                join_path("..", "..", self.makefile_name),
                f"CC={spack_cc}",
                f"CXX={spack_cxx}",
                "O=b/spack",
                "USE_ASM=",
                # without -Werror, which the makefiles add
                "CFLAGS_WARN_WALL=-Wall -Wextra",
                # 7-Zip strips the binary by default
                "LFLAGS_STRIP=",
            )

    def install(self, pkg, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "b", "spack", "7zz"), prefix.bin)


class NMakeBuilder(nmake.NMakeBuilder):
    @property
    def makefile_root(self):
        return join_path(self.pkg.stage.source_path, "CPP", "7zip")

    @property
    def plat_arch(self):
        """PLATFORM of 7-Zip's Build.mak for the target, which is also its output directory"""
        return {"x86_64": "x64", "aarch64": "arm64", "x86": "x86"}[str(self.spec.target.family)]

    def nmake_args(self):
        link_type = "1" if "static" in self.spec.variants["link_type"].value else "0"
        return [
            self.define("PLATFORM", self.plat_arch),
            self.define("MY_STATIC_LINK", link_type),
            self.define("NEW_COMPILER", "1"),
        ]

    def build(self, pkg, spec, prefix):
        # 7zips makefile is configured in such as way that if this value is set
        # compiler paths with spaces are incorrectly parsed. Compiler will be infered
        # from VCVARs on Windows
        os.environ.pop("CC", None)
        super().build(pkg, spec, prefix)

    def install(self, pkg, spec, prefix):
        """7Zip exports no install target so we must hand install"""
        with working_dir(self.build_directory):
            for root in ("Bundles", "UI"):
                for ext in ("*.exe", "*.dll"):
                    for x in glob.glob(os.path.join(root, "*", self.plat_arch, ext)):
                        install(x, os.path.join(prefix, os.path.basename(x)))
