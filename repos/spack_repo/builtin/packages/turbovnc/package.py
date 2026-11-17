# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Turbovnc(CMakePackage):
    """TurboVNC is a derivative of VNC (Virtual Network Computing)
    that is tuned to provide peak performance for 3D and video workloads.
    TurboVNC was originally a fork of TightVNC 1.3.x, on the surface,
    the X server and Windows viewer still behave similarly to their parents."""

    homepage = "https://www.turbovnc.org/"
    url = "https://github.com/TurboVNC/turbovnc/releases/download/3.3.1/turbovnc-3.3.1.tar.gz"

    version("3.3.1", sha256="9be0a0764d89f1a234cad7775ea142a01c0efe198523456899883bd6466691da")
    version("3.2.1", sha256="e5b853b832808d796764e17a85396de62bc65f21e8b98056f6de333a2ef64720")
    version("3.2", sha256="a4fd895ebb8a40a5962db8c38e3de61e4d22c77d64d2ea0afe8fd78c7a8aff72")

    variant("server", default=True, description="Build the TurboVNC server")
    variant("x11deps", default=True, description="Build with X11 dependencies")

    depends_on("libjpeg-turbo@1.5.1:", when="@2.1:")
    depends_on("openssl")
    depends_on("java@17")

    with when("+x11deps"):
        depends_on("libx11")
        depends_on("libxext")
        depends_on("libxdmcp")
        depends_on("libxau")
        depends_on("libxdamage")
        depends_on("libxcursor")
        depends_on("libxxf86vm")
        depends_on("libxxf86misc")
        depends_on("xf86vidmodeproto")
        depends_on("libxi")
        depends_on("xtrans")

        depends_on("xkeyboard-config", type=("build", "run"))
        depends_on("font-util fonts=font-adobe-75dpi", type="run")
        depends_on("xkbcomp", type=("build", "run"))
        depends_on("xauth", type=("build", "run"))

    with when("+server"):
        depends_on("libxfont2")
        depends_on("pixman")
        depends_on("libdrm")
        depends_on("libxkbfile")
        depends_on("mesa+egl")
        depends_on("kbproto")
        depends_on("xorgproto")
        depends_on("virtualgl")
        depends_on("linux-pam")

    def cmake_args(self):
        options = [
            self.define_from_variant("TVNC_BUILDSERVER", "server"),
            self.define("TVNC_DRI3", False),
        ]

        if "+server" in self.spec:
            pam = self.spec["linux-pam"]
            include_paths = [pam.prefix.include]

            if "+x11deps" in self.spec:
                include_paths.append(self.spec["xtrans"].prefix.include)

            options.extend(
                [
                    self.define(
                        "CMAKE_C_FLAGS",
                        " ".join("-isystem {0}".format(path) for path in include_paths),
                    ),
                    self.define("PAM_LIBRARY", pam.prefix.lib.join("libpam.so")),
                ]
            )

            if "~x11deps" in self.spec:
                options.append(self.define("TVNC_NVCONTROL", True))

        if "+x11deps" in self.spec:
            options.extend(
                [
                    self.define(
                        "XKB_BASE_DIRECTORY",
                        self.spec["xkeyboard-config"].prefix.share.join("X11/xkb"),
                    ),
                    self.define("XKB_BIN_DIRECTORY", self.spec["xkbcomp"].prefix.bin),
                ]
            )

        options.append(
            self.define(
                "TJPEG_LIBRARY",
                self.spec["libjpeg-turbo"].prefix.lib.join("libturbojpeg.a"),
            )
        )

        return options
