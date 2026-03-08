# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.xorg import XorgPackage

from spack.package import *


class XcbUtilCursor(AutotoolsPackage, XorgPackage):
    """The XCB util modules provides a number of libraries which sit on top
    of libxcb, the core X protocol library, and some of the extension
    libraries. These experimental libraries provide convenience functions
    and interfaces which make the raw X protocol more usable. Some of the
    libraries also provide client-side code which is not strictly part of
    the X protocol but which have traditionally been provided by Xlib."""

    homepage = "https://gitlab.freedesktop.org/xorg/lib/libxcb-cursor"
    xorg_mirror_path = "lib/xcb-util-cursor-0.1.4.tar.xz"
    git = "https://gitlab.freedesktop.org/xorg/lib/libxcb-cursor.git"

    license("MIT")

    maintainers("wdconinc")

    version("0.1.6", sha256="fdeb8bd127873519be5cc70dcd0d3b5d33b667877200f9925a59fdcad8f7a933")
    version("0.1.5", sha256="0caf99b0d60970f81ce41c7ba694e5eaaf833227bb2cbcdb2f6dc9666a663c57")
    version("0.1.4", sha256="28dcfe90bcab7b3561abe0dd58eb6832aa9cc77cfe42fcdfa4ebe20d605231fb")

    depends_on("c", type="build")  # generated

    depends_on("libxcb@1.4:")
    depends_on("xcb-util-renderutil")
    depends_on("xcb-util-image")

    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")
