# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Amg2023(CMakePackage, CudaPackage, ROCmPackage):
    """AMG2023 is a parallel algebraic multigrid solver for linear systems
    arising from problems on unstructured grids. The driver provided here
    builds linear systems for various 3-dimensional problems. It requires
    an installation of hypre-2.29.0 or higher.
    """

    tags = ["benchmark"]
    homepage = "https://github.com/LLNL/AMG2023"
    url = "https://github.com/llnl/AMG2023/archive/refs/tags/20261006.tar.gz"
    git = "https://github.com/LLNL/AMG2023.git"

    maintainers("liruipeng")

    license("Apache-2.0")

    version("develop", branch="main")
    version(
        "20261006",
        sha256="0ce8fe631cde79932d30f2c8f9ee08d160bc2c2ffba6ece8fa029f30256ecc71",
        preferred=True,
    )
    version("20240511", branch="20240511")

    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("caliper", default=False, description="Enable Caliper monitoring")
    variant("umpire", default=False, description="Enable Umpire support")
    variant("mixedint", default=False, description="Use 64bit integers while reducing memory use")
    variant("gpu-aware-mpi", default=False, description="Enable GPU aware MPI")

    # AMG2023's CMake project starts as C, but later enables CXX and links
    # the executable with the C++ linker. Both language dependencies are needed
    # so Spack's compiler wrappers set CC/CXX and linker wrapper arguments.
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")

    depends_on("mpi", when="+mpi")

    with when("+umpire"):
        depends_on("umpire@2026.07.2:", when="@develop")
        depends_on("umpire@2026.07.2", when="@20261006")

    depends_on("hypre+mpi", when="+mpi")
    requires("+mpi", when="^hypre+mpi")
    depends_on("caliper", when="+caliper")
    depends_on("adiak", when="+caliper")
    depends_on("hypre+caliper", when="+caliper")
    depends_on("hypre@:2.29.0", when="@20240511")
    depends_on("hypre@3.2.0", when="@20261006")
    depends_on("hypre@3.2.0:", when="@develop")
    depends_on("hypre~fortran")
    depends_on("hypre+mixedint", when="+mixedint")

    depends_on("hypre~cuda", when="~cuda")

    conflicts("+umpire", when="~cuda~rocm")

    with when("+cuda"):
        depends_on("hypre+cuda")
        with when("+umpire"):
            depends_on("hypre+umpire")
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on("hypre cuda_arch={0}".format(sm_), when="cuda_arch={0}".format(sm_))
            depends_on(
                "umpire cuda_arch={0}".format(sm_),
                when="+umpire cuda_arch={0}".format(sm_),
            )

    depends_on("hypre~rocm", when="~rocm")
    with when("+rocm"):
        depends_on("hypre+rocm")
        with when("+umpire"):
            depends_on("hypre+umpire")
        for arch in ROCmPackage.amdgpu_targets:
            depends_on("hypre amdgpu_target={0}".format(arch), when="amdgpu_target={0}".format(arch))
            depends_on(
                "umpire amdgpu_target={0}".format(arch),
                when="+umpire amdgpu_target={0}".format(arch),
            )

    depends_on("hypre+gpu-aware-mpi", when="+mpi+gpu-aware-mpi")

    def cmake_args(self):
        cmake_options = []
        cmake_options.append(self.define_from_variant("AMG_WITH_CALIPER", "caliper"))
        cmake_options.append(self.define_from_variant("AMG_WITH_OMP", "openmp"))
        cmake_options.append(self.define_from_variant("AMG_WITH_UMPIRE", "umpire"))
        cmake_options.append(self.define("HYPRE_PREFIX", self.spec["hypre"].prefix))
        if self.spec["hypre"].satisfies("+cuda"):
            cmake_options.append(self.define("AMG_WITH_CUDA", True))

        if self.spec["hypre"].satisfies("+rocm"):
            cmake_options.append(self.define("AMG_WITH_HIP", True))

        if self.spec["hypre"].satisfies("+mpi"):
            cmake_options.append(self.define("AMG_WITH_MPI", True))

        return cmake_options
