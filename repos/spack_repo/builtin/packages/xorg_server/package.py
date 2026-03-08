# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.xorg import XorgPackage

from spack.package import *


class XorgServer(AutotoolsPackage, XorgPackage):
    """X.Org Server is the free and open source implementation of the display
    server for the X Window System stewarded by the X.Org Foundation."""

    homepage = "https://gitlab.freedesktop.org/xorg/xserver"
    xorg_mirror_path = "xserver/xorg-server-1.18.99.901.tar.gz"

    license("MIT")

    version("21.1.21", sha256="952444a35ce6a720c3e978d3bad2b683bacb648cceedc03e3600f6fb170071d2")
    version(
        "21.0.99.902", sha256="11d8f4bb405bfb0ebed23fb524ff355dcc9fa5013fcb32557eb733b09297ce51"
    )
    version(
        "21.0.99.901", sha256="7b3a05a9a77961466518f44a989a0909b382237f1145d46b3d6dc67d4137c099"
    )
    version("21.0.99.1", sha256="8d7c7de272a8e6b457a8358c6a9240ba4a4c798a041833006c6cec75d3abc533")
    version("1.20.14", sha256="54b199c9280ff8bf0f73a54a759645bd0eeeda7255d1c99310d5b7595f3ac066")
    version(
        "1.19.99.905", sha256="0df18d38805a8e1735480cbe6479193dbb221e66b5f766461fca160ebaf18ac9"
    )
    version(
        "1.19.99.904", sha256="f1fe5e27d0eab494a4eea11a075f8f6d3989c3683c22e0bdf5c060e57d351c0f"
    )
    version(
        "1.19.99.903", sha256="9cfcb585a8b84b657456d445f1c5ad521fa461bdcf06e009f1ae4e625eba6529"
    )
    version(
        "1.19.99.902", sha256="e7a4a3bb289dfca9dd8cd478682f686e5d04fee46e6ff59eb3f2fb11c0b84ad3"
    )
    version(
        "1.19.99.901", sha256="8c620b5b88e81a545c272e73dbcfff4b789ded432b6a1caa478a3476c00677e3"
    )
    version("1.19.7", sha256="5f6d3da0d1e341f27a7706779a24a5fa7174d5f161b5f8530f103753f0152de7")
    version(
        "1.18.99.902", sha256="fe5a312f7bdc6762c97f01b7a1d3c7a8691997255be6fbf7598c180abf384ea3"
    )
    version(
        "1.18.99.901", sha256="c8425163b588de2ee7e5c8e65b0749f2710f55a7e02a8d1dc83b3630868ceb21"
    )

    variant("glx", default=True, description="Build GLX extension")
    variant("dri", default=True, description="Build DRI, DRI2, DRI3 extensions")

    # glibc stopped declaring major()/minor() macros in <sys/types.h>
    # https://gitlab.freedesktop.org/xorg/xserver/-/commit/d732c36597fab2e9bc4f2aa72cf1110997697557
    patch("sysmacros.patch", when="@:1.18 ^glibc@2.25:")

    def patch(self):
        with when("@1"):
            # Due to transition from mesa version numbers to libglvnd version numbers,
            # subset of https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/292
            filter_file('LIBGL="gl >= 7.1.0"', 'LIBGL="gl >= 1.2"', "configure")
            filter_file('LIBGL="gl >= 9.2.0"', 'LIBGL="gl >= 1.2"', "configure")

    depends_on("c", type="build")

    depends_on("pixman@0.27.2:")
    depends_on("font-util")
    depends_on("libxshmfence@1.1:")
    depends_on("libdrm@2.3.0:", when="+dri")
    depends_on("libx11")

    depends_on("gl", when="+dri")
    depends_on("gl", when="+glx")

    depends_on("xf86driproto@2.1.0:", type="build", when="+dri")
    depends_on("dri2proto@2.8:", type="build", when="+dri")
    depends_on("dri3proto@1.0:", type="build", when="+dri")
    depends_on("glproto@1.4.17:", type="build", when="+dri")
    depends_on("glproto@1.4.17:", type="build", when="+glx")

    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("util-macros", type="build")
    depends_on("fixesproto@5.0:", type="build")
    depends_on("damageproto@1.1:", type="build")
    depends_on("xcmiscproto@1.2.0:", type="build")
    depends_on("xtrans@1.3.5:")
    depends_on("bigreqsproto@1.1.0:", type="build")
    depends_on("xproto@7.0.28:", type="build")
    depends_on("randrproto@1.5.0:", type="build")
    depends_on("renderproto@0.11:", type="build")
    depends_on("xextproto@7.2.99.901:", type="build")
    depends_on("inputproto@2.3:", type="build")
    depends_on("kbproto@1.0.3:", type="build")
    depends_on("fontsproto@2.1.3:", type="build")
    depends_on("pixman@0.27.2:")
    depends_on("videoproto", type="build")
    depends_on("compositeproto@0.4:", type="build")
    depends_on("recordproto@1.13.99.1:", type="build")
    depends_on("scrnsaverproto@1.1:", type="build")
    depends_on("resourceproto@1.2.0:", type="build")
    depends_on("presentproto@1.0:", type="build")
    depends_on("xineramaproto", type="build")
    depends_on("libxkbfile")
    depends_on("libxfont2")
    depends_on("libxext")
    depends_on("libxdamage")
    depends_on("libxfixes")
    depends_on("libepoxy")
    depends_on("libpciaccess")

    @when("@:1.19")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/406
        env.set("CPPFLAGS", "-fcommon")

        env.set("GL_LIBS", self.spec["gl"].libs.ld_flags)
        env.set("GL_CFLAGS", self.spec["gl"].headers.cpp_flags)

    def configure_args(self):
        args = []

        if self.spec.satisfies("+glx ^[virtuals=gl] osmesa"):
            args.append("--enable-glx")
        else:
            args.append("--disable-glx")

        if self.spec.satisfies("+dri"):
            args.append("--disable-dri")  # dri requires libdri, not libdrm
            args.append("--enable-dri2")
            args.append("--enable-dri3")
            args.append("--enable-drm")
        else:
            args.append("--disable-dri")
            args.append("--disable-dri2")
            args.append("--disable-dri3")
            args.append("--disable-drm")

        if self.spec.satisfies("^[virtuals=gl] osmesa"):
            args.append("--enable-glx")
        else:
            args.append("--disable-glx")

        args.extend(["--disable-glamor"])  # Glamor for Xorg requires gbm >= 10.2.0

        return args
