# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Kynema(CMakePackage, CudaPackage, ROCmPackage):
    """An open-source performance-oriented structural dynamics simulation code."""

    license("MIT License", checked_by="ddement")

    homepage = "https://kynema.github.io/kynema/"
    url = "https://github.com/kynema/kynema.git"
    git = "https://github.com/kynema/kynema.git"

    maintainers("faisal-bhuiyan", "ddement", "deslaughter")

    version("main", branch="main")

    variant("tests", default=False, description="Build Kynema Test Suite")
    variant("openmp", default=False, description="Build Kynema with OpenMP support")
    variant("vtk", default=False, description="Enable VTK")
    variant("adi", default=False, description="Build the OpenFAST ADI external project")
    variant("rosco", default=False, description="Build the ROSCO controller external project")
    variant("klu", default=True, description="Build with support for the KLU sparse direct solver")
    variant(
        "umfpack",
        default=False,
        description="Build with support for the UMFPACK sparse direct solver",
    )
    variant(
        "superlu",
        default=False,
        description="Build with support for the SuperLU sparse direct solver",
    )
    variant(
        "superlu-mt",
        default=False,
        description="Build with support for the SuperLU_MT sparse direct solver",
    )
    variant(
        "mkl",
        default=False,
        description="Build with support for the MKL Pardiso sparse direct solver",
    )
    variant(
        "cusolversp",
        default=True,
        when="+cuda",
        description="Build with support for the cuSolverSP sparse direct solver",
    )
    variant(
        "cudss",
        default=False,
        when="+cuda",
        description="Build with support for the cuDSS sparse direct solver",
    )

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("netcdf-c@4.9:")
    depends_on("yaml-cpp@0.6:")
    depends_on("kokkos-kernels")
    depends_on("lapack")
    depends_on("eigen")

    depends_on("kokkos@4.6:")
    depends_on("kokkos-kernels@4.6:")

    depends_on("kokkos+cuda+wrapper", when="+cuda")
    depends_on("kokkos+rocm", when="+rocm")
    depends_on("kokkos~cuda", when="~cuda")
    depends_on("kokkos~rocm", when="~rocm")

    depends_on("kokkos-kernels+cuda+cublas+cusparse+cusolver", when="+cuda")
    depends_on("kokkos-kernels+rocblas+rocsparse+rocsolver", when="+rocm")
    depends_on("kokkos-kernels+openmp", when="+openmp")
    depends_on("kokkos-kernels~cuda", when="~cuda")
    depends_on("kokkos-kernels~openmp", when="~openmp")

    depends_on("suite-sparse@7.4:", when="+klu")
    depends_on("suite-sparse@7.4:", when="+umfpack")
    depends_on("superlu", when="+superlu")
    depends_on("superlu-mt", when="+superlu-mt")
    depends_on("mkl", when="+mkl")
    depends_on("cudss", when="+cudss")

    depends_on("googletest", when="+tests")
    depends_on("rosco", when="+rosco")
    depends_on("openfast", when="+adi")

    def cmake_args(self):
        options = [
            self.define_from_variant("KYNEMA_FMB_ENABLE_TESTS", "tests"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_OPENFAST_ADI", "adi"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_ROSCO_CONTROLLER", "rosco"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_KLU", "klu"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_UMFPACK", "umfpack"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_SUPERLU", "superlu"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_SUPERLU_MT", "superlu-mt"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_MKL", "mkl"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_CUSOLVERSP", "cusolversp"),
            self.define_from_variant("KYNEMA_FMB_ENABLE_CUDSS", "cudss"),
        ]
        return options
