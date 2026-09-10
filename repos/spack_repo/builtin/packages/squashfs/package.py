# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Squashfs(MakefilePackage):
    """Squashfs - read only compressed filesystem"""

    homepage = "https://squashfs.sourceforge.net"
    url = "https://downloads.sourceforge.net/project/squashfs/squashfs/squashfs4.3/squashfs4.3.tar.gz"

    license("GPL-2.0-or-later")

    # version      sha1
    version("4.6.1", sha256="94201754b36121a9f022a190c75f718441df15402df32c2b520ca331a107511c")
    version(
        "4.5.1",
        sha256="277b6e7f75a4a57f72191295ae62766a10d627a4f5e5f19eadfbc861378deea7",
        url="https://downloads.sourceforge.net/project/squashfs/squashfs/squashfs4.5.1/squashfs-tools-4.5.1.tar.gz",
    )

    variant("gzip", default=True, description="Enable gzip compression support")
    variant("lz4", default=False, description="Enable LZ4 compression support")
    variant("lzo", default=False, description="Enable LZO compression support")
    variant("xz", default=False, description="Enable xz compression support")
    variant("zstd", default=False, description="Enable Zstandard/zstd support")
    variant(
        "default_compression",
        default="gzip",
        values=("gzip", "lz4", "lzo", "xz", "zstd"),
        multi=False,
        description="Default compression algorithm",
    )
    variant("static", default=False, description="Build fully static mksquashfs executable")

    conflicts(
        "squashfs~gzip default_compression=gzip",
        msg="Cannot set default compression to missing algorithm",
    )
    conflicts(
        "squashfs~lz4 default_compression=lz4",
        msg="Cannot set default compression to missing algorithm",
    )
    conflicts(
        "squashfs~lzo default_compression=lzo",
        msg="Cannot set default compression to missing algorithm",
    )
    conflicts(
        "squashfs~xz default_compression=xz",
        msg="Cannot set default compression to missing algorithm",
    )
    conflicts(
        "squashfs~zstd default_compression=zstd",
        msg="Cannot set default compression to missing algorithm",
    )

    depends_on("c", type="build")  # generated

    depends_on("zlib-api", when="+gzip")
    depends_on("lz4", when="+lz4")
    depends_on("lz4 libs=static", when="+lz4 +static")
    depends_on("lzo", when="+lzo")
    depends_on("lzo libs=static", when="+lzo +static")
    depends_on("xz", when="+xz")
    depends_on("xz libs=static", when="+xz +static")
    depends_on("zstd", when="+zstd")
    depends_on("zstd libs=static", when="+zstd +static")

    def make_options(self, spec):
        default = spec.variants["default_compression"].value
        return [
            "GZIP_SUPPORT={0}".format(1 if "+gzip" in spec else 0),
            "LZ4_SUPPORT={0}".format(1 if "+lz4" in spec else 0),
            "LZO_SUPPORT={0}".format(1 if "+lzo" in spec else 0),
            "XZ_SUPPORT={0}".format(1 if "+xz" in spec else 0),
            "ZSTD_SUPPORT={0}".format(1 if "+zstd" in spec else 0),
            "COMP_DEFAULT={0}".format(default),
            "EXTRA_LDFLAGS={0}".format("-static" if "+static" in spec else ""),
        ]

    def build(self, spec, prefix):
        options = self.make_options(spec)
        with working_dir("squashfs-tools"):
            make(*options)

    def install(self, spec, prefix):
        options = self.make_options(spec)
        prefix_arg = "INSTALL_PREFIX={}".format(prefix)
        with working_dir("squashfs-tools"):
            make("install", prefix_arg, *options)
