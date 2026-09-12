# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Finufft(CMakePackage, CudaPackage):
    """Flatiron Institute Nonuniform Fast Fourier Transform library.

    FINUFFT computes the three standard types of nonuniform FFT to a
    user-specified tolerance, in one, two or three dimensions, on a
    multi-core shared-memory machine. The optional GPU library cuFINUFFT
    provides the same transforms on NVIDIA hardware."""

    homepage = "https://finufft.readthedocs.io"
    url = "https://github.com/flatironinstitute/finufft/archive/refs/tags/v2.5.1.tar.gz"
    git = "https://github.com/flatironinstitute/finufft.git"

    maintainers("hmenke")

    license("Apache-2.0", checked_by="hmenke")

    version("2.5.1", sha256="809aa60ea4bf11a9976642d30d6bd2634da0083bdebd580d64705bc4aecfcd0e")

    # Sources that upstream fetches with CPM at configure time, pinned per
    # FINUFFT release in CMakeLists.txt and cmake/setup*.cmake.
    cpm_versions = {"2.5.1": "0.42.0"}
    cpm_checksums = {"0.42.0": "2020b4fc42dba44817983e06342e682ecfc3d2f484a581f11cc5731fbe4dce8a"}

    findfftw_commits = {"2.5.1": "d449ea0bcbf94a4a1c3dbb2108aa57609a4967ff"}
    findfftw_checksums = {
        "d449ea0bcbf94a4a1c3dbb2108aa57609a4967ff": (
            "48336c41c30c6795324a4af98f64b782b4d9d356a23a90dec45c24b90a4b3fb1"
        )
    }

    ducc0_versions = {"2.5.1": "ducc0_0_39_1"}
    ducc0_checksums = {
        "ducc0_0_39_1": "a01ff2fe1d8324e4248cf0c0ae65882afd983e3973c2d7180014a21d22da98e3"
    }

    cpm_cache_dir = "spack-cpm-cache"

    variant("openmp", default=True, description="Build with OpenMP multi-threading")
    variant("shared", default=True, description="Build shared libraries")
    variant("fortran", default=False, description="Build the Fortran interface and examples")
    variant(
        "fft",
        default="fftw",
        values=("fftw", "ducc"),
        multi=False,
        description="FFT backend of the CPU library",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.24:", type="build")

    # xsimd 13 and earlier fail to compile the SIMD spreader, because
    # get_padding is not constexpr there.
    depends_on("xsimd@14:")

    with when("fft=fftw"):
        depends_on("fftw@3.3.6: precision=float,double")
        depends_on("fftw+openmp", when="+openmp")

    with when("+cuda"):
        depends_on("cuda@11:")
        depends_on("cccl")
        conflicts("cuda_arch=none", msg="Building cuFINUFFT requires setting cuda_arch")

    for _finufft_version, _cpm_version in cpm_versions.items():
        resource(
            name="cpm-cmake",
            url="https://github.com/cpm-cmake/CPM.cmake/releases/download/v{0}/CPM.cmake".format(
                _cpm_version
            ),
            sha256=cpm_checksums[_cpm_version],
            expand=False,
            destination=join_path(cpm_cache_dir, "cpm"),
            # cmake/setupCPM.cmake looks the file up under its version.
            placement={"CPM.cmake": "CPM_{0}.cmake".format(_cpm_version)},
            when="@{0}".format(_finufft_version),
        )

    for _finufft_version, _findfftw_commit in findfftw_commits.items():
        resource(
            name="findfftw",
            url="https://github.com/egpbos/findFFTW/archive/{0}.tar.gz".format(_findfftw_commit),
            sha256=findfftw_checksums[_findfftw_commit],
            placement="findfftw",
            when="@{0} fft=fftw".format(_finufft_version),
        )

    for _finufft_version, _ducc0_version in ducc0_versions.items():
        resource(
            name="ducc0",
            url="https://github.com/mreineck/ducc/archive/refs/tags/{0}.tar.gz".format(
                _ducc0_version
            ),
            sha256=ducc0_checksums[_ducc0_version],
            placement="ducc0",
            when="@{0} fft=ducc".format(_finufft_version),
        )

    del _finufft_version, _cpm_version, _findfftw_commit, _ducc0_version

    def cmake_args(self):
        spec = self.spec
        source = self.stage.source_path

        args = [
            self.define("FINUFFT_USE_CPU", True),
            self.define_from_variant("FINUFFT_USE_CUDA", "cuda"),
            self.define_from_variant("FINUFFT_USE_OPENMP", "openmp"),
            self.define_from_variant("FINUFFT_BUILD_FORTRAN", "fortran"),
            self.define("FINUFFT_STATIC_LINKING", spec.satisfies("~shared")),
            self.define("FINUFFT_POSITION_INDEPENDENT_CODE", True),
            self.define("FINUFFT_USE_DUCC0", spec.satisfies("fft=ducc")),
            self.define("FINUFFT_BUILD_TESTS", self.run_tests),
            self.define("FINUFFT_BUILD_EXAMPLES", False),
            self.define("FINUFFT_BUILD_DOCS", False),
            self.define("FINUFFT_BUILD_MATLAB", False),
            self.define("FINUFFT_BUILD_PYTHON", False),
            # Upstream defaults to -march=native.
            self.define("FINUFFT_ARCH_FLAGS", ""),
            self.define("CPM_DOWNLOAD_VERSION", self.cpm_versions[str(spec.version)]),
            self.define("CPM_SOURCE_CACHE", join_path(source, self.cpm_cache_dir)),
            self.define("CPM_USE_LOCAL_PACKAGES", True),
            # CPM derives the version it passes to find_package() from GIT_TAG,
            # where upstream pins unversioned commits. Advertise the version
            # Spack provides, so the installed package is accepted.
            self.define("XSIMD_VERSION", spec["xsimd"].version),
        ]

        if spec.satisfies("fft=ducc"):
            args.append(self.define("CPM_ducc0_SOURCE", join_path(source, "ducc0")))
        else:
            args += [
                self.define("CPM_findfftw_SOURCE", join_path(source, "findfftw")),
                self.define("FFTW_ROOT", spec["fftw"].prefix),
            ]

        if spec.satisfies("+cuda"):
            cccl_version = spec["cccl"].version
            args += [
                self.define("CUDA11_CCCL_VERSION", cccl_version),
                self.define("CUDA12_CCCL_VERSION", cccl_version),
                self.define("CMAKE_CUDA_ARCHITECTURES", spec.variants["cuda_arch"].value),
            ]

        return args
