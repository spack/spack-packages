# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class GreenMbpt(CMakePackage, CudaPackage):
    """GreenMbpt (green-mbpt) is a weak-coupling perturbation expansion solver for the simulation
    of electronic structure in real materials using first principles Green's function methods.
    """

    # Homepage and source
    homepage = "https://www.green-phys.org"
    url = "https://github.com/Green-Phys/green-mbpt/archive/refs/tags/v0.3.0.tar.gz"

    # Maintainers and License info
    maintainers("egull", "gauravharsha")
    license("MIT", checked_by="egull")

    # Versions and checksums
    version("0.3.0", sha256="181873fa442831d21662cf38c15f30ae97d89c07c5256d45232774a5c072574d")

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
        mpi = self.spec["mpi"]
        args.append(self.define("CMAKE_C_COMPILER", mpi.mpicc))
        args.append(self.define("CMAKE_CXX_COMPILER", mpi.mpicxx))
        if "+cuda" in self.spec:
            args.append(self.define("CUSTOM_KERNELS", "https://github.com/Green-Phys/green-gpu"))
            args.append(self.define("GPU_ARCH", self.spec.variants["cuda_arch"].value[0]))
        return args

    def setup_run_environment(self, env):
        # Set environment variable for GreenMbpt
        env.set("GREENMBPT_ROOT", self.prefix)
