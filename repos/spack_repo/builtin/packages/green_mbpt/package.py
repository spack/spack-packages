# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class GreenMbpt(CMakePackage, CudaPackage):
    """GreenMbpt (green-mbpt) provides weak-coupling perturbation expansion and self-energy
    embedding solvers for electronic-structure simulations using Green's function methods.
    """

    # Homepage and source
    homepage = "https://www.green-phys.org"
    url = "https://github.com/Green-Phys/green-mbpt/archive/refs/tags/v0.3.1.tar.gz"

    # Maintainers and License info
    maintainers("egull", "gauravharsha")
    license("MIT", checked_by="egull")

    # Versions and checksums
    version("1.0.0", sha256="cad56c46a1297088f3c484605b7d1dda36b6a7d80bc401d18fe9f7a4ad51acdc")
    version(
        "0.3.2-patch1",
        sha256="d8406553cc19ffb75e4bf626427a1c1c63338930fbd678f6d0ee84032945f985",
        url="https://github.com/Green-Phys/green-mbpt/archive/refs/tags/0.3.2-patch1.tar.gz",
    )
    version("0.3.1", sha256="a7f80bf722fefeb275f66d348c3e756ac0e29b8dd3b67376696587b66e338521")
    version(
        "0.3.0",
        sha256="181873fa442831d21662cf38c15f30ae97d89c07c5256d45232774a5c072574d",
        deprecated=True,
    )  # Known issues, use v0.3.1+

    # Variant for CUDA Kernels
    variant("cuda", default=False, description="Enable CUDA support (requires CUDAToolkit >= 12)")
    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="A value for cuda_arch must be specified. Add cuda_arch=XX."
        "Visit https://developer.nvidia.com/cuda-gpus to find out the architecture of your GPU."
        "You can also run `nvidia-smi` on the compute nodes if the NVIDIA drivers are installed.",
    )

    # Build system dependency
    depends_on("cmake@3.27:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("git", type="build")

    # Other dependencies
    depends_on("mpi")
    depends_on("eigen@3.4.0:4.9.0")
    depends_on("hdf5@1.10.0: ~mpi+hl")
    depends_on("blas")
    depends_on("lapack", when="@1.0.0")

    # CUDA variant dependency
    depends_on("cuda@12:12.9", when="+cuda")

    def cmake_args(self):
        args = []
        # Tell CMake to use Spack's MPI wrappers
        mpi = self.spec["mpi"]
        args.append(self.define("CMAKE_C_COMPILER", mpi.mpicc))
        args.append(self.define("CMAKE_CXX_COMPILER", mpi.mpicxx))
        args.append(self.define("Build_Tests", "OFF"))  # Disable building tests by default
        if "+cuda" in self.spec:
            args.append(self.define("CUSTOM_KERNELS", "https://github.com/Green-Phys/green-gpu"))
            args.append(self.define("GPU_ARCHS", self.spec.variants["cuda_arch"].value[0]))
        return args

    @run_after("install")
    def install_ed_solver(self):
        if not self.spec.satisfies("@1.0.0"):
            return

        source_dir = join_path(self.stage.source_path, "green-seet-solvers")
        build_dir = join_path(source_dir, "spack-build")
        install_dir = join_path(self.prefix, "seet_solvers")
        git = which("git", required=True)
        git("clone", "https://github.com/Green-Phys/green-seet-solvers.git", source_dir)

        mpi = self.spec["mpi"]
        args = [
            self.define("CMAKE_C_COMPILER", mpi.mpicc),
            self.define("CMAKE_CXX_COMPILER", mpi.mpicxx),
            self.define("CMAKE_INSTALL_PREFIX", install_dir),
            self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True),
            self.define("Build_Tests", False),
        ]

        with working_dir(build_dir, create=True):
            cmake(source_dir, *args)
            make()
            make("install")

    def setup_run_environment(self, env):
        # Set environment variable for GreenMbpt
        env.set("GREENMBPT_ROOT", self.prefix)
        if self.spec.satisfies("@1.0.0"):
            env.prepend_path("PATH", join_path(self.prefix, "seet_solvers", "bin"))
