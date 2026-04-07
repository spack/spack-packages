# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class KokkosFft(CMakePackage):
    """Kokkos-FFT: FFT interfaces for Kokkos C++ Performance Portability Programming EcoSystem"""

    homepage = "https://github.com/kokkos/kokkos-fft"
    url = "https://github.com/kokkos/kokkos-fft/archive/refs/tags/v0.3.0.tar.gz"

    maintainers("cedricchevalier19", "tpadioleau", "yasahi-hpc")

    license("Apache-2.0 WITH LLVM-exception OR MIT", checked_by="cedricchevalier19")

    version("1.0.0", sha256="626c8eec4bd0675a13ccbbffccde0984d8b9ded18809ca8223370b51a0bbfc82")
    version("0.4.0", sha256="c51d37b8c06d74bdb2af0fa4e1eae40104c23ae0dae17c795bce55dbda6ab0d6")
    version("0.3.0", sha256="a13c423775afec5f9f79fa9a23dd6001d3d63bae9f4786b1e0cd3ed65b3993a3")

    variant(
        "host_backend",
        default="fftw-serial",
        values=("fftw-serial", "fftw-openmp"),
        multi=True,
        description="Enable host backend",
    )
    variant(
        "device_backend",
        default="none",
        values=("none", "cufft", "hipfft", "onemkl"),
        multi=False,
        description="Enable device backend",
    )
    variant("tests", default=False, description="Enable tests")

    depends_on("cxx", type="build")
    depends_on("cmake@3.22:3", type="build")

    depends_on("kokkos +complex_align")
    depends_on("kokkos@4.4:4", when="@0.3")
    depends_on("kokkos@4.5:4", when="@0.4")
    depends_on("kokkos@4.6:5", when="@1.0:")
    # Kokkos-FFT currently only supports compilation with the Kokkos nvcc wrapper
    requires("^kokkos +serial", when="host_backend=fftw-serial")
    requires("^kokkos +openmp", when="host_backend=fftw-openmp")
    requires("^kokkos +cuda +wrapper", when="device_backend=cufft")
    requires("^kokkos +rocm", when="device_backend=hipfft")
    requires("^kokkos +sycl", when="device_backend=onemkl")
    depends_on("googletest@1.15:1", when="+tests")

    depends_on("fftw@3.3:3 ~mpi precision=float,double")
    requires("^fftw +openmp", when="host_backend=fftw-openmp")
    depends_on("cuda@11:12", when="device_backend=cufft")
    depends_on("hipfft@5.3:6", when="device_backend=hipfft")
    depends_on("intel-oneapi-mkl@2023:2025", when="device_backend=onemkl")

    def cmake_args(self):
        args = [
            self.define("KokkosFFT_ENABLE_INTERNAL_KOKKOS", False),
            self.define_from_variant("KokkosFFT_ENABLE_TESTS", "tests"),
            self.define("KokkosFFT_ENABLE_DOCS", False),
            self.define("KokkosFFT_ENABLE_BENCHMARK", False),
            self.define("KokkosFFT_ENABLE_EXAMPLES", False),
            self.define(
                "KokkosFFT_ENABLE_FFTW",
                self.spec.satisfies("host_backend=fftw-serial")
                or self.spec.satisfies("host_backend=fftw-openmp"),
            ),
            self.define("KokkosFFT_ENABLE_CUFFT", self.spec.satisfies("device_backend=cufft")),
            self.define("KokkosFFT_ENABLE_HIPFFT", self.spec.satisfies("device_backend=hipfft")),
            self.define("KokkosFFT_ENABLE_ONEMKL", self.spec.satisfies("device_backend=onemkl")),
        ]

        if self.spec.satisfies("^kokkos+rocm") and not (
            self.spec.satisfies("^kokkos %cxx=clang") or self.spec.satisfies("^kokkos %cxx=rocmcc")
        ):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
