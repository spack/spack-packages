# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Ddc(CMakePackage):
    """DDC is the discrete domain computation library."""

    homepage = "https://github.com/CExA-project/ddc"
    git = "https://github.com/CExA-project/ddc.git"
    url = "https://github.com/CExA-project/ddc/archive/refs/tags/v0.7.0.tar.gz"

    maintainers("tpadioleau", "tretre91")

    license("MIT", checked_by="tpadioleau")

    version("main", branch="main", no_cache=True)
    version("0.15.0", sha256="1bcb7eda695e7e37bb37dd7ea40adcb614c2cfe71b2890201424b05c48fce331")
    version("0.14.0", sha256="8c239cea877cf52c3334de6d5c5d248eac85e6df27b9476047fd7ff3f78b85b5")
    version("0.13.0", sha256="6b93a532896d9f5342b477a2bcf85f05d242c8d7b0331580a62e50a9bf155bad")
    version("0.12.0", sha256="30a464b00d712ce7264835cc162b63797185667fea3f4c9457d7dfff0a2bc0cc")
    version("0.11.0", sha256="c3ee616cc6cbbf417dade247cd49805b1a5422b4ac3539cb954f608b8ea27cf4")
    version("0.10.0", sha256="0ab717a21c641b59af8119ff665c0322498fcccf5f49b2c3a2746eecbf1a4964")
    version("0.9.0", sha256="e975a19f2d8e4fc668ab7628e145b927987812496c94b384ee9e72d054711078")
    version("0.8.0", sha256="6c6d28f1d406e1417021f88d748829cae0afce2cb3714cf82fd3f4cd3b7b91b4")
    version("0.7.0", sha256="128dd93d0021da35dcd62db7eabab3136c826a924dbe90368361d347e6bd3111")

    variant("fft", default=True, description="Build DDC kernels for FFT")
    variant("pdi", default=True, description="Build DDC PDI wrapper")
    variant("splines", default=True, description="Build DDC kernels for splines")
    variant("deprecated_code", default=True, description="Build deprecated code")
    variant(
        "double_precision",
        default=True,
        description="Use double precision floating point numbers instead of single precision",
    )
    variant("tests", default=False, description="Build the tests")

    depends_on("cxx", type="build")

    depends_on("cmake@3.25:", type="build", when="@0.9:")
    depends_on("cmake@3.22:", type="build")
    depends_on("cmake@:4", type="build")
    depends_on("cmake@:3", type="build", when="@:0.8")

    depends_on("kokkos@4.4.1:")
    depends_on("kokkos@:5")
    depends_on("kokkos@:4", when="@:0.8")

    with when("+fft"):
        depends_on("kokkos-fft@0.3:")
        depends_on("kokkos-fft@:1")
        depends_on("kokkos-fft@:0", when="@:0.10")
        depends_on("kokkos-fft host_backend=fftw-serial", when="^kokkos ~openmp")
        depends_on("kokkos-fft host_backend=fftw-openmp", when="^kokkos +openmp")
        depends_on("kokkos-fft device_backend=cufft", when="^kokkos +cuda")
        depends_on("kokkos-fft device_backend=hipfft", when="^kokkos +rocm")
        depends_on("kokkos-fft device_backend=onemkl", when="^kokkos +sycl")

    with when("+splines"):
        depends_on("ginkgo@1.8:")
        depends_on("ginkgo@:1")
        depends_on("kokkos-kernels@4.7:", when="@0.12:")
        depends_on("kokkos-kernels@4.5.1:")
        depends_on("kokkos-kernels@:5")
        depends_on("kokkos-kernels@:4", when="@:0.8")
        depends_on("lapack")

        for arch in CudaPackage.cuda_arch_values:
            with when(f"^kokkos +cuda cuda_arch={arch}"):
                depends_on(f"ginkgo +cuda cuda_arch={arch}")
                depends_on(f"kokkos-kernels +cuda cuda_arch={arch}")

        for target in ROCmPackage.amdgpu_targets:
            depends_on(
                f"ginkgo +rocm amdgpu_target={target}",
                when=f"^kokkos +rocm amdgpu_target={target}",
            )

        depends_on("ginkgo +sycl", when="^kokkos +sycl")
        depends_on("ginkgo +openmp", when="^kokkos +openmp")

    with when("+pdi"):
        depends_on("pdi@1.10.1:", when="@0.11:")
        depends_on("pdi@1.6:")
        depends_on("pdi@:1")

    with when("+tests"):
        depends_on("googletest@1.14: +gmock")
        depends_on("googletest@:1 +gmock")
        depends_on("pdiplugin-user-code@1.6:", type=("build", "test"), when="+pdi")
        depends_on("pdiplugin-user-code@:1", type=("build", "test"), when="+pdi")
        depends_on("py-numpy@1.24:", when="@0.15:")
        depends_on("py-numpy@:2", when="@0.15:")
        depends_on("py-pytest@8.4:", when="@0.15:")
        depends_on("py-pytest@:9", when="@0.15:")

    conflicts("^kokkos@4.5.0", msg="Incompatible with the embedded mdspan of Kokkos")

    requires(
        "^kokkos +cuda_constexpr",
        when="^kokkos +cuda",
        msg="DDC relies on the constexpr support of nvcc",
    )
    requires(
        "^kokkos +cuda_relocatable_device_code",
        when="^kokkos +cuda",
        msg="DDC relies on relocatable device code",
    )
    requires(
        "^kokkos +hip_relocatable_device_code",
        when="^kokkos +rocm",
        msg="DDC relies on relocatable device code",
    )
    requires(
        "^kokkos +sycl_relocatable_device_code",
        when="^kokkos +sycl",
        msg="DDC relies on relocatable device code",
    )

    def cmake_args(self):
        args = [
            self.define("DDC_BUILD_EXAMPLES", False),
            self.define("DDC_BUILD_DOCUMENTATION", False),
            self.define("DDC_Kokkos_DEPENDENCY_POLICY", "INSTALLED"),
            self.define_from_variant("DDC_BUILD_TESTS", "tests"),
            self.define_from_variant("DDC_BUILD_KERNELS_FFT", "fft"),
            self.define_from_variant("DDC_BUILD_KERNELS_SPLINES", "splines"),
            self.define_from_variant("DDC_BUILD_PDI_WRAPPER", "pdi"),
            self.define_from_variant("DDC_BUILD_DEPRECATED_CODE", "deprecated_code"),
            self.define_from_variant("DDC_BUILD_DOUBLE_PRECISION", "double_precision"),
        ]

        if self.spec.satisfies("+fft"):
            args.append(self.define("DDC_KokkosFFT_DEPENDENCY_POLICY", "INSTALLED"))

        if self.spec.satisfies("+splines"):
            args.append(self.define("DDC_KokkosKernels_DEPENDENCY_POLICY", "INSTALLED"))

            lapack_provider = self.spec["lapack"]
            if lapack_provider.name == "cray-libsci":
                lapack_include_directories = ""
                for directory in lapack_provider.headers.directories:
                    lapack_include_directories += f" -isystem {directory}"
                args.extend(
                    [
                        self.define("BLA_PREFER_PKGCONFIG", True),
                        self.define("BLA_PKGCONFIG_BLAS", "libsci"),
                        self.define("BLA_PKGCONFIG_LAPACK", "libsci"),
                        self.define("CMAKE_CXX_FLAGS", lapack_include_directories.strip()),
                    ]
                )

        if self.spec.satisfies("+tests"):
            args.append(self.define("DDC_GTest_DEPENDENCY_POLICY", "INSTALLED"))

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
