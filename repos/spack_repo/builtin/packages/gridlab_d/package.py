# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from typing import List

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GridlabD(CMakePackage):
    """
    CMake package for Gridlab-D, a new power distribution system simulation
    and analysis tool that provides valuable information to users who design
    and operate distribution systems, and to utilities that wish to take
    advantage of the latest energy technologies. Gridlab-D is a flexible
    simulation environment that can be integrated with a variety of third-party
    data management and analysis tools.
    """

    homepage = "https://www.gridlabd.org/"
    git = "https://github.com/gridlab-d/gridlab-d"

    maintainers("0t1s1", "yee29", "afisher1")

    # Using only develop as other branches and releases historically did not build properly.
    version("develop", branch="develop", submodules=True)

    variant("mysql", default=False, description="Enable MySQL support for Gridlab-D.")
    variant("helics", default=False, description="Enable Helics support for Gridlab-D.")

    # Add dependencies.
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.10:", type="build")
    depends_on("xerces-c@3.2.0:")
    # depends_on("superlu-mt") gridlab-d now uses its own internal version
    depends_on("helics@3.1.0:", when="+helics")
    depends_on("mysql", when="+mysql")
    depends_on("ncurses+termlib", when="+mysql")
    depends_on("pkgconfig", when="+mysql", type="build")

    patch("find_mysql_pkg_conf.patch", when="+mysql")

    def cmake_args(self):
        args = []

        args.append("-DXercesC_ROOT=" + self.spec["xerces-c"].prefix)

        if self.spec.satisfies("+helics"):
            args.append("-DGLD_USE_HELICS=ON")
            args.append("-DGLD_HELICS_DIR=" + self.spec["helics"].prefix)
        else:
            args.append("-DGLD_USE_HELICS=OFF")

        if self.spec.satisfies("+mysql"):
            args.append("-DGLD_USE_MYSQL=ON")
            args.append("-DGLD_MYSQL_DIR=" + self.spec["mysql"].prefix)
        else:
            args.append("-DGLD_USE_MYSQL=OFF")

        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Need to add GLPATH otherwise Gridlab-D will not run.
        env.set("GLPATH", self.prefix.lib)
        env.prepend_path("GLPATH", self.prefix.share)

    def flag_handler(self, name: str, flags: List[str]):
        # gridlab-d's C++ code isn't strict-standards-compliant and needs
        # -fpermissive on GCC/Clang-family compilers to build at all.
        if name == "cxxflags":
            if (
                self.spec.satisfies("%gcc")
                or self.spec.satisfies("%clang")
                or self.spec.satisfies("%apple-clang")
            ):
                flags.append("-fpermissive")
        if name == "ldflags" and self.spec.satisfies("^ncurses+termlib"):
            flags.append("-ltinfo")
        return (flags, None, None)
