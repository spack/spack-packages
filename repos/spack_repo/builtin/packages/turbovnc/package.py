# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack import *
from spack.package import *


class Turbovnc(CMakePackage):
    """TurboVNC is a derivative of VNC (Virtual Network Computing)
    that is tuned to provide peak performance for 3D and video workloads.
    TurboVNC was originally a fork of TightVNC 1.3.x, on the surface,
    the X server and Windows viewer still behave similarly to their parents."""

    homepage = "http://www.turbovnc.org/"
    url = "https://github.com/TurboVNC/turbovnc/releases/download/3.2/turbovnc-3.2.tar.gz"

    version("3.2", sha256="a4fd895ebb8a40a5962db8c38e3de61e4d22c77d64d2ea0afe8fd78c7a8aff72")

    variant("server", default=True, description="Enable server build")
    variant("x11deps", default=True, description="Depends x11 depends")

    depends_on("libx11", when="+x11deps")
    depends_on("libjpeg-turbo@1.5.1:", when="@2.1:")
    depends_on("openssl")

    depends_on("java@17")
    depends_on("libxext", when="+x11deps")
    depends_on("libxdmcp", when="+x11deps")
    depends_on("libxau", when="+x11deps")
    depends_on("libxdamage", when="+x11deps")
    depends_on("libxcursor", when="+x11deps")
    depends_on("libxxf86vm", when="+x11deps")
    depends_on("libxxf86misc", when="+x11deps")
    depends_on("xf86vidmodeproto", when="+x11deps")
    depends_on("libxi", when="+x11deps")

    depends_on("xkeyboard-config", when="+x11deps", type=("build", "run"))
    depends_on("font-util fonts=font-adobe-75dpi", when="+x11deps", type="run")
    depends_on("xkbcomp", when="+x11deps", type=("build", "run"))
    depends_on("xauth", when="+x11deps", type=("build", "run"))

    with when("+server"):
        depends_on("libxfont2")
        depends_on("pixman")
        depends_on("libdrm")
        depends_on("libxkbfile")
        depends_on("mesa+egl")
        depends_on("kbproto")
        depends_on("xorgproto")
        depends_on("virtualgl")

    def cmake_args(self):

        options = []
        options.append("-DTVNC_BUILDJAVA:BOOL=OFF")
        options.append("-DTVNC_BUILDNATIVE:BOOL=ON")
        options.append("-DTVNC_BUILDSERVER:BOOL=ON")
        options.append("-DTVNC_DRI3=OFF")
        if "+server" in self.spec:
            options.append("-DTVNC_BUILDSERVER:BOOL=ON")
            if "~x11deps" in self.spec:
                options.append("-DTVNC_NVCONTROL:BOOL=ON")
        else:
            options.append("-DTVNC_BUILDSERVER:BOOL=OFF")
        if "+x11deps" in self.spec:
            options.append(
                "-DXKB_BASE_DIRECTORY:PATH="
                + self.spec["xkeyboard-config"].prefix
                + "/share/X11/xkb"
            )
            options.append("-DXKB_BIN_DIRECTORY:PATH=" + self.spec["xkbcomp"].prefix + "/bin")

        options.append(
            "-DTJPEG_LIBRARY=" + self.spec["libjpeg-turbo"].prefix + "/lib/libturbojpeg.a"
        )
        return options
