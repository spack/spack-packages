# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *

class Libotf(AutotoolsPackage):
    homepage = "https://www.nongnu.org/m17n"
    url = "https://download.savannah.nongnu.org/releases/m17n/libotf-0.9.16.tar.gz"
    cvs = ":pserver:anonymous@cvs.savannah.nongnu.org:/sources/m17n%module=libotf"

    maintainers = ["cosmicexplorer"]

    license("LGPL-2.1")

    variant("X", default=True, description="Add support for the X window system.")
    variant("freetype-config", default=False, description="Use freetype-config program for deps.")

    depends_on("c", type="build")

    depends_on("freetype@2:")
    depends_on("freetype+freetype-config", when="+freetype-config")

    depends_on("pkg-config", type="build", when="~freetype-config")
    variant(
        "libs",
        default="shared,static",
        values=("shared", "static"),
        multi=True,
        description="Build shared libs, static libs or both",
    )
    variant("pic", default=True, description="Enable position-independent code (PIC)")
    requires("+pic", when="libs=shared")

    with when("+X"):
        depends_on("libx11")
        depends_on("libxaw")
        depends_on("libxt")
        depends_on("libxmu")

    with default_args(type="build"):
        depends_on("autoconf")
        depends_on("automake")
        depends_on("libtool")
        depends_on("m4")

    version("0.9.16", sha256="68db0ca3cda2d46a663a92ec26e6eb5adc392ea5191bcda74268f0aefa78066b")
    # version("main", branch="MAIN")
    # version("1.34", branch="1.34")
    # version("2021-12-10", date="2021-12-10")

    patch("replace-freetype-config.patch", when="~freetype-config")

    def configure_args(self):
        return [
            *self.with_or_without("x", variant="X"),
            *self.enable_or_disable(
                "shared", activation_value=lambda opt: opt == 'shared', variant="libs"),
            *self.enable_or_disable(
                "static", activation_value=lambda opt: opt == 'static', variant="libs"),
            *self.with_or_without("pic"),
        ]
