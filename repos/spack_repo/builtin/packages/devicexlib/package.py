# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack.package import *


class Devicexlib(AutotoolsPackage, CudaPackage, ROCmPackage):
    """Library wrapping device-oriented routines and utilities.

    deviceXlib provides wrappers for device data allocation and host-device data
    transfers. It supports CUDA, OpenACC, and OpenMP programming paradigms, and
    wraps a subset of routines from NVIDIA cuBLAS, Intel oneMKL BLAS, and AMD
    rocBLAS libraries.
    """

    homepage = "https://gitlab.com/max-centre/components/devicexlib"
    url = "https://gitlab.com/max-centre/components/devicexlib/-/archive/0.9.0/devicexlib-0.9.0.tar.gz"
    git = "https://gitlab.com/max-centre/components/devicexlib"

    maintainers = ["nicspalla"]

    version('develop', branch='develop')

    version("0.9.1", sha256="900fe8b0849d451e7c541d00a1b92c723e0969bae47ebcabd295e14ebcc17d1e")
    version("0.9.0", sha256="77c57a31381a69a2eb2a77138b131a553c96aff03ca934c88b8a6d8434b39460")
    version("0.8.6", sha256="36e6222bc59cf0ed7268cc3652a3661887109f7fe072cefe06884dcd6de2407d")
    version("0.8.5", sha256="498d5c6804e697123d382d9dd35dedeb4b64228704f84711877c842b851d37df")
    version("0.8.4", sha256="6c50bb6d51a26429f17c9bbb00e81b279ed7f731b2a73f4689b7b30a8e30f115")
    version("0.8.3", sha256="3d2d4264df8c57da2791b0f94def52d789d67c6fe7ad5960f96c96dfc6c25cb2")
    version("0.8.2", sha256="c184de73f424e9437e352eb0e35716514348a7cd88ebac3ad7a52c66c4e4ba9c")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    variant("openmp", default=False, description="Enable OpenMP support")

    variant(
        "openmp5",
        default=False,
        description="Build with OpenMP-GPU support",
    )

    variant(
        "openacc",
        default=False,
        description="Build with OpenACC",
    )

    variant(
        "cuda-fortran",
        default=False,
        description="Build with CUDA Fortran",
    )

    variant(
        "nvtx",
        default=False,
        description="Enable NVTX support",
        when="+cuda",
    )

    variant(
        "roctx",
        default=False,
        description="Enable ROCTX support",
        when="+rocm",
    )

    variant(
        "mkl",
        default=False,
        description="Enable MKL-GPU support",
    )

    with when("@0.9.0: +openacc"):
        variant(
            "openacc-debug",
            default=False,
            description="Enable OpenACC DEBUG macro",
        )

    with when("+cuda"):
        variant(
            "cuda_rt",
            values=str,
            default="none",
            when="%nvhpc",
            description=(
                'Specify the CUDA runtime version, e.g. "11.8", only if you '
                "want the secondary version installed with the NVHPC SDK."
            ),
        )

    with when("+cuda-fortran"):
        requires(
            "%nvhpc",
            msg="CUDA Fortran is available only with NVIDIA compilers",
        )

    with when("+openacc"):
        requires(
            "%nvhpc",
            "%gcc@10:+nvptx",
            policy="one_of",
            msg="OpenACC is available only with NVIDIA or GCC compilers",
        )

    with when("+openmp5"):
        requires(
            "%oneapi",
            "%cce",
            "%gcc@10:+nvptx",
            policy="one_of",
            msg=(
                "OpenMP offloading is available only with GCC, oneAPI, "
                "or Cray compilers"
            ),
        )

    depends_on("blas")

    depends_on("intel-oneapi-mkl", when="+mkl")

    with when("+openmp"):
        depends_on("openblas threads=openmp", when="^[virtuals=blas] openblas")

    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="CUDA architecture is required",
    )

    conflicts(
        "cuda_arch=none",
        when="+cuda-fortran",
        msg="CUDA architecture is required",
    )

    conflicts(
        "cuda_rt=none",
        when="@:0.8.5 +cuda",
        msg="CUDA runtime version is required",
    )

    def enable_or_disable_openmp(self, activated):
        return "--enable-openmp" if activated else "--disable-openmp"

    def enable_or_disable_cuda(self, activated):
        return "--enable-cublas=yes" if activated else "--enable-cublas=no"

    def enable_or_disable_rocm(self, activated):
        return "--enable-rocblas=yes" if activated else "--enable-rocblas=no"

    def enable_or_disable_mkl(self, activated):
        return "--enable-mkl-gpu=yes" if activated else "--enable-mkl-gpu=no"

    def setup_build_environment(self, env):
        spec = self.spec

        if "%nvhpc" in spec:
            env.set("CC", "nvc")
            env.set("FC", "nvfortran")
            env.set("F90", "nvfortran")
            env.set("CPP", "cpp -E")
            env.set("FPP", "nvfortran -Mpreprocess -E")
            env.set("F90SUFFIX", ".f90")

        if "%gcc" in spec:
            env.set("CC", "gcc")
            env.set("FC", "gfortran")
            env.set("F90", "gfortran")
            env.set("CPP", "gcc -E -P")
            env.set("FPP", "gfortran -E -P")
            env.set("F90SUFFIX", ".f90")

    def configure_args(self):
        spec = self.spec

        args = [
            "--enable-cuda-env-check=no",
            "--enable-parallel=no",
        ]

        # OpenMP
        args.extend(self.enable_or_disable("openmp"))

        # GPU offloading
        if "+cuda-fortran" in spec:
            args.append("--enable-cuda-fortran")

        if "+openacc" in spec:
            args.append("--enable-openacc")

        if "+openacc-debug" in spec:
            args.append("--enable-openacc-debug")

        if "+openmp5" in spec:
            args.append("--enable-openmp5")

        # BLAS
        if "^nvhpc+blas" in spec:
            args.append("--with-blas-libs=-lblas")
        else:
            args.append(f"--with-blas-libs={spec['blas'].libs}")

        # CUDA
        args.extend(self.enable_or_disable("cuda"))

        if "+cuda" in spec:
            cuda_arch = spec.variants["cuda_arch"].value[0]
            args.append(f"--with-cuda-cc={cuda_arch}")

            if spec.variants["cuda_rt"].value != "none":
                args.append(
                    f"--with-cuda-runtime={spec.variants['cuda_rt'].value}"
                )

            if "%nvhpc" not in spec:
                args.append(f"--with-cuda-path={spec['cuda'].home}")

        # ROCm
        args.extend(self.enable_or_disable("rocm"))

        if "+rocm" in spec:
            args.append(f"--with-rocm-path={spec['hip'].home}")

        # MKL
        args.extend(self.enable_or_disable("mkl"))

        return args

    @property
    def build_targets(self):
        return ["all"]
