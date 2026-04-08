# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Roounfold(CMakePackage):
    """RooUnfold — Unfolding framework based on RooFit/ROOT.

    A framework implementing several unfolding algorithms for use in HEP analyses.
    """

    homepage = "https://gitlab.cern.ch/RooUnfold/RooUnfold"
    url = "https://gitlab.cern.ch/RooUnfold/RooUnfold/-/archive/3.1.0/RooUnfold-3.1.0.zip"
    git = "https://gitlab.cern.ch/RooUnfold/RooUnfold.git"

    tags = ["hep"]

    maintainers("wdconinc")

    license("BSD-3-Clause", checked_by="wdconinc")

    version("3.1.0", sha256="51daf6373971512ce5882574bb18a373e68a0a2e1f824141ff99d6488d43cbf9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")

    depends_on("root+roofit")

    def cmake_args(self):
        args = [self.define("CMAKE_DISABLE_FIND_PACKAGE_Doxygen", True)]
        return args
