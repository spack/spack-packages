# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class GGMLPackageBase(CMakePackage, CudaPackage, ROCmPackage):
    variant("shared", default=True, description="build shared libraries")
    variant("cpu", default=True, description="build CPU backend")
    variant("blas", default=True, description="build BLAS backend")
    variant("openmp", default=True, description="build OpenMP backend")
    variant("cuda", default=False, description="build CUDA backend")
    variant("rocm", default=False, description="build HIP backend")
    variant("metal", default=True, description="build Metal backend", when="platform=darwin")
    variant("rpc", default=False, description="build with RPC support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("git", type="build")

    depends_on("blas", when="+blas")
    depends_on("llvm-openmp", when="platform=darwin %apple-clang")

    depends_on("hipblas", when="+rocm")
    depends_on("rocblas", when="+rocm")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("GGML_CPU", "cpu"),
            self.define_from_variant("GGML_BLAS", "blas"),
            self.define_from_variant("GGML_OPENMP", "openmp"),
            self.define_from_variant("GGML_CUDA", "cuda"),
            self.define_from_variant("GGML_ROCM", "rocm"),
            self.define_from_variant("GGML_METAL", "metal"),
            self.define_from_variant("GGML_RPC", "rpc"),
        ]

        if self.spec.satisfies("+blas"):
            if self.spec.satisfies("%blas=openblas"):
                blas_vendor = "OpenBLAS"
            elif self.spec.satisfies("%blas=intel-oneapi-mkl"):
                blas_vendor = "Intel"
            elif self.spec.satisfies("%blas=veclibfort"):
                blas_vendor = "Apple"
            else:
                blas_vendor = "Generic"
            args.append(self.define("GGML_BLAS_VENDOR", blas_vendor))

        if self.spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_CUDA_COMPILER", f"{self.spec['cuda'].prefix}/bin/nvcc"))
            if not self.spec.satisfies("cuda_arch=none"):
                archs = self.spec.variants["cuda_arch"].value
                arch_str = ";".join(archs)
                args.append(self.define("CMAKE_CUDA_ARCHITECTURES", arch_str))

        if self.spec.satisfies("+rocm"):
            args.append(
                self.define(
                    "CMAKE_HIP_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
            if not self.spec.satisfies("amdgpu_target=none"):
                archs = self.spec.variants["amdgpu_target"].value
                arch_str = ";".join(archs)
                args.append(self.define("CMAKE_HIP_ARCHITECTURES", arch_str))
        return args


class Ggml(GGMLPackageBase):
    """Tensor library for machine learning"""

    homepage = "https://github.com/ggml-org/ggml"
    git = "https://github.com/ggml-org/ggml.git"

    maintainers("rbberger")

    license("MIT")

    version("master", branch="master")
    version("0.9.4", tag="v0.9.4", commit="72632094336524a9c809e129e8b1c52154543a5a")
