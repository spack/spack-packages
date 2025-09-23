# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GreenSeet(CMakePackage):
    """Green-SEET is a multi-scale Green's function embedding code that combines the Green's
    function weak-coupling perturbation theories (GF2 and GW) and self-energy embedding theory
    (SEET) to treat strongly correlated systems. The code is developed to perform
    ab initio calculations of realistic periodic systems with large unit cells containing
    transition metal atoms.
    """

    # Homepage and source
    homepage = "https://www.green-phys.org"
    url = "https://github.com/Green-Phys/green-mbpt"
    git = "https://github.com/Green-Phys/green-mbpt"

    # Maintainers and License info
    maintainers("egull", "gauravharsha")
    license("MIT")

    # Versions and checksums
    version("seet-dev", branch="SEET", commit="7b076bf07930157d9583f9e942867bc08605a4dd")

    # Build system dependency
    depends_on("cmake@3.27:", type="build")

    # Other dependencies
    depends_on("mpi")
    depends_on("eigen")
    depends_on("hdf5@1.10.0: ~mpi+hl")
    depends_on("blas")
    depends_on("arpack-ng@3.5.0:")
    depends_on("alpscore@2.3.2:")

    # TODO: CUDA Variant -- consider later

    def cmake_args(self):
        args = []
        # Tell CMake to use Spack's MPI wrappers
        mpi = self.spec["mpi"]
        args.append(self.define("CMAKE_C_COMPILER", mpi.mpicc))
        args.append(self.define("CMAKE_CXX_COMPILER", mpi.mpicxx))
        return args

    def install(self, spec, prefix):
        # ---------- Step 1: Build green-seet-solvrs ----------
        # NOTE: green-seet-solvers will be merged into green-mbpt for next SEET release
        seet_solvers_src_dir = join_path(self.stage.source_path, "seet_solvers_src")
        git = which("git")
        git("clone", "https://github.com/Green-Phys/green-seet-solvers.git", seet_solvers_src_dir)

        seet_solvers_build_dir = join_path(seet_solvers_src_dir, "spack-build")
        seet_solvers_install_dir = join_path(prefix, "seet_solvers")

        args = self.cmake_args() + [
            self.define("ALPSCore_DIR", spec["alpscore"].prefix),
            self.define("ARPACK_DIR", spec["arpack-ng"].prefix),
            self.define("CMAKE_INSTALL_PREFIX", seet_solvers_install_dir),
            self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True),
        ]

        with working_dir(seet_solvers_build_dir, create=True):
            cmake(seet_solvers_src_dir, *args)
            make()
            make("install")

        # ---------- Step 2: Build main project ----------
        build_dir = join_path(self.stage.source_path, "spack-build")
        args_main = self.cmake_args() + [self.define("CMAKE_INSTALL_PREFIX", prefix)]

        with working_dir(build_dir, create=True):
            cmake(self.stage.source_path, *args_main)
            make()
            make("install")

    def setup_run_environment(self, env):
        # Set environment variable for GreenSeet
        env.set("GREENSEET_ROOT", self.prefix)
