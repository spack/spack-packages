from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class _2decompFft(CMakePackage):
    """2DECOMP&FFT, 2D pencil decomposition library used by x3d2."""

    homepage = "https://github.com/2decomp-fft/2decomp-fft"
    url = "https://github.com/2decomp-fft/2decomp-fft/archive/refs/tags/v2.0.3.2.tar.gz"

    maintainers = ["kaanolgu", "slaizet", "mathrack", "rfj82982"]

    license("BSD-3-Clause")

    version("2.0.3.2", sha256="58eafc33cb767cbe9764a82eb2d9ec2774c892b9b433dcc60a00b18b871a93ff")

    variant("double", default=True, description="Build with double precision")

    depends_on("fortran", type="build")
    depends_on("cmake@3.21:", type="build")
    depends_on("mpi")
    depends_on("mpich+fortran", when="^[virtuals=mpi] mpich")

    def patch(self):
        # Remove the hardcoded host flags. Then the Spack target flags apply.
        # Upstream (v2.0.3.2):
        # https://github.com/2decomp-fft/2decomp-fft/blob/78e50247d341f19f53b61a5fe062ac63fed354f7/cmake/compilers/D2D_flags_gnu.cmake#L10
        # https://github.com/2decomp-fft/2decomp-fft/blob/78e50247d341f19f53b61a5fe062ac63fed354f7/cmake/compilers/D2D_flags_intel.cmake#L10
        filter_file(" -march=native", "", "cmake/compilers/D2D_flags_gnu.cmake", string=True)
        filter_file(" -xHost", "", "cmake/compilers/D2D_flags_intel.cmake", string=True)

    def cmake_args(self):
        args = [
            self.define("BUILD_TARGET", "mpi"),
            self.define("FFT_Choice", "generic"),
            self.define("BUILD_SHARED_LIBS", False),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define_from_variant("DOUBLE_PRECISION", "double"),
        ]
        if hasattr(self.spec["mpi"], "mpifc"):
            args.append(self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc))
        return args
