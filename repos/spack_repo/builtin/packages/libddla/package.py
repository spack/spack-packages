# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Libddla(CMakePackage, CudaPackage):
    """Distributed dense linear algebra with CPU and optional CUDA backends
    and an MPI-based block-cyclic data distribution."""

    homepage = "https://github.com/userchba/LibDDLA"
    url = "https://github.com/userchba/LibDDLA/archive/refs/tags/v0.0.7.tar.gz"
    git = "https://github.com/userchba/LibDDLA.git"

    license("LGPL-3.0-only")

    version("0.0.7", sha256="8991797705b0854dfcd83f6e2b3b1d68fad1a8f704b6ed2a4450eef2234353c6")

    variant("openmp", default=True, description="Enable OpenMP in the host kernels")

    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")
    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("llvm-openmp", when="+openmp %apple-clang")
    # GPU allocations use cudaMallocAsync/cudaFreeAsync without a fallback.
    depends_on("cuda@11.2:", when="+cuda")

    conflicts("cuda_arch=none", when="+cuda", msg="Select a CUDA architecture for LibDDLA")

    # The public API and calls to BLAS/LAPACK use 32-bit integers.
    conflicts("^openblas +ilp64")
    conflicts("^intel-oneapi-mkl +ilp64")
    conflicts("^blis +ilp64")
    conflicts("^aocl-blas +ilp64")
    conflicts("^amdblis +ilp64")
    conflicts("^aocl-lapack +ilp64")
    conflicts("^amdlibflame +ilp64")
    conflicts("^armpl-gcc +ilp64")
    conflicts("^blis ~cblas")
    conflicts("^aocl-blas ~cblas")
    conflicts("^amdblis ~cblas")

    def setup_build_environment(self, env):
        # Upstream treats OPENBLAS as an override for both library providers.
        env.unset("OPENBLAS")

    def cmake_args(self):
        blas = self.spec["blas:c,fortran"].libs
        # Retain BLAS after LAPACK for providers with separate static archives.
        lapack = self.spec["lapack"].libs + blas
        args = [
            self.define_from_variant("DDLA_USE_CUDA", "cuda"),
            self.define("DDLA_USE_HIP", False),
            self.define("DDLA_USE_CCL", False),
            self.define_from_variant("DDLA_USE_OPENMP", "openmp"),
            self.define("DDLA_ENABLE_FORTRAN", False),
            self.define("DDLA_ENABLE_PYTHON", False),
            self.define("BUILD_TESTS", self.run_tests),
            # Use library lists instead of upstream's single-file overrides.
            self.define("DDLA_CPU_BLAS_LIBRARY", ""),
            self.define("DDLA_LAPACK_LIBRARY", ""),
            # Complex dot products require CBLAS in addition to Fortran BLAS.
            self.define("BLAS_LIBRARIES", blas),
            self.define("LAPACK_LIBRARIES", lapack),
        ]
        if "+cuda" in self.spec:
            cuda = self.spec["cuda"].prefix
            args.extend(
                [
                    self.define("CMAKE_CUDA_COMPILER", cuda.bin.nvcc),
                    self.define("CMAKE_CUDA_HOST_COMPILER", self.spec["cxx"].package.cxx),
                    self.define("CUDAToolkit_ROOT", cuda),
                    self.define("CMAKE_CUDA_ARCHITECTURES", self.spec.variants["cuda_arch"].value),
                ]
            )
        return args
