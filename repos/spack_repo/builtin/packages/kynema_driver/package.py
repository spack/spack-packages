# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class KynemaDriver(CMakePackage, CudaPackage, ROCmPackage):
    """Multi-application driver for Kynema project."""

    homepage = "https://github.com/Kynema/kynema-driver"
    git = "https://github.com/Kynema/kynema-driver.git"

    maintainers("jrood-nrel")

    tags = ["ecp", "ecp-apps"]
    submodules = True

    license("Apache-2.0")

    version("main", branch="main")

    variant("kynema_sgf_gpu", default=False, description="Enable Kynema-SGF on the GPU")
    variant("kynema_ugf_gpu", default=False, description="Enable Kynema-UGF on the GPU")
    variant("sycl", default=False, description="Enable SYCL backend for Kynema-SGF")
    variant("gpu-aware-mpi", default=False, description="gpu-aware-mpi")
    variant("kynema-fmb", default=False, description="Couple with Kynema-FMB structural solver")
    variant("pic", default=True, description="Enable position independent code")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    for arch in CudaPackage.cuda_arch_values:
        depends_on(
            "kynema-sgf+cuda cuda_arch=%s" % arch, when="+kynema_sgf_gpu+cuda cuda_arch=%s" % arch
        )
        depends_on(
            "kynema-ugf+cuda cuda_arch=%s" % arch, when="+kynema_ugf_gpu+cuda cuda_arch=%s" % arch
        )
        depends_on(
            "trilinos+cuda cuda_arch=%s" % arch, when="+kynema_ugf_gpu+cuda cuda_arch=%s" % arch
        )

    for arch in ROCmPackage.amdgpu_targets:
        depends_on(
            "kynema-sgf+rocm amdgpu_target=%s" % arch,
            when="+kynema_sgf_gpu+rocm amdgpu_target=%s" % arch,
        )
        depends_on(
            "kynema-ugf+rocm amdgpu_target=%s" % arch,
            when="+kynema_ugf_gpu+rocm amdgpu_target=%s" % arch,
        )
        depends_on(
            "trilinos+rocm amdgpu_target=%s" % arch,
            when="+kynema_ugf_gpu+rocm amdgpu_target=%s" % arch,
        )

    depends_on("kynema-ugf+hypre+openfast+tioga")
    depends_on("kynema-sgf+netcdf+mpi+tiny_profile")
    depends_on("trilinos")
    depends_on("yaml-cpp@0.6:")
    depends_on("tioga~nodegid")
    depends_on("openfast+cxx@2.6.0:")
    depends_on("kynema-ugf+kynema-fmb", when="+kynema-fmb")
    depends_on("kynema-sgf+sycl", when="+kynema_sgf_gpu+sycl")
    depends_on("kokkos-nvcc-wrapper", type="build", when="+cuda")
    depends_on("mpi")
    depends_on("kynema-ugf+gpu-aware-mpi", when="+gpu-aware-mpi")
    depends_on("kynema-sgf+gpu-aware-mpi", when="+gpu-aware-mpi")

    with when("~kynema_sgf_gpu~kynema_ugf_gpu"):
        conflicts("+cuda")
        conflicts("+rocm")
        conflicts("+sycl")
    with when("~kynema_ugf_gpu"):
        conflicts("^kynema-ugf+cuda")
        conflicts("^kynema-ugf+rocm")
    with when("~kynema_sgf_gpu"):
        conflicts("^kynema-sgf+cuda")
        conflicts("^kynema-sgf+rocm")
        conflicts("^kynema-sgf+sycl")
    conflicts("+kynema_sgf_gpu", when="~cuda~rocm~sycl")
    conflicts("+kynema_ugf_gpu", when="~cuda~rocm")
    conflicts("+kynema_ugf_gpu", when="+sycl")
    conflicts("^kynema-sgf+hypre", when="~kynema_sgf_gpu+kynema_ugf_gpu")
    conflicts("^kynema-sgf+hypre", when="+kynema_sgf_gpu~kynema_ugf_gpu")
    conflicts("+sycl", when="+cuda")
    conflicts("+rocm", when="+cuda")
    conflicts("+sycl", when="+rocm")

    def cmake_args(self):
        spec = self.spec

        args = [self.define("MPI_HOME", spec["mpi"].prefix)]

        args.append(self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"))

        if spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx))
            args.append(self.define("CMAKE_C_COMPILER", spec["mpi"].mpicc))
            args.append(self.define("KYNEMA_DRIVER_ENABLE_CUDA", True))
            args.append(
                self.define("KYNEMA_DRIVER_CUDA_ARCH", self.spec.variants["cuda_arch"].value)
            )
            args.append(self.define("CUDAToolkit_ROOT", self.spec["cuda"].prefix))

        if spec.satisfies("+rocm"):
            targets = self.spec.variants["amdgpu_target"].value
            args.append(self.define("KYNEMA_DRIVER_ENABLE_ROCM", True))
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            # Optimization to only build one specific target architecture:
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", ";".join(str(x) for x in targets)))
            args.append(self.define("AMDGPU_TARGETS", ";".join(str(x) for x in targets)))
            args.append(self.define("GPU_TARGETS", ";".join(str(x) for x in targets)))

        if spec.satisfies("^kynema-sgf+hdf5"):
            args.append(self.define("H5Z_ZFP_USE_STATIC_LIBS", True))

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.append_flags("CXXFLAGS", "-DUSE_STK_SIMD_NONE")
        if self.spec.satisfies("+rocm+kynema_sgf_gpu~kynema_ugf_gpu"):
            # Manually turn off device self.defines to solve Kokkos issues in Kynema-UGF headers
            env.append_flags("CXXFLAGS", "-U__HIP_DEVICE_COMPILE__ -DDESUL_HIP_RDC")
        if self.spec.satisfies("+cuda"):
            env.set("OMPI_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
            env.set("MPICH_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
            env.set("MPICXX_CXX", self["kokkos-nvcc-wrapper"].kokkos_cxx)
        if self.spec.satisfies("+rocm"):
            env.set("OMPI_CXX", self.spec["hip"].hipcc)
            env.set("MPICH_CXX", self.spec["hip"].hipcc)
            env.set("MPICXX_CXX", self.spec["hip"].hipcc)
