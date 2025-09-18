# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Openroad(CMakePackage):
    """OpenROAD is an integrated chip design and layout tool that takes a
    design from RTL to GDSII."""

    homepage = "https://the-openroad-project.org/"
    git = "https://github.com/The-OpenROAD-Project/OpenROAD.git"

    version("master", branch="master", submodules=True)
    version("24Q3", tag="24Q3", submodules=True)

    depends_on("cudd")
    depends_on("boost@1.83.0 cxxstd=17 +serialization +system +thread")
    depends_on("eigen")
    depends_on("googletest@1.14.0")
    depends_on("lemon")
    depends_on("or-tools")
    depends_on("spdlog cxxstd=17")
    depends_on("swig")
    depends_on("tcl")
    depends_on("yosys")

    def cmake_args(self):
        args = [
            self.define("Boost_NO_SYSTEM_PATHS", True),
            self.define("BOOST_ROOT", self.spec["boost"].prefix),
            self.define("BUILD_PYTHON", True),
            self.define("ENABLE_GUI", False),
            self.define("ENABLE_TESTS", False),
            self.define("CUDD_DIR", self.spec["cudd"].prefix),
        ]
        return args
