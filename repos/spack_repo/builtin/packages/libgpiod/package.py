# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems import meson
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libgpiod(AutotoolsPackage, MesonPackage):
    """C library and tools for interacting with the linux GPIO character device
    (gpiod stands for GPIO device)"""

    homepage = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/"
    url = "https://mirrors.edge.kernel.org/pub/software/libs/libgpiod/libgpiod-2.3.1.tar.xz"
    git = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod"

    maintainers("davekeeshan")

    license("LGPL-2.1-or-later")

    # libgpiod switched from autotools to meson in the 2.3 release series
    build_system(
        conditional("autotools", when="@:2.2"), conditional("meson", when="@2.3:"), default="meson"
    )

    version("master", branch="master")
    version("2.3.1", sha256="e3a358a90a9204ff16f92b6f4028ed91460b1926f10589eb54b3566484650a30")
    version("2.3.0", sha256="cb71db463aec2604ac520c95bf04eff1839d86bdc9a2dfd67ef879fbb10426ea")
    version("2.2.5", sha256="0df1bb2be89d9091a167b9f702f8f31d89863e8d84997aad09ee4aba12fe78c5")
    version("2.2.4", sha256="13207176b0eb9b3e0f02552d5f49f5a6a449343ce47416158bb484d9d3019592")
    version("2.2.3", sha256="70012b0262e4b90f140431efa841ca89643b02ea6c09f507e23cec664a51b71a")
    version("2.2.2", sha256="7e3bff0209d75fbca2e9fcff1fd5f07cc58b543e129e08b6d4bb1e4a56cfec0d")
    version("2.2.1", sha256="0e948049c309b87c220fb24ee0d605d7cd5b72f22376e608470903fffa2d4b18")
    version("2.2.0", sha256="ee29735890eb1cc0e4b494001da5163d1a9c4735343201d22485db313601ca07")
    version("2.1.3", sha256="2be4c0b03e995d236c0e476e14aeb475d7b431dd1439609b6d65c540f91eaf58")
    version("2.1.2", sha256="7a148a5a7d1c97a1abb40474b9a392b6edd7a42fe077dfd7ff42cfba24308548")
    version("2.1.1", sha256="b21913f469d3135680d5516f00fdf9f81d5e564e19ffb690927ea7f1d7e312cb")
    version("2.1.0", sha256="fa4024a080121c958502f9a46a5bda44bea85e7a4dd7fcb3dead463b6fc4261c")
    version("2.0.2", sha256="c3c923dc63b7b1b02639c9179c81e3d9febf0887bbaa59775990229cdbedb88b")
    version("2.0.1", sha256="b5367d28d045b36007a4ffd42cceda4c358737ef4f2ce22b0c1d05ec57a38392")
    version("2.0.0", sha256="f74cbf82038b3cb98ebeb25bce55ee2553be28194002d2a9889b9268cce2dd07")
    version("1.6.5", sha256="ae280f697bf035a1fb780c9972e5c81d0d2712b7ab6124fb3fba24619daa72bc")
    version("1.6.4", sha256="7b146e12f28fbca3df7557f176eb778c5ccf952ca464698dba8a61b2e1e3f9b5")
    version("1.6.3", sha256="841be9d788f00bab08ef22c4be5c39866f0e46cb100a3ae49ed816ac9c5dddc7")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")

    def url_for_version(self, version):
        # Release tarballs for x.y.0 drop the trailing ".0" (e.g. 2.3, not 2.3.0)
        base = "https://mirrors.edge.kernel.org/pub/software/libs/libgpiod"
        if version[2] == 0:
            return f"{base}/libgpiod-{version.up_to(2)}.tar.xz"
        return f"{base}/libgpiod-{version}.tar.xz"


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        return [
            "-Dtools=enabled",
            "-Dtests=disabled",
            "-Dexamples=disabled",
            "-Dbindings-cxx=disabled",
            "-Dgpioset-interactive=disabled",
        ]
