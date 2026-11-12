# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Adms(AutotoolsPackage):
    """ADMS is a code generator that converts electrical compact device models
    specified in high-level description language into ready-to-compile c code
    for the API of spice simulators."""

    homepage = "https://sourceforge.net/projects/mot-adms/"
    url = "https://github.com/Qucs/ADMS/releases/download/release-2.3.7/adms-2.3.7.tar.gz"
    git = "https://github.com/Qucs/ADMS.git"

    maintainers("cessenat")

    license("GPL-3.0-only")

    version("master", branch="master")
    version("2.3.7", sha256="3a78e1283ecdc3f356410474b3ff44c4dcc82cb89772087fd3bbde8a1038ce08")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

        depends_on("bison@2.5:")
        depends_on("flex")
        depends_on("perl-xml-libxml")

        depends_on("autoconf", when="@master")
        depends_on("automake", when="@master")
        depends_on("libtool", when="@master")

    # https://github.com/Qucs/ADMS/issues/116
    conflicts("%gcc@15:", msg="ADMS is no longer actively maintained and fails on newer compilers")

    @when("@master")
    def autoreconf(self, spec, prefix):
        sh = which("sh", required=True)
        sh("./bootstrap.sh")
