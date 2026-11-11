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


class Phloem(CachedCMakePackage, CudaPackage, ROCmPackage):
    """A suite of MPI benchmarks with Umpire memory allocation."""

    homepage = "https://github.com/LLNL/phloem"
    git = "https://github.com/LLNL/phloem.git"
    url = "https://github.com/LLNL/phloem/releases/download/v2.0.0/phloem-v2.0.0.tar.gz"

    maintainers("nhanford")

    license("MIT", checked_by="nhanford")

    version("main", branch="main", submodules=False)
    version("2.0.0", sha256="f1d01297c9a814108406d51c9ac3dd0e97193abde708153a88c97f898d8e0bb4")

    depends_on("blt", type="build")
    depends_on("umpire")
    depends_on("mpi")

    variant("man", default=True, description="Install manual pages")

    with when("+rocm"):
        for arch_ in ROCmPackage.amdgpu_targets:
            depends_on(f"umpire+rocm amdgpu_target={arch_}", when=f"amdgpu_target={arch_}")
        for impl_ in ["openmpi@5:", "mpich", "mvapich-plus", "cray-mpich"]:
            depends_on(f"{impl_} +rocm", when=f"^[virtuals=mpi] {impl_}")

    with when("+cuda"):
        depends_on("umpire+cuda")
        for impl_ in ["openmpi@5:", "mpich", "mvapich-plus", "cray-mpich"]:
            depends_on(f"{impl_} +cuda", when=f"^[virtuals=mpi] {impl_}")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def initconfig_mpi_entries(self):
        entries = super().initconfig_mpi_entries()
        entries.extend(
            [
                cmake_cache_option("ENABLE_MPI", True),
                cmake_cache_path("MPI_HOME", self.spec["mpi"].prefix),
            ]
        )
        return entries

    def cmake_args(self):
        args = []

        args.extend(
            [
                self.define_from_variant("ENABLE_HIP", "rocm"),
                self.define_from_variant("ENABLE_CUDA", "cuda"),
                self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix),
            ]
        )
        if self.spec.satisfies("+man"):
            args.append(self.define("CMAKE_INSTALL_MANDIR", self.prefix.man))
        if self.spec.satisfies("+rocm") and self.spec.satisfies("^cray-mpich"):
            mpi_link_flags = self.spec["mpi"].libs.link_flags
            mpi_link_flags += "-lmpi_gtl_hsa"
            args.append(self.define("BLT_MPI_LINK_FLAGS", mpi_link_flags))
        return args
