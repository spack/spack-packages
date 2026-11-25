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
    url = "https://github.com/userchba/LibDDLA/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/userchba/LibDDLA.git"

    license("LGPL-3.0-only")

    version("0.0.7", sha256="8991797705b0854dfcd83f6e2b3b1d68fad1a8f704b6ed2a4450eef2234353c6")

    depends_on("cxx", type="build")
    depends_on("cmake@3.18:", type="build")
    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    # GPU allocations use cudaMallocAsync/cudaFreeAsync without a fallback.
    depends_on("cuda@11.2:", when="+cuda")

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
        args = [
            self.define_from_variant("DDLA_USE_CUDA", "cuda"),
            self.define("BUILD_TESTS", self.run_tests),
            # Complex dot products require CBLAS in addition to Fortran BLAS.
            self.define("BLAS_LIBRARIES", blas),
            # Retain BLAS after LAPACK for providers with separate static archives.
            self.define("LAPACK_LIBRARIES", self.spec["lapack"].libs + blas),
        ]
        if "+cuda" in self.spec:
            args.append(self.define("CMAKE_CUDA_COMPILER", self.spec["cuda"].prefix.bin.nvcc))
            if "cuda_arch=none" not in self.spec:
                args.append(self.define_from_variant("CMAKE_CUDA_ARCHITECTURES", "cuda_arch"))
        return args
