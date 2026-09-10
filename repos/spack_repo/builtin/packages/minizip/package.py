# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Minizip(AutotoolsPackage):
    """C library for zip/unzip via zLib."""

    homepage = "https://www.winimage.com/zLibDll/minizip.html"
    url = "https://zlib.net/fossils/zlib-1.2.11.tar.gz"

    license("Zlib")

    version("1.3.1", sha256="9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23")

    depends_on("c", type="build")

    configure_directory = "contrib/minizip"

    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("zlib-api")

    # statically link to libz.a
    # https://github.com/Homebrew/homebrew-core/blob/master/Formula/minizip.rb
    patch("static.patch", when="%apple-clang@12:")

    # build minizip and miniunz
    @run_before("autoreconf")
    def build_minizip_binary(self):
        configure()
        make()
        with working_dir(self.configure_directory):
            make()

    # install minizip and miniunz
    @run_after("install")
    def install_minizip_binary(self):
        mkdirp(self.prefix.bin)
        with working_dir(self.configure_directory):
            install("minizip", self.prefix.bin)
            install("miniunz", self.prefix.bin)
