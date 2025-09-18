# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GreenMbpt(CMakePackage):
    """GreenMbpt (green-mbpt) is a weak-coupling perturbation expansion solver for the simulation
    of electronic structure in real materials using first principles Green's function methods.
    """

    homepage = "https://www.green-phys.org"
    url = "https://github.com/Green-Phys/green-mbpt"
    git = "https://github.com/Green-Phys/green-mbpt"
    version("develop", branch="main")

    maintainers("egull", "gauravharsha")
    license("MIT", checked_by="egull")

    # Variant for CUDA Kernels
    variant("cuda", default=False, description="Enable CUDA support (requires CUDAToolkit >= 12)")

    # Build system dependency
    depends_on("cmake@3.27:", type="build")

    # Other dependencies
    depends_on("mpi")
    depends_on("eigen")
    depends_on("hdf5@1.10.0: ~mpi+hl")
    depends_on("blas")

    # CUDA variant dependency
    depends_on("cuda@12:", when="+cuda")

    def cmake_args(self):
        args = []
        # Tell CMake to use Spack's MPI wrappers
        mpi = self.spec['mpi']
        args.append(self.define("CMAKE_C_COMPILER", mpi.mpicc))
        args.append(self.define("CMAKE_CXX_COMPILER", mpi.mpicxx))
        if "+cuda" in self.spec:
            args.append(self.define("CUSTOM_KERNELS", "https://github.com/Green-Phys/green-gpu"))
        return args

    def setup_run_environment(self, env):
        # Set environment variable for GreenMbpt
        env.set("GREENMBPT_ROOT", self.prefix)