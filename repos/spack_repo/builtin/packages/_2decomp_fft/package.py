from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class _2decompFft(CMakePackage):
    """2DECOMP&FFT is a Fortran library for 2D pencil decomposition and distributed FFTs."""

    homepage = "https://github.com/2decomp-fft/2decomp-fft"
    url = "https://github.com/2decomp-fft/2decomp-fft/archive/refs/tags/v2.0.3.2.tar.gz"

    maintainers("kaanolgu", "slaizet", "mathrack", "rfj82982")

    license("BSD-3-Clause")

    version("2.0.3.2", sha256="58eafc33cb767cbe9764a82eb2d9ec2774c892b9b433dcc60a00b18b871a93ff")

    variant("double", default=True, description="Build with double precision")

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
            (" -xHost", "cmake/compilers/D2D_flags_intel.cmake"),
        ):
            filter_file(flag, "", file, string=True)

    def cmake_args(self):
        return [
            self.define("BUILD_TARGET", "mpi"),
            self.define("FFT_Choice", "generic"),
            self.define("BUILD_SHARED_LIBS", False),
            self.define_from_variant("DOUBLE_PRECISION", "double"),
            # FindMPI must use the Spack compiler wrapper and not search `PATH`.
            self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc),
        ]
