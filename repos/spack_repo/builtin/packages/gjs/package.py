# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Gjs(MesonPackage):
    """GJS is a JavaScript runtime built on Firefox's SpiderMonkey JavaScript engine and the GNOME
    platform libraries.

    Use the GNOME platform libraries in your JavaScript programs. GJS powers GNOME Shell, Maps,
    Characters, Sound Recorder and many other apps."""

    homepage = "https://gitlab.gnome.org/GNOME/gjs"
    url = "https://download.gnome.org/sources/gjs/1.86/gjs-1.86.0.tar.xz"
    git = "https://gitlab.gnome.org/GNOME/gjs.git"

    maintainers("KineticTheory")

    license("GNU LGPL-2.1")

    version("1.86.0", sha256="63448f7a57804d4c2a8d0c7f5e90e224d04d4eb2d560142c076c65a8eda00799")
    version("1.84.2", sha256="35142edf345705636300291ec3a7d583f14969ff3fae0ff30f4a95b1e6740166")
    version("1.82.3", sha256="63e84b9c82a60d166c8704322f8907945e25d9bbd0b80485468d3126505c027d")
    version("1.80.2", sha256="135e39c5ac591096233e557cfe577d64093f5054411d47cb2e214bad7d4199bd")

    # Note: gjs doesn't seem to be able to use a readline installation provided by spack.
    variant("readline", default=False, description="Build with readline support.")

    depends_on("c", type="build")

    depends_on("cairo", type=("build", "link"))
    depends_on("glib@2.86:", type=("build", "link"), when="@1.86:")
    depends_on("glib@2.68:", type=("build", "link"), when="@1.84:")
    depends_on("glib@2.66:", type=("build", "link"))
    depends_on("meson@1.4:", when="@1.84:")
    depends_on("meson@0.62:", when="@1.82:")
    depends_on("meson@0.58:")
    depends_on("mozjs@140.0.0:140", type=("build", "link"), when="@1.86:")
    depends_on("mozjs@128.0.0:128", type=("build", "link"), when="@1.82:1.84")
    depends_on("mozjs@115.0.0:115", type=("build", "link"), when="@:1.82")
    depends_on("gtkplus", type=("build", "link"))
    depends_on("readline", type="build", when="+readline")

    def url_for_version(self, version):
        return f"https://download.gnome.org/sources/gjs/{version.up_to(2)}/gjs-{version}.tar.xz"

    def meson_args(self):
        args = []
        if self.spec.satisfies("~readline"):
            args.append("-Dreadline=disabled")
        return args
