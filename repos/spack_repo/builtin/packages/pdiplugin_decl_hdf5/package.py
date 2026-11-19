# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

from ..pdi.package import Pdi


class PdipluginDeclHdf5(CMakePackage):
    """Decl'HDF5 plugin enables one to read and write data from HDF5 files in a
    declarative way. Decl'HDF5 does not support the full HDF5 feature set but
    offers a simple declarative interface to access a large subset of it for the
    PDI library"""

    homepage = "https://pdi.dev"
    git = "https://github.com/pdidev/pdi.git"
    url = "https://github.com/pdidev/pdi/archive/refs/tags/1.8.0.tar.gz"

    license("BSD-3-Clause")

    maintainers("jbigot")

    for v in Pdi.versions:
        version(str(v), **Pdi.versions[v])

    variant("benchs", default=False, description="Build benchmarks")
    variant("mpi", default=True, description="Enable parallel HDF5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # I would prefer fortran to be a test dependency but it failed to concretize in Spack 1.2.2
    depends_on("fortran", type="build")

    for v in Pdi.versions:
        depends_on(f"pdiplugin-mpi@{str(v)}", type="test", when=f"@{str(v)}+mpi")

    depends_on("cmake@3.22.1:", type=("build"), when="@1.10.0:")
    depends_on("cmake@3.16.3:", type=("build"))
    depends_on("hdf5@1.10.7:2 +shared", type=("build", "link", "run"), when="@1.10.0:")
    depends_on("hdf5@1.10.4:2 +shared", type=("build", "link", "run"))
    depends_on("hdf5 +mpi", type=("build", "link", "run"), when="+mpi")
    depends_on("mpi", when="+mpi")
    for v in Pdi.versions:
        depends_on("pdi@" + str(v), type=("link", "run"), when="@" + str(v))
    depends_on("pkgconfig", type=("build"))
    depends_on("pdi +fortran", type="test")

    root_cmakelists_dir = "plugins/decl_hdf5"

    def cmake_args(self):
        return [
            "-DINSTALL_PDIPLUGINDIR:PATH={:s}".format(self.prefix.lib),
            self.define_from_variant("BUILD_BENCHMARKING", "benchs"),
            self.define("BUILD_FORTRAN", self.run_tests),
            self.define_from_variant("BUILD_HDF5_PARALLEL", "mpi"),
            self.define("BUILD_TESTING", self.run_tests),
        ]

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PRTE_MCA_rmaps_default_mapping_policy", ":oversubscribe")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PDI_PLUGIN_PATH", self.prefix.lib)
