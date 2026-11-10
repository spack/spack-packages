from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class _2decompFft(CMakePackage):
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

    with default_args(type="build"):
        depends_on("fortran")
        depends_on("cmake@3.21:")

    depends_on("mpi")
    depends_on("mpich+fortran", when="^[virtuals=mpi] mpich")

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

    def cmake_args(self):
        # The test run parameters `PROW`, `PCOL`, `NX`, `NY` and `NZ` keep the upstream defaults.
        return [
            self.define("BUILD_TARGET", "mpi"),
            self.define("FFT_Choice", "generic"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("DOUBLE_PRECISION", "double"),
            self.define_from_variant("SINGLE_PRECISION_OUTPUT", "single_output"),
            self.define_from_variant("ENABLE_INPLACE", "inplace"),
            self.define_from_variant("HALO_DEBUG", "halo_debug"),
            self.define_from_variant("EVEN", "even"),
            # FindMPI must use the Spack compiler wrapper and not search `PATH`.
            self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc),
        ]
