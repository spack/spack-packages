# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class KokkosFft(CMakePackage):
    """FFT interfaces for Kokkos C++ Performance Portability Programming EcoSystem"""

    homepage = "https://github.com/kokkos/kokkos-fft"
    url = "https://github.com/kokkos/kokkos-fft/archive/refs/tags/v0.3.0.tar.gz"

    maintainers("cedricchevalier19", "tpadioleau", "yasahi-hpc")

    license("Apache-2.0 WITH LLVM-exception OR MIT", checked_by="cedricchevalier19")

    version("0.3.0", sha256="a13c423775afec5f9f79fa9a23dd6001d3d63bae9f4786b1e0cd3ed65b3993a3")

    variant("fftw", default=True, description="Enable FFTW")
    variant("cufft", default=False, description="Enable cufft")
    variant("hipfft", default=False, description="Enable hipfft")
    variant("onemkl", default=False, description="Enable oneMKL fft")
    variant("tests", default=False, description="Enable tests")

    depends_on("kokkos@4.4:4 +complex_align") # not supported in Spack 0.23.1
    requires("^kokkos +wrapper", when="^kokkos +cuda")
    depends_on("googletest@1.15:1", when="+tests")

    depends_on("fftw@3.3:3 ~mpi precision=float,double", when="+fftw")
    requires("^fftw +openmp", when="^kokkos +openmp")
    # requires("^fftw +threads", when="^kokkos +threads") # the option +threads does not exist
    depends_on("cuda@11:12", when="+cufft")
    depends_on("hipfft@5.3:6", when="+hipfft")
    depends_on("intel-oneapi-mkl@2023:2025", when="+onemkl")

    requires("^kokkos +cuda", when="+cufft")
    requires("^kokkos +rocm", when="+hipfft")
    requires("^kokkos +sycl", when="+onemkl")

    def cmake_args(self):
        args = [
            self.define("KokkosFFT_ENABLE_INTERNAL_KOKKOS", False),
            self.define_from_variant("KokkosFFT_ENABLE_TESTS", "tests"),
            self.define_from_variant("KokkosFFT_ENABLE_FFTW", "fftw"),
            self.define_from_variant("KokkosFFT_ENABLE_CUFFT", "cufft"),
            self.define_from_variant("KokkosFFT_ENABLE_HIPFFT", "hipfft"),
            self.define_from_variant("KokkosFFT_ENABLE_ONEMKL", "onemkl"),
            self.define("KokkosFFT_ENABLE_DOCS", False),
            self.define("KokkosFFT_ENABLE_BENCHMARK", False),
            self.define("KokkosFFT_ENABLE_EXAMPLES", False),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["kokkos"].kokkos_cxx))

        return args
