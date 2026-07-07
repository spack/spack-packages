# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libarchive(AutotoolsPackage):
    """libarchive: C library and command-line tools for reading and
    writing tar, cpio, zip, ISO, and other archive formats."""

    homepage = "https://www.libarchive.org"
    url = "https://www.libarchive.org/downloads/libarchive-3.1.2.tar.gz"

    maintainers("haampie")

    license("BSD-2-Clause AND BSD-3-Clause AND Public-Domain")

    version("3.8.5", sha256="8a60f3a7bfd59c54ce82ae805a93dba65defd04148c3333b7eaa2102f03b7ffd")
    version("3.8.0", sha256="191b5b24811499d5c2e5efa3248975fa6daa5e6a227700cc7b8e54d6d7c06eef")
    version("3.7.9", sha256="aa90732c5a6bdda52fda2ad468ac98d75be981c15dde263d7b5cf6af66fd009f")
    version("3.7.8", sha256="a123d87b1bd8adb19e8c187da17ae2d957c7f9596e741b929e6b9ceefea5ad0f")
    version("3.7.7", sha256="4cc540a3e9a1eebdefa1045d2e4184831100667e6d7d5b315bb1cbc951f8ddff")
    version("3.7.6", sha256="b4071807367b15b72777c2eaac80f42c8ea2d20212ab279514a19fe1f6f96ef4")
    version("3.7.5", sha256="37556113fe44d77a7988f1ef88bf86ab68f53d11e85066ffd3c70157cc5110f1")

    variant(
        "libs",
        default="static,shared",
        values=("static", "shared"),
        multi=True,
        description="What libraries to build",
    )

    # TODO: BLAKE2 is missing
    variant(
        "compression",
        default="bz2lib,lz4,lzo2,lzma,zlib,zstd",
        values=("bz2lib", "lz4", "lzo2", "lzma", "zlib", "zstd"),
        multi=True,
        description="Supported compression",
    )
    variant(
        "xar",
        default="libxml2",
        values=("libxml2", "expat"),
        description="What library to use for xar support",
    )
    variant(
        "crypto",
        default="openssl",
        values=("mbedtls", "nettle", "openssl"),
        description="What crypto library to use for mtree and xar hashes",
    )
    variant(
        "programs",
        values=any_combination_of("bsdtar", "bsdcpio", "bsdcat"),
        description="What executables to build",
    )
    variant("iconv", default=True, description="Support iconv")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("pkgconfig", type="build")

    depends_on("bzip2", when="compression=bz2lib")
    depends_on("lz4", when="compression=lz4")
    depends_on("lzo", when="compression=lzo2")
    depends_on("xz", when="compression=lzma")
    depends_on("zlib-api", when="compression=zlib")
    depends_on("zstd", when="compression=zstd")

    depends_on("nettle", when="crypto=nettle")
    depends_on("openssl", when="crypto=openssl")
    depends_on("mbedtls@2.0:2 +pic", when="crypto=mbedtls")

    depends_on("libxml2", when="xar=libxml2")
    depends_on("expat", when="xar=expat")

    depends_on("iconv", when="+iconv")

    # NOTE: `make check` is known to fail with the Intel compilers
    # The build test suite cannot be built with Intel

    def configure_args(self):
        spec = self.spec
        args = ["--without-libb2"]
        args += self.with_or_without("compression")
        args += self.with_or_without("crypto")
        args += self.enable_or_disable("programs")

        if spec.satisfies("+iconv"):
            if spec["iconv"].name == "libiconv":
                args.append(f"--with-libiconv-prefix={spec['iconv'].prefix}")
            else:
                args.append("--without-libiconv-prefix")
        else:
            args.append("--without-iconv")

        if spec.satisfies("xar=expat"):
            args.append("--with-expat")
        else:
            args.append("--without-expat")

        if spec.satisfies("xar=libxml2"):
            args.append("--with-xml2")
        else:
            args.append("--without-xml2")

        return args
