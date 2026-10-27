# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class GuacamoleServer(AutotoolsPackage):
    """The guacamole-server package is a set of software which forms the
    basis of the Guacamole stack. It consists of guacd, libguac, and
    several protocol support libraries."""

    homepage = "https://guacamole.apache.org/"
    url = "https://github.com/apache/guacamole-server/archive/1.1.0.tar.gz"
    list_url = "https://github.com/apache/guacamole-server/tags"

    license("GPL-3.0-or-later")

    version("1.6.0", sha256="913b05d19beabed4a3066e6e2be3078783048f55c7a9d2e3a012897a8766c245")
    version("1.5.5", sha256="50430c0f0f3b92f2cd3e60436fab0cedee8c1a9f762696a666016347039c731e")

    variant("ssh", default=True, description="SSH support")
    variant("vnc", default=False, description="VNC support")
    variant("webp", default=False, description="WebP support")

    depends_on("c", type="build")

    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("cairo +pdf +png")  # pdf enables zlib support required for CairoScript
    depends_on("libjpeg")
    depends_on("libpng")
    depends_on("uuid")
    depends_on("openssl", when="+ssh")
    depends_on("libssh2", when="+ssh")
    depends_on("pango", when="+ssh")
    depends_on("libvncserver", when="+vnc")
    depends_on("libwebp", when="+webp")

    def configure_args(self):
        args = []
        args += self.with_or_without("ssh")
        args += self.with_or_without("vnc")
        args += self.with_or_without("webp")
        return args
