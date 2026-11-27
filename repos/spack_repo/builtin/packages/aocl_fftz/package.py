# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclFftz(CMakePackage):
    """AOCL-FFTZ is a high performance Fast Fourier Transform (FFT) library
    developed by AMD supporting advanced optimizations for AMD Zen-based CPUs.

    +wrappers builds FFTW 3.x ABI libraries (libfftw3*) and provides fftw-api;
    that mode conflicts with aocl-fftw / fftw / amdfftw. Prefer aocl-fftw for
    the amd-aocl bundle and most HPC apps. ~wrappers builds the native FFTZ
    API only and may be installed beside aocl-fftw.
    """

    homepage = "https://www.amd.com/en/developer/aocl/fftz.html"
    git = "https://github.com/amd/aocl-fftz.git"
    url = "https://github.com/amd/aocl-fftz/archive/6.0.0.tar.gz"

    maintainers("amd-toolchain-support")

    license("BSD-3-Clause")

    version("6.0.0", sha256="09861bf1973b6b0c477d37e47775745a09a3bd4a4e016109add11a0646ec2914")

    depends_on("cmake@3.26:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant("shared", default=True, description="Build shared libraries")
    variant(
        "openmp", default=True, description="Build OpenMP multithreaded FFTW API (libfftw3*_omp)"
    )
    variant(
        "wrappers",
        default=True,
        description="Build/install FFTW 3.x wrapper libraries and CMake/pkg-config shims",
    )
    variant("aocl_enable_log", default=False, description="Enable AOCL logging")
    variant(
        "aocl_test_coverage",
        default="OFF",
        values=("OFF", "STANDARD", "EXHAUSTIVE"),
        multi=False,
        description="AOCL test coverage level",
    )
    variant("accuracy_with_dft", default=False, description="Accuracy mode with DFT")
    variant("enable_fma", default=True, description="Enable FMA instructions")
    variant("enable_strict_warnings", default=False, description="Treat warnings as errors")

    provides("fftw-api@3", when="+wrappers")

    conflicts(
        "fftw",
        when="+wrappers",
        msg="Use AOCL-FFTZ or FFTW, not both as separate roots/providers",
    )
    conflicts(
        "aocl-fftw",
        when="+wrappers",
        msg="Use AOCL-FFTZ or aocl-fftw, not both as separate roots/providers",
    )
    conflicts(
        "amdfftw",
        when="+wrappers",
        msg="Use AOCL-FFTZ or amdfftw, not both as separate roots/providers",
    )

    def cmake_args(self):
        spec = self.spec
        args = []

        target = spec.target
        if "avx512" in target:
            args.append(self.define("ENABLE_INSTRUCTIONS_UPTO", "AVX512"))
        elif "avx2" in target:
            args.append(self.define("ENABLE_INSTRUCTIONS_UPTO", "AVX256"))
        else:
            args.append(self.define("ENABLE_INSTRUCTIONS_UPTO", "None"))

        args.append(self.define_from_variant("ENABLE_MULTI_THREADING", "openmp"))

        if spec.satisfies("+wrappers"):
            args.append(self.define("BUILD_THIRD_PARTY_WRAPPERS", "ON"))
        else:
            args.append(self.define("BUILD_THIRD_PARTY_WRAPPERS", "OFF"))

        if spec.satisfies("+shared"):
            args.append(self.define("BUILD_STATIC_LIBS", "OFF"))
            args.append(self.define("BUILD_SHARED_LIBS", "ON"))
        else:
            args.append(self.define("BUILD_STATIC_LIBS", "ON"))
            args.append(self.define("BUILD_SHARED_LIBS", "OFF"))

        args.append(self.define_from_variant("AOCL_ENABLE_LOG", "aocl_enable_log"))
        args.append(self.define_from_variant("AOCL_TEST_COVERAGE", "aocl_test_coverage"))
        args.append(self.define_from_variant("ACCURACY_WITH_DFT", "accuracy_with_dft"))
        args.append(self.define_from_variant("ENABLE_FMA", "enable_fma"))
        args.append(self.define_from_variant("ENABLE_STRICT_WARNINGS", "enable_strict_warnings"))

        return args

    @property
    def libs(self):
        spec = self.spec
        names = []
        if spec.satisfies("+wrappers"):
            names.extend(["libfftw3", "libfftw3f"])
            if spec.satisfies("+openmp"):
                names.extend(["libfftw3_omp", "libfftw3f_omp"])
        names.append("libaocl_fftz")
        shared = spec.satisfies("+shared")
        return find_libraries(names, root=self.prefix, shared=shared, recursive=True)
