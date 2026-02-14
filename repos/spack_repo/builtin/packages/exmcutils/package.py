# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Exmcutils(AutotoolsPackage):
    """ExM C-Utils: Generic C utility library for ADLB/X and Swift/T"""

    homepage = "http://swift-lang.org/Swift-T"
    url = "https://swift-lang.github.io/swift-t-downloads/spack/exmcutils-0.6.4.tar.gz"
    git = "https://github.com/swift-lang/swift-t.git"

    maintainers("j-woz")

    version("master", branch="master")
    version("0.6.4", sha256="7a0c473cdb3eb97379e4aaf7be5cd04f57c463726d1a1a0b3ab73de6763b8b7c")
    version("0.6.0", sha256="43812f79ae83adcacc05d4eb64bc8faa1c893994ffcdfb40a871f6fa4c9c1435")
    version("0.5.7", sha256="6b84f43e8928d835dbd68c735ece6a9b7c648a1a4488ec2b1d2f3c4ceec508e8")
    version("0.5.6", sha256="296ba85cc828bd816c7c4de9453f589da37f32854a58ffda3586b6f371a23abf")

    depends_on("c", type="build")  # generated

    @property
    def configure_directory(self):
        if self.version == Version("master"):
            return "c-utils/code"
        else:
            return "."

    def autoreconf(self, spec, prefix):
        which("bash", required=True)("bootstrap")

    depends_on("m4", when="@master")
    depends_on("autoconf", when="@master")
    depends_on("automake", when="@master")
    depends_on("libtool", when="@master")
