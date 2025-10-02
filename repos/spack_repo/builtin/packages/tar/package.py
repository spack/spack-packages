# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Tar(AutotoolsPackage, GNUMirrorPackage):
    """GNU Tar provides the ability to create tar archives, as well as various
    other kinds of manipulation."""

    homepage = "https://www.gnu.org/software/tar/"
    gnu_mirror_path = "tar/tar-1.32.tar.gz"

    executables = [r"^tar$"]

    tags = ["core-packages"]

    license("GPL-3.0-or-later")

    version("1.35", sha256="14d55e32063ea9526e057fbf35fcabd53378e769787eff7919c3755b02d2b57e")
    version("1.34", sha256="03d908cf5768cfe6b7ad588c921c6ed21acabfb2b79b788d1330453507647aed")

    variant(
        "zip",
        default="pigz",
        values=("gzip", "pigz"),
        description="Default compression program for tar -z",
    )

    depends_on("c", type="build")

    depends_on("iconv")

    # Compression
    depends_on("gzip", type="run", when="zip=gzip")
    depends_on("pigz", type="run", when="zip=pigz")
    depends_on("zstd+programs", type="run")
    depends_on("xz", type="run")  # for xz/lzma
    depends_on("bzip2", type="run")

    # The NVIDIA compilers do not currently support some GNU builtins.
    # Detect this case and use the fallback path.
    with when("%nvhpc"):
        patch("nvhpc-1.34.patch", when="@1.34")
        # Workaround bug where __LONG_WIDTH__ is not defined
        patch("nvhpc-long-width.patch", when="@1.34:")
        # Newer versions are marked as conflict for now
        conflicts("@1.35:", msg="NVHPC not yet supported for 1.35")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"tar \(GNU tar\) (\S+)", output)
        return match.group(1) if match else None

    def flag_handler(self, name, flags):
        if name == "ldflags" and self.spec.satisfies("@1.35 ^[virtuals=iconv] libiconv"):
            # https://savannah.gnu.org/bugs/?64441
            flags.append("-liconv")
        return (flags, None, None)

    def configure_args(self):
        # Note: compression programs are passed by abs path,
        # so that tar can locate them when invoked without spack load.
        args = [
            "--disable-nls",
            f"--with-xz={self.spec['xz'].prefix.bin.xz}",
            f"--with-lzma={self.spec['xz'].prefix.bin.lzma}",
            f"--with-bzip2={self.spec['bzip2'].prefix.bin.bzip2}",
        ]

        if self.spec.dependencies("zstd"):
            args.append(f"--with-zstd={self.spec['zstd'].prefix.bin.zstd}")

        # Choose gzip/pigz
        zip = self.spec.variants["zip"].value
        if zip == "gzip":
            gzip_path = self.spec["gzip"].prefix.bin.gzip
        elif zip == "pigz":
            gzip_path = self.spec["pigz"].prefix.bin.pigz
        args.append(f"--with-gzip={gzip_path}")

        if self.spec["iconv"].name == "libiconv":
            args.append(f"--with-libiconv-prefix={self.spec['iconv'].prefix}")
        else:
            args.append("--without-libiconv-prefix")
        return args
