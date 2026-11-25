# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libddla(CMakePackage):
    """Distributed dense linear algebra with a CPU backend and an MPI-based
    block-cyclic data distribution."""

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
        return [
            self.define("DDLA_USE_CUDA", False),
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
