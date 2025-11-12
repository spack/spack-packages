# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cached_cmake import (
    CachedCMakePackage,
    cmake_cache_option,
    cmake_cache_path,
)
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Quandary(CachedCMakePackage, CudaPackage, ROCmPackage):
    """Optimal control for open quantum systems"""

    homepage = "https://github.com/LLNL/quandary"
    git = "https://github.com/LLNL/quandary.git"

    maintainers("steffi7574", "tdrwenski", "adrienbernede")

    license("MIT", checked_by="tdrwenski")

    version("main", branch="main", preferred=True)
    version("4.3", tag="v4.3", commit="d5087e7ac82665ceb028b492c88b3fe8acd5cd13")
    version("4.2", tag="v4.2", commit="557675fd76daf9fd0be7ebd6321bf2afcb6a6b9c")
    version("learning", branch="learning")

    variant("slepc", default=False, description="Build with SLEPc library")
    variant("int64", default=False, description="Use 64 bit ints for PetscInts")
    variant("test", default=False, description="Add dependencies needed for testing")
    variant("werror", default=False, description="Enable warnings as errors")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("petsc~hypre~metis~fortran")
    depends_on("petsc+debug", when="build_type=Debug")
    depends_on("petsc~debug", when="build_type=Release")
    depends_on("petsc~debug", when="build_type=RelWithDebInfo")
    depends_on("petsc+int64", when="+int64")
    depends_on("petsc~int64", when="~int64")

    depends_on("slepc", when="+slepc")
    depends_on("mpi", type=("build", "link", "run"))

    depends_on("blt@0.6.0:", type="build")

    with when("+rocm"):
        for arch_ in ROCmPackage.amdgpu_targets:
            depends_on(f"petsc+rocm amdgpu_target={arch_}", when=f"amdgpu_target={arch_}")

    with when("+cuda"):
        for sm_ in CudaPackage.cuda_arch_values:
            depends_on(f"petsc+cuda cuda_arch={sm_}", when=f"cuda_arch={sm_}")

    with when("+test"):
        depends_on("python", type="run")
        depends_on("py-pip", type="run")

    build_targets = ["all"]
    install_targets = ["install"]

    def initconfig_package_entries(self):
        spec = self.spec
        entries = []

        entries.append(cmake_cache_path("BLT_SOURCE_DIR", spec["blt"].prefix))
        entries.append(cmake_cache_option("WITH_SLEPC", spec.satisfies("+slepc")))
        entries.append(cmake_cache_option("ENABLE_WARNINGS_AS_ERRORS", spec.satisfies("+werror")))

        return entries
