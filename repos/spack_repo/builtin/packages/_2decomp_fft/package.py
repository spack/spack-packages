from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class _2decompFft(CMakePackage, CudaPackage):
    """2DECOMP&FFT is a Fortran library for 2D pencil decomposition and distributed FFTs."""

    homepage = "https://github.com/2decomp-fft/2decomp-fft"
    url = "https://github.com/2decomp-fft/2decomp-fft/archive/refs/tags/v2.0.3.2.tar.gz"

    maintainers("kaanolgu", "slaizet", "mathrack", "rfj82982")

    license("BSD-3-Clause")

    version("2.0.3.2", sha256="58eafc33cb767cbe9764a82eb2d9ec2774c892b9b433dcc60a00b18b871a93ff")

    variant(
        "build_type",
        default="Release",
        description="The build type",
        values=("Release", "Debug", "Dev"),
    )
    variant("shared", default=False, description="Build shared libraries")
    variant("double", default=True, description="Build with double precision")
    variant(
        "single_output",
        default=False,
        when="+double",
        description="Write the output in single precision",
    )
    variant(
        "inplace",
        default=False,
        description="Overwrite the input of the FFT. The generic FFT ignores this option",
    )
    variant("halo_debug", default=False, description="Enable the halo debug checks")
    variant("even", default=False, description="Pad the MPI all-to-all transpose operations")
    variant(
        "fft",
        default="generic",
        values=("generic", "fftw", "fftw_f03", "mkl", "cufft"),
        multi=False,
        description="The FFT library",
    )
    # The `CudaPackage` class provides the `cuda` and `cuda_arch` variants. The `cuda` variant
    # selects the GPU target of the library.
    variant("openacc", default=True, when="+cuda", description="Use OpenACC in the GPU target")
    variant(
        "managed",
        default=False,
        when="+cuda",
        description="Use the automatic GPU memory management of NVHPC",
    )
    variant(
        "nccl",
        default=False,
        when="+cuda",
        description=(
            "Use the NCCL library of NVHPC for the collective communication. "
            "This build fails with 2decomp-fft 2.0.3.2 and nvhpc 25.3 because "
            "`decomp_2d_nccl.f90` does not declare `cudastreamcreate`. This path is not verified"
        ),
    )
    variant("adios2", default=False, description="Use ADIOS2 for the I/O")
    variant("caliper", default=False, description="Enable the Caliper profiler")

    with default_args(type="build"):
        depends_on("fortran")
        depends_on("cmake@3.21:")

        with when("+adios2"):
            depends_on("c")
            depends_on("cxx")

        with when("+caliper"):
            depends_on("c")
            depends_on("cxx")

        # The CMake CUDA language check runs nvcc, and nvcc runs the C++ compiler as the linker.
        depends_on("cxx", when="+cuda")

    with when("+cuda"):
        requires("%fortran=nvhpc", msg="2decomp-fft +cuda needs nvfortran (%fortran=nvhpc)")
        conflicts("cuda_arch=none", msg="2decomp-fft +cuda needs a cuda_arch value")
        conflicts("+even", msg="2decomp-fft +cuda does not support +even")

    requires("+cuda", when="fft=cufft", msg="2decomp-fft fft=cufft needs +cuda")

    depends_on("mpi")
    depends_on("mpich+fortran", when="^[virtuals=mpi] mpich")

    depends_on("intel-oneapi-mkl +envmods", when="fft=mkl")

    for fft in ("fftw", "fftw_f03"):
        with when(f"fft={fft}"):
            # Upstream links the FFTW library that matches the precision of the build.
            depends_on("fftw@3:")
            depends_on("fftw precision=double", when="+double")
            depends_on("fftw precision=float", when="~double")
            # Upstream downloads the FindFFTW module at configure time. Supply a pinned copy.
            resource(
                name="findfftw",
                git="https://github.com/egpbos/findFFTW.git",
                commit="d449ea0bcbf94a4a1c3dbb2108aa57609a4967ff",
                placement="findFFTW",
            )
            patch("fftw-module.patch")

    depends_on("adios2 +mpi +fortran", when="+adios2")
    depends_on("caliper +fortran +mpi", when="+caliper")

    def patch(self):
        # Remove the hardcoded host flags. Then the Spack target flags apply.
        # Upstream (v2.0.3.2) sets the host flags in line 10 of the files
        # `cmake/compilers/D2D_flags_gnu.cmake` and `cmake/compilers/D2D_flags_intel.cmake`.
        for flag, file in (
            (" -march=native", "cmake/compilers/D2D_flags_gnu.cmake"),
            (" -tp=native", "cmake/compilers/D2D_flags_nvidia.cmake"),
            (" -xHost", "cmake/compilers/D2D_flags_intel.cmake"),
        ):
            filter_file(flag, "", file, string=True)

    def setup_build_environment(self, env):
        # The cuda package sets NVHPC_CUDA_HOME for its dependents.
        # Then NVHPC cannot find its own comm_libs and math_libs for that CUDA version.
        # The Fortran compiler does not find `mpif.h`.
        # Point NVCOMPILER_COMM_LIBS_HOME and NVCOMPILER_MATH_LIBS_HOME at these directories.
        if self.spec.satisfies("+cuda"):
            nvhpc = self.spec["nvhpc"]
            cuda_version = self.spec["cuda"].version.up_to(2)
            nvhpc_root = join_path(
                nvhpc.prefix, f"Linux_{nvhpc.target.family}", str(nvhpc.version)
            )
            for lib in ("COMM", "MATH"):
                env.set(
                    f"NVCOMPILER_{lib}_LIBS_HOME",
                    join_path(nvhpc_root, f"{lib.lower()}_libs", str(cuda_version)),
                )

    def cmake_args(self):
        # The test run parameters `PROW`, `PCOL`, `NX`, `NY` and `NZ` keep the upstream defaults.
        spec = self.spec
        if "+cuda" in spec and len(spec.variants["cuda_arch"].value) != 1:
            raise InstallError("2decomp-fft accepts exactly one cuda_arch value")
        mkl_dir = (
            join_path(spec["intel-oneapi-mkl"].package.component_prefix, "lib", "cmake", "mkl")
            if "intel-oneapi-mkl" in spec
            else None
        )
        return [
            self.define("BUILD_TARGET", "gpu" if "+cuda" in spec else "mpi"),
            self.define_from_variant("ENABLE_CUDA", "cuda"),
            self.define_from_variant("ENABLE_OPENACC", "openacc"),
            self.define_from_variant("ENABLE_MANAGED", "managed"),
            self.define_from_variant("ENABLE_NCCL", "nccl"),
            self.define("IO_BACKEND", "adios2" if "+adios2" in self.spec else "mpi"),
            self.define("ENABLE_PROFILER", "caliper" if "+caliper" in self.spec else "OFF"),
            self.define_from_variant("FFT_Choice", "fft"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("DOUBLE_PRECISION", "double"),
            self.define_from_variant("SINGLE_PRECISION_OUTPUT", "single_output"),
            self.define_from_variant("ENABLE_INPLACE", "inplace"),
            self.define_from_variant("HALO_DEBUG", "halo_debug"),
            self.define_from_variant("EVEN", "even"),
            # FindMPI must use the Spack compiler wrapper and not search `PATH`.
            self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc),
            # Upstream detects the GPU of the build host if this option is missing.
            *(
                [self.define("CUDA_ARCH_COMP", spec.variants["cuda_arch"].value[0])]
                if "+cuda" in spec
                else []
            ),
            *([self.define("FFTW_ROOT", spec["fftw"].prefix)] if "fftw" in spec else []),
            *([self.define("MKL_DIR", mkl_dir)] if mkl_dir else []),
        ]
