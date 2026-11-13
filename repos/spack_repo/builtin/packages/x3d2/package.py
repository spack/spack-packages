from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class X3d2(CMakePackage, CudaPackage):
    """x3d2, a Xcompact3d successor, CFD solver"""

    homepage = "https://github.com/xcompact3d/x3d2"
    git = "https://github.com/xcompact3d/x3d2.git"

    maintainers("kaanolgu", "slaizet")

    license("BSD-3-Clause")

    # The version is fixed to this commit until the first release.
    version("main", commit="3431b7947143b959d04d2b63c549f1b94b52efa6")

    variant(
        "build_type",
        default="Release",
        description="The build type to build",
        values=("Release", "Debug"),
    )
    variant("mpi", default=True, description="Build with MPI (off gives a single serial rank)")
    variant(
        "double",
        default=True,
        description="Use double precision (off gives single precision, also in 2decomp-fft)",
    )
    variant(
        "decomp2d",
        default=True,
        when="+mpi",
        description="Build the Poisson FFT solver with 2decomp-fft",
    )
    variant("adios2", default=False, description="Enable ADIOS2 I/O")

    # The `CudaPackage` class provides the `cuda` and `cuda_arch` variants.
    # The `omp_tgt` variant only selects the GPU backend.
    variant(
        "omp_tgt",
        default=False,
        description="Use the OpenMP target offload backend instead of the CUDA backend",
    )
    # The OMP_TGT backend on AMD and Intel GPUs is not tested. No build host has these GPUs.
    variant(
        "backend_arch",
        default="none",
        values=str,
        when="+omp_tgt ~cuda",
        description=(
            "GPU architecture of the OMP_TGT backend on AMD and Intel GPUs, for example gfx942, "
            "spir64 or pvc (this path is not tested)"
        ),
    )

    variant(
        "adios2_gpu",
        default=False,
        when="+adios2 +cuda ~omp_tgt",
        description="Pass the GPU memory to ADIOS2 directly (needs ADIOS2 with CUDA)",
    )
    variant(
        "fp_trap",
        default=False,
        when="+cuda ~omp_tgt build_type=Debug",
        description="Trap the floating point exceptions in the CUDA debug build",
    )

    with when("+omp_tgt ~cuda"):
        conflicts(
            "backend_arch=none", msg="x3d2 +omp_tgt needs +cuda cuda_arch=NN or backend_arch"
        )
        conflicts("%fortran=nvhpc", msg="use +cuda cuda_arch=NN with the nvhpc compiler")

    with default_args(type="build"):
        depends_on("fortran")
        depends_on("c")
        depends_on("cxx")
        # Upstream needs CMake 3.13. Its documentation recommends CMake 3.20.
        depends_on("cmake@3.20:")
        depends_on("python@3:")

    depends_on("mpi", when="+mpi")
    depends_on("mpich+fortran", when="+mpi ^[virtuals=mpi] mpich")

    with when("+decomp2d"):
        depends_on("2decomp-fft+double", when="+double")
        depends_on("2decomp-fft~double", when="~double")
        depends_on("2decomp-fft %fortran=nvhpc", when="+cuda")

    with when("+cuda"):
        requires("%fortran=nvhpc", msg="x3d2 +cuda needs nvfortran (%fortran=nvhpc)")
        conflicts("cuda_arch=none", msg="x3d2 +cuda needs a cuda_arch value")
        # `CMakeLists.txt` checks BACKEND_ARCH against `^cc[0-9]+$`.
        # A value with a suffix, such as 90a, fails this check.
        for arch in CudaPackage.cuda_arch_values:
            if not arch.isdigit():
                conflicts(
                    "cuda_arch=" + arch, msg="x3d2 BACKEND_ARCH takes ccNN only, not cc" + arch
                )
            # ADIOS2 must use the same GPU architecture as x3d2.
            depends_on(f"adios2 +cuda cuda_arch={arch}", when=f"+adios2_gpu cuda_arch={arch}")
        # `setup_build_environment` points NVCOMPILER_*_LIBS_HOME at the NVHPC directories.
        # These directories belong to the CUDA version that the SDK includes.
        # This version is 12.8 for nvhpc@25.3.
        # A newer cuda breaks the MPI configure step.
        depends_on("cuda@12.8", when="%fortran=nvhpc@25.3")

    with when("+adios2"):
        depends_on("adios2@2.12: ~libcatalyst +fortran")
        depends_on("adios2 +mpi", when="+mpi")
        depends_on("adios2 ~mpi", when="~mpi")
        # The libmgard that GCC builds links libgomp.
        # In the GPU backends, libgomp clashes with libnvomp
        # (ctest fails with "libgomp: TODO"). Build adios2 with nvhpc and without mgard.
        depends_on("adios2 ~mgard %fortran=nvhpc", when="+cuda")

    def patch(self):
        # Remove the hardcoded host flags. Then the Spack target flags apply.
        # Upstream: https://github.com/xcompact3d/x3d2/blob/3431b7947143b959d04d2b63c549f1b94b52efa6/src/CMakeLists.txt#L183-L199
        for flag in (" -march=native", " -xHost"):
            filter_file(flag, "", "src/CMakeLists.txt", string=True)

    def setup_build_environment(self, env):
        # The cuda package sets NVHPC_CUDA_HOME for its dependents.
        # Then NVHPC cannot find its own comm_libs and math_libs for that CUDA version.
        # The mpicc compiler refuses to run and -lcublas is missing.
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
        spec = self.spec
        backend = (
            "OMP_TGT"
            if spec.satisfies("+omp_tgt")
            else "CUDA"
            if spec.satisfies("+cuda")
            else "OFF"
        )
        args = [
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define("SINGLE_PREC", spec.satisfies("~double")),
            self.define("WITH_2DECOMPFFT", spec.satisfies("+decomp2d")),
            self.define_from_variant("WITH_ADIOS2", "adios2"),
            self.define_from_variant("WITH_ADIOS2_GPU_AWARE", "adios2_gpu"),
            self.define_from_variant("CUDA_DEBUG_FP_TRAP", "fp_trap"),
            self.define("ENABLE_BACKEND", backend),
        ]
        if spec.satisfies("+mpi"):
            args += [
                self.define("MPI_C_COMPILER", spec["mpi"].mpicc),
                self.define("MPI_CXX_COMPILER", spec["mpi"].mpicxx),
                # CMake FindMPI must not read PATH, so pass the Fortran wrapper too.
                self.define("MPI_Fortran_COMPILER", spec["mpi"].mpifc),
            ]
        if spec.satisfies("+decomp2d"):
            args.append(self.define("decomp2d_install_dir", spec["2decomp-fft"].prefix))
        if spec.satisfies("+omp_tgt ~cuda"):
            args.append(self.define_from_variant("BACKEND_ARCH", "backend_arch"))
        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            if len(cuda_arch) != 1:
                raise InstallError("x3d2 accepts exactly one cuda_arch value")
            args += [
                self.define("BACKEND_ARCH", "cc" + cuda_arch[0]),
                self.define("BACKEND_CUDA_VERSION", str(spec["cuda"].version.up_to(2))),
            ]
        if spec.satisfies("+adios2"):
            # Spack does not fetch ADIOS2, so the build always uses the Spack installation.
            args += [
                self.define("USE_SYSTEM_ADIOS2", True),
                self.define("ADIOS2_ROOT_DIR", spec["adios2"].prefix),
                # The tests of the GPU ADIOS2 path need to know that ADIOS2 has CUDA.
                self.define("ADIOS2_WITH_CUDA", spec.satisfies("^adios2 +cuda")),
            ]
        # These options stay at the upstream defaults. They only set test runs:
        # WITH_NIGHTLY_REGRESSION, CMAKE_CTEST_NPROCS, CMAKE_CTEST_ARGUMENTS and
        # FLANG_OPENMP_RUNTIME_DIR.
        return args

    def install(self, spec, prefix):
        # The CMake project has no install() rules. Copy the binaries.
        install_tree(join_path(self.build_directory, "bin"), prefix.bin)
