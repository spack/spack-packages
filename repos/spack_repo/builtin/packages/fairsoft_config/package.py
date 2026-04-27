# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class FairsoftConfig(CMakePackage):
    """Legacy fairsoft-config script"""

    homepage = "https://github.com/FairRootGroup/fairsoft-config"
    git = "https://github.com/FairRootGroup/fairsoft-config"
    maintainers("dennisklein", "fuhlig1", "jezwilkinson")

    version("master")

    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        multi=False,
        description="C++ standard reported",
    )

    variant(
        "fairsoft_version",
        default="develop",
        values=("develop", "may25"),
        multi=False,
        description="Installed version of fairsoft-bundle",
    )

    depends_on("cmake@3:", type="build")
    depends_on("root", type=("build", "link", "run"))

    def cmake_args(self):
        args = []
        args += [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define_from_variant("FAIRSOFT_VERSION", "fairsoft_version"),
        ]
        return args
