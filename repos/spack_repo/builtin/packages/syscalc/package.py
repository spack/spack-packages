# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Syscalc(CMakePackage):
    """A tool to derive theoretical systematic uncertainties"""

    homepage = "https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/SysCalc"
    url = "https://bazaar.launchpad.net/~mgtools/mg5amcnlo/SysCalc/tarball/17"

    # This is a mirror + added CMakeLists.txt file
    git = "https://github.com/paulgessinger/SysCalc.git"

    version("1.1.7", commit="d62edf92b04a6cf89cde6837b0a999bc79601e8f")

    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    tags = ["hep"]

    depends_on("lhapdf@6:")
    depends_on("tinyxml2")

    def url_for_version(self, version):
        url = self.url.rsplit("/", 1)[0]
        url += "/SysCalc_V{0}.tar.gz"

        url = url.format(version)
        return url
