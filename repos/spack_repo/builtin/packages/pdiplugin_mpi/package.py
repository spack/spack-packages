# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from ..pdi.package import Pdi


class PdipluginMpi(CMakePackage):
    """MPI plugin for the PDI library"""

    homepage = "https://pdi.dev"
    git = "https://github.com/pdidev/pdi.git"
    url = "https://github.com/pdidev/pdi/archive/refs/tags/1.8.0.tar.gz"

    license("BSD-3-Clause")

    maintainers("jbigot")

    for v in Pdi.versions:
        version(str(v), **Pdi.versions[v])

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # I would prefer fortran to be a test dependency but it failed to concretize in Spack 1.2.2
    depends_on("fortran", type="build")

    depends_on("cmake@3.22.1:", type=("build"), when="@1.10.0:")
    depends_on("cmake@3.16.3:", type=("build"))
    depends_on("mpi", type=("build", "link", "run"))
    for v in Pdi.versions:
        depends_on("pdi@" + str(v), type=("link", "run"), when="@" + str(v))
    depends_on("pkgconfig", type=("build"))
    depends_on("pdi +fortran", type="test")

    root_cmakelists_dir = "plugins/mpi"

    def cmake_args(self):
        return [
            "-DINSTALL_PDIPLUGINDIR:PATH={:s}".format(self.prefix.lib),
            self.define("BUILD_FORTRAN", self.run_tests),
            self.define("BUILD_TESTING", self.run_tests),
        ]

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PDI_PLUGIN_PATH", self.prefix.lib)
