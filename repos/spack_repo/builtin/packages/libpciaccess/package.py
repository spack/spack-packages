# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.xorg import XorgPackage

from spack.package import *


class Libpciaccess(AutotoolsPackage, XorgPackage):
    """Generic PCI access library."""

    homepage = "https://cgit.freedesktop.org/xorg/lib/libpciaccess/"
    xorg_mirror_path = "lib/libpciaccess-0.13.5.tar.gz"

    license("X11")

    maintainers("CodingYayaToure")

    version("0.18.1", sha256="4af43444b38adb5545d0ed1c2ce46d9608cc47b31c2387fc5181656765a6fa76")
    version("0.18", sha256="5461b0257d495254346f52a9c329b44b346262663675d3fecdb204a7e7c262a9")
    version("0.17", sha256="bf6985a77d2ecb00e2c79da3edfb26b909178ffca3f2e9d14ed0620259ab733b")
    version("0.16", sha256="84413553994aef0070cf420050aa5c0a51b1956b404920e21b81e96db6a61a27")
    version("0.13.5", sha256="fe26ec788732b4ef60b550f2d3fa51c605d27f646e18ecec878f061807a3526e")
    version("0.13.4", sha256="74d92bda448e6fdb64fee4e0091255f48d625d07146a121653022ed3a0ca1f2f")

    def url_for_version(self, version):
        if version >= Version("0.18"):
            return f"https://www.x.org/archive/individual/lib/libpciaccess-{version}.tar.xz"
        return f"https://www.x.org/archive/individual/lib/libpciaccess-{version}.tar.gz"

    depends_on("c", type="build")

    depends_on("pkgconfig", type="build")
    depends_on("util-macros", type="build")

    patch("nvhpc.patch", when="%nvhpc")

    conflicts("platform=darwin")

    def flag_handler(self, name, flags):
        if name == "cflags":
            if self.spec.satisfies("%gcc@15:"):
                # gcc@15: is -std=gnu23 by default
                flags.append("-std=gnu17")
        return (flags, None, None)

    def configure_args(self):
        config_args = []

        if self.spec.satisfies("%nvhpc@:20.11") and (
            self.spec.target.family == "aarch64" or self.spec.target.family == "ppc64le"
        ):
            config_args.append("--disable-strict-compilation")
            config_args.append("--disable-selective-werror")

        return config_args
