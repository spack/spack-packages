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
    version("21.1.20", sha256="a51aea1cbb29cb8122e39c1c8728469d4fd8db71a538565fbf017df11841bf04")
    version("21.1.19", sha256="d99934e82dc8f0f4b4ffca1831e49a3ed5c0ab20488b3c31757443ac71af9f32")
    version("21.1.18", sha256="c8591ceb70b177440062406542fe52ba60212f217f27f8f802dd20373ca9e74b")
    version("21.1.17", sha256="5b808335c09026a88dafd08e7e513b47e68183e3d6bd35d63db8cedaaa23af4b")
    version("21.1.16", sha256="59fa52b63f6f8747ee2c4716decb29ced249c4c574e2a18c96b7d3b1420f7fd9")
    version("21.1.15", sha256="f62354a5996b021615702fb6d67dd0e870e2cddba0261a833efb60f5b7d6d413")
    version("21.1.14", sha256="b79dbaf668c67da25c4eb5b395eec60f2593240519aefdd3e8645023ef46226f")
    version("21.1.13", sha256="2864b6a5359ab41c5a6132c69b5d0c9af6eb85ad26d433edb012c914029de752")
    version("21.1.12", sha256="f76a5878b0e6d16415cf0cd24ffc21090845fef3bc4ada45e57ea86b6c8fb75b")
    version("21.1.11", sha256="1aa0ee1adad0b2db7f291f3823a4ab240c7f4aea710e89f5ef4aa232b6833403")
    version("21.1.10", sha256="db6cb65c3460dd8346ff1fce99002e24897a5c1f18f8a2acd0fd65bfaa4d0d56")
    version("21.1.9", sha256="455ac22c411b3e74adb4d1b3fd48b9037b6b5ba9260247c59b669f67a08fd26e")
    version("21.1.8", sha256="d845d1fee2edb33cb94f31b5170f26d98ed31f853ce2da21daca7c60c8ff3aae")
    version("21.1.7", sha256="1a9005f47c7ea83645a977581324439628a32c4426303e5a4b9c2d6615becfbf")
    version("21.1.6", sha256="6f9c73ccc50e2731adac17671c8e33687738c8cd556b49ecb9f410ce7217be11")
    version("21.1.5", sha256="5e391867bfe44ce766a8c748e7563dc9678c229af72b5f94e221a92b1b04b7a1")
    version("21.1.4", sha256="cbd5a1f75881e8a341823e51e489281aee0912c7023b4eed170b26b18f617e36")
    version("21.1.3", sha256="c52403a66935092da86a18052ffdcb93a2762a146901f63c1261744a708b12e2")
    version("21.1.2", sha256="cc6ef34db47cc402af2a597301c625f71c142a1423aaf16fde257cce7d924bf3")
    version("21.1.1", sha256="bd809c59e3f887eb75c8ba9e0160a234a8cee87145771158907ad5ae2ec80b1a")
    version("21.1.0", sha256="133ec56ebb576803ebb917c85506f7ad3e2e0fa6ca32ee7dd382bf513c8e5097")
    version(
        "21.0.99.902", sha256="11d8f4bb405bfb0ebed23fb524ff355dcc9fa5013fcb32557eb733b09297ce51"
    )
    version(
        "21.0.99.901", sha256="7b3a05a9a77961466518f44a989a0909b382237f1145d46b3d6dc67d4137c099"
    )
    version("21.0.99.1", sha256="8d7c7de272a8e6b457a8358c6a9240ba4a4c798a041833006c6cec75d3abc533")
    version("1.20.14", sha256="54b199c9280ff8bf0f73a54a759645bd0eeeda7255d1c99310d5b7595f3ac066")
    version("1.20.13", sha256="26f801f4d92216995f389873cf3b4e90069cf63e94bc5dd09ebbf7fd7e1ddcc2")
    version("1.20.12", sha256="71687561262e4527a7ef779193725416f70c3e0424daaa9a6617bd37dc7701bb")
    version("1.20.11", sha256="4e9341c96f5ed0f6b9491ed732c501303479d3fe21da280c768a1822d7e5d352")
    version("1.20.10", sha256="02f2198608b6191b7f8c65158bd4613734ec1c5c3d6784c5177f41b5cd2d30a3")
    version("1.20.9", sha256="067c348fe1a86a1924010354c1c7cf1eaa9e43866e48540aa56a465f2a341ddc")
    version("1.20.8", sha256="1e1f9245301cb3b7e89cb3ac7ae9ac513e362963fae92d2153762e3a95758f0b")
    version("1.20.7", sha256="0271b774095034c932e55593d9b842b78b44e939c7d42de8e3566096322d75e8")
    version("1.20.6", sha256="1f00a9444482280e3815de4642758fcb279496002becb85c2f9d994456903ad4")
    version("1.20.5", sha256="3c0b1c41c05da7bbc10c391d9a503cdb86f4eaf08f3ad1b7e9d1044034272bcf")
    version("1.20.4", sha256="a6447de89eca3e22eeead682b325d902779569534ad83388c9e16611d72baaf3")
    version("1.20.3", sha256="d9e4fbefe1a31a4999c9a5f1c81a8e34e1d1b9056f3ac225f299f515eab2bcb8")
    version("1.20.2", sha256="a560c199fdf5a6f99578627cf524933d6140a8cc04054cecb1443eabcd306530")
    version("1.20.1", sha256="dc02dd7fc55ae7422bb2c96be8b8e211f5adb1f3deea3ded1afcee14c5f59f1b")
    version("1.20.0", sha256="6f55004082f9b9c3304037ae78bc5969889d066cf06c0f3130393fef79942ed1")
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
    version("1.19.6", sha256="3c0e4a354a6b1d5d357b121357946ee8ffdb2f52158b2e63e105be9cef013168")
    version("1.19.5", sha256="1818068b6b86387ee0e392cbe28208ff949d253a1611d17bf2908961f3669b1c")
    version("1.19.4", sha256="a1c87baa073faa3b7eb11610dd2c89a25586c71f861d32265fc26e11d12fafed")
    version("1.19.3", sha256="8f93b98f1ac9fbd87515bfe329a069b48bbec98e5329584ab5fbf759a0953b8d")
    version("1.19.2", sha256="191d91d02c059c66747635e145c30bc1004e703fe3b74439e26c0d05d5c4d28b")
    version("1.19.1", sha256="24c7419a963f55eeed5951541344cd616196ae97c273e17b32ad7f0c3658bf2b")
    version("1.19.0", sha256="c3e8660a74e2902e6ecaa66aa774e15d1ab66c2c19a023bd9e74e651ef005a43")
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
