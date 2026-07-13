# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems import autotools, meson
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *


class Libgpiod(AutotoolsPackage, MesonPackage):
    """C library and tools for interacting with the linux GPIO character device
    (gpiod stands for GPIO device)"""

    homepage = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/about/"
    git = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod"

    maintainers("davekeeshan")

    license("LGPL-2.1-or-later")

    # libgpiod switched from autotools to meson in the 2.3 release series
    build_system(
        conditional("autotools", when="@:2.2"),
        conditional("meson", when="@2.3:"),
        default="meson",
    )

    version("master", branch="master")
    version("2.3.1", sha256="33ae7069ba1558b4b0f5385479c2a357a05f70998535c19d170079597ff7d09c")
    version("2.3.0", sha256="aff97f550327a03b2200da4460ca629fce5b110ad3ae1ba3820689a78f90f9c2")
    version("2.2.5", sha256="f4eb223c6f56df930d335def9609103773a028d71716d350a196c867af707e34")
    version("2.2.4", sha256="fc8294633f1579648c77dac2afc9c05d6db05285c62ecd3d0ccbab34b4d538ce")
    version("2.2.3", sha256="70de4639856620571f99d851cf1acd48f6462b62ccba929f1a0235ec76b4e4dc")
    version("2.2.2", sha256="02794831a65adab942620dd3e8f038ff881c3c127d7d26841d94caa8caea793f")
    version("2.2.1", sha256="c6054a64a12681beeb0ce5200867754843bb68465b06c543f132ad984aee3f83")
    version("2.2.0", sha256="9af73e884b06f63ee777938999a6f563a02dd9afdb785a5a7479e94ac2d99f75")
    version("2.1.3", sha256="aa1bd204982862cf991eb827a244867969f7d6f5361d56514f599d9724a33974")
    version("2.1.2", sha256="87b093d07d34f2180df5cd7425209cff5e77b79343485e5dda1c27108bda1dbd")
    version("2.1.1", sha256="2ca57a484d4d5d4005778b032c06156a09d0536160eb8de7713ed3346b873d40")
    version("2.1.0", sha256="00eed92b31dd15fc995a41650dbf705b227958c444866fd082b415c1b2a53b95")
    version("2.0.2", sha256="dc2d13ff73d42bba1bad80a67745f97e5594c84d087534a0d0b710b2c090d8a3")
    version("2.0.1", sha256="cf0d4db1d94cc99281de142063d0e28f42760c4d918d6b8854e1b27811517c34")
    version("2.0.0", sha256="a0f835c4ca4a2a3ca021090b574235ba58bb9fd612d8a6051fb1350054e04fdd")
    version("1.6.5", sha256="7715458859333fe111f900d23baac459a5e0629881e6490779de79fce49373fb")
    version("1.6.4", sha256="9f920260c46b155f65cba8796dcf159e4ba56950b85742af357d75a1af709e68")
    version("1.6.3", sha256="b4b8d4ffc13777ce7540532e47458924df475dd3eb7d4fb4afcca7fe3fe03595")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")

    with when("build_system=autotools"):
        depends_on("autoconf", type="build")
        depends_on("autoconf-archive", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")

    def url_for_version(self, version):
        # Patch-0 releases are tagged without the trailing ".0" (e.g. v2.3, not v2.3.0)
        if version[2] == 0:
            return f"https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-v{version.up_to(2)}.tar.gz"
        else:
            return f"https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-v{version}.tar.gz"


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def autoreconf(self, pkg, spec, prefix):
        Executable("./autogen.sh")()


class MesonBuilder(meson.MesonBuilder):
    def meson_args(self):
        return [
            "-Dtools=enabled",
            "-Dtests=disabled",
            "-Dexamples=disabled",
            "-Dbindings-cxx=disabled",
            "-Dgpioset-interactive=disabled",
        ]
