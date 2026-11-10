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

    variant("adios2", default=False, description="Enable ADIOS2 I/O")

    # The `CudaPackage` class provides the `cuda` and `cuda_arch` variants.
    # The `omp_tgt` variant only selects the GPU backend.
    variant(
        "omp_tgt",
        default=False,
        description=(
            "Use the OpenMP target offload backend instead of the CUDA backend (needs +cuda)"
        ),
    )

    # AMD GPU support for OMP_TGT is planned. Follow the current development in
    # https://github.com/xcompact3d/x3d2
    conflicts(
        "~cuda",
        when="+omp_tgt",
        msg="x3d2 +omp_tgt needs +cuda and a cuda_arch value, "
        "the recipe supports OMP_TGT on NVIDIA GPUs only (AMD and Intel OMP_TGT are not packaged)",
    )

    with default_args(type="build"):
        depends_on("fortran")
        depends_on("c")
        depends_on("cxx")
        # Upstream needs CMake 3.13. Its documentation recommends CMake 3.20.
        depends_on("cmake@3.20:")
        depends_on("python@3:")

    depends_on("mpi")
    depends_on("mpich+fortran", when="^[virtuals=mpi] mpich")
    # The GPU backends use their own FFT path. Only the CPU build needs 2decomp-fft.
    depends_on("2decomp-fft+double", when="~cuda")

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
        # `setup_build_environment` points NVCOMPILER_*_LIBS_HOME at the NVHPC directories.
        # These directories belong to the CUDA version that the SDK includes.
        # This version is 12.8 for nvhpc@25.3.
        # A newer cuda breaks the MPI configure step.
        depends_on("cuda@12.8", when="%fortran=nvhpc@25.3")

    with when("+adios2"):
        depends_on("adios2@2.12: ~libcatalyst +fortran +mpi")
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
            "OFF"
            if spec.satisfies("~cuda")
            else ("OMP_TGT" if spec.satisfies("+omp_tgt") else "CUDA")
        )
        args = [
            self.define("WITH_MPI", True),
            self.define("MPI_C_COMPILER", spec["mpi"].mpicc),
            self.define("MPI_CXX_COMPILER", spec["mpi"].mpicxx),
            # CMake FindMPI must not read PATH, so pass the Fortran wrapper too.
            self.define("MPI_Fortran_COMPILER", spec["mpi"].mpifc),
            self.define("WITH_2DECOMPFFT", spec.satisfies("~cuda")),
            self.define_from_variant("WITH_ADIOS2", "adios2"),
            self.define("ENABLE_BACKEND", backend),
        ]
        if spec.satisfies("~cuda"):
            args.append(self.define("decomp2d_install_dir", spec["2decomp-fft"].prefix))
        else:
            cuda_arch = spec.variants["cuda_arch"].value
            if len(cuda_arch) != 1:
                raise InstallError("x3d2 accepts exactly one cuda_arch value")
            args.append(self.define("BACKEND_ARCH", "cc" + cuda_arch[0]))
        if spec.satisfies("+adios2"):
            args += [
                self.define("USE_SYSTEM_ADIOS2", True),
                self.define("ADIOS2_ROOT_DIR", spec["adios2"].prefix),
                self.define("WITH_ADIOS2_GPU_AWARE", False),
            ]
        return args

    def install(self, spec, prefix):
        # The CMake project has no install() rules. Copy the binaries.
        install_tree(join_path(self.build_directory, "bin"), prefix.bin)
