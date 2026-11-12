# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libvncserver(CMakePackage):
    """A library for easy implementation of a VNC server."""

    homepage = "https://github.com/LibVNC/libvncserver"
    url = "https://github.com/LibVNC/libvncserver/archive/refs/tags/LibVNCServer-0.9.14.tar.gz"

    license("GPL-2.0-or-later", checked_by="wspear")

    version("0.9.15", sha256="62352c7795e231dfce044beb96156065a05a05c974e5de9e023d688d8ff675d7")
    version("0.9.14", sha256="83104e4f7e28b02f8bf6b010d69b626fae591f887e949816305daebae527c9a5")
    version("0.9.13", sha256="0ae5bb9175dc0a602fe85c1cf591ac47ee5247b87f2bf164c16b05f87cbfa81a")
    version("0.9.12", sha256="33cbbb4e15bb390f723c311b323cef4a43bcf781984f92d92adda3243a116136")
    version("0.9.11", sha256="193d630372722a532136fd25c5326b2ca1a636cbb8bf9bb115ef869c804d2894")
    version("0.9.10", sha256="ed10819a5bfbf269969f97f075939cc38273cc1b6d28bccfb0999fba489411f7")
    version("0.9.9", sha256="f5f9f87f23f8f81260e071dac89169357b69f60dd61f537578b2613bc5fb60af")
    version("0.9.8", sha256="6ae237a7983c216ef235331324def1bc9078d3610f9a4345dec8a4d1179dd494")

    variant("openssl", default=True, description="TLS and crypto support via OpenSSL")
    variant("shared", default=True, description="Build shared libraries")

    depends_on("c", type="build")
    depends_on("cmake@3.4:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("zlib-api")
    depends_on("jpeg")
    depends_on("libpng")
    depends_on("openssl", when="+openssl")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_OPENSSL", "openssl"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("WITH_GCRYPT", False),
            self.define("WITH_GNUTLS", False),
            self.define("WITH_SDL", False),
            self.define("WITH_GTK", False),
            self.define("WITH_SYSTEMD", False),
            self.define("WITH_EXAMPLES", False),
            self.define("WITH_TESTS", False),
        ]
        return args

    @property
    def libs(self):
        return find_libraries(
            ["libvncclient", "libvncserver"],
            root=self.prefix,
            shared=self.spec.satisfies("+shared"),
            recursive=True,
        )
