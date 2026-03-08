# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Syscalc(MakefilePackage, CMakePackage):
    """A tool to derive theoretical systematic uncertainties"""

    homepage = "https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/SysCalc"
    url = "https://bazaar.launchpad.net/~mgtools/mg5amcnlo/SysCalc/tarball/17"

    build_system(
        conditional("makefile", when="@1.1.7"),
        conditional("cmake", when="1.1.7.paulgessinger"),
        default="cmake",
    )

    version(
        "1.1.7.paulgessinger.p1-4-gd62edf9",
        commit="d62edf92b04a6cf89cde6837b0a999bc79601e8f",
        git="https://github.com/paulgessinger/SysCalc.git",
    )
    version(
        "1.1.7",
        sha256="ac73df0f9f195eb62601fafc2eede3db17a562750f7971616870d6df4abd1b6c",
        url="https://bazaar.launchpad.net/~mgtools/mg5amcnlo/SysCalc/tarball/17",
        extension=".tgz",
        deprecated=True,
    )

    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated
    depends_on("pkgconfig", type="build")

    tags = ["hep"]

    depends_on("lhapdf@6:")
    depends_on("tinyxml2", when="build_system=cmake")

    def url_for_version(self, version):
        url = self.url.rsplit("/", 1)[0]
        url += "/SysCalc_V{0}.tar.gz"

        url = url.format(version)
        return url

    @when("build_system=makefile")
    def build(self, spec, prefix):
        with working_dir("mg5amcnlo/SysCalc"):
            make("all")

    @when("build_system=makefile")
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with working_dir("mg5amcnlo/SysCalc"):
            install("sys_calc", prefix.bin)
            install_tree("include", prefix.include)
