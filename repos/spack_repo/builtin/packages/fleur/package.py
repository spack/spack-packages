# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Fleur(CMakePackage):
    """FLEUR (Full-potential Linearised augmented plane wave in EURope)
    is a code family for calculating groundstate as well as excited-state properties
    of solids within the context of density functional theory (DFT)."""

    homepage = "https://www.flapw.de/MaX-5.1"
    git = "https://iffgit.fz-juelich.de/fleur/fleur.git"

    license("MIT")

    version("develop", branch="develop")
    version("8.1", tag="MaX-R8.1", commit="6dc78fc1e5b4b6ec93155a860ca57a0ffa71d503")
    version("7.2", tag="MaX-R7.2", commit="447eed3b7ec3de5fcdfbd232cd1eda4caefb51d3")
    version("5.1", tag="MaX-R5.1", commit="a482abd9511b16412c2222e2ac1b1a303acd454b")
    version("5.0", tag="MaX-R5", commit="f2df362c3dad6ef39938807ea14e4ec4cb677723")
    version("4.0", tag="MaX-R4", commit="ea0db7877451e6240124e960c5546318c9ab3953")
    version("3.1", tag="MaX-R3.1", commit="f6288a0699604ad9e11efbfcde824b96db429404")

    variant("mpi", default=True, description="Enable MPI support")
    variant("hdf5", default=False, description="Enable HDF5 support")
    variant("scalapack", default=False, description="Enable SCALAPACK")
    variant(
        "fft",
        default="internal",
        values=("internal", "mkl", "fftw"),
        description="Enable the use of Intel MKL FFT/FFTW provider",
    )
    variant("elpa", default=False, description="Enable ELPA support")
    variant("magma", default=False, description="Enable Magma support")
    variant("external_libxc", default=False, description="Enable external libxc support")
    variant("spfft", default=False, description="Enable spfft support")
    variant("wannier90", default=False, description="Enable wannier90 support")
    variant("openmp", default=False, description="Enable OpenMP support.")
    # FLEUR only ships compiler flags for Release and Debug builds.
    variant(
        "build_type",
        default="Release",
        description="CMake build type",
        values=("Release", "Debug"),
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.12:", type="build")
    depends_on("python@3:", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("libxml2")
    depends_on("mpi", when="+mpi")
    depends_on("intel-oneapi-mkl", when="fft=mkl")
    depends_on("fftw-api", when="fft=fftw")
    depends_on("scalapack", when="+scalapack")
    depends_on("libxc+fortran", when="+external_libxc")
    depends_on("hdf5+fortran+mpi", when="+hdf5+mpi")
    depends_on("hdf5+fortran~mpi", when="+hdf5~mpi")
    depends_on("magma+fortran", when="+magma")
    depends_on("wannier90", when="+wannier90")
    depends_on("spfft+fortran~openmp", when="+spfft~openmp")
    depends_on("spfft+fortran+openmp", when="+spfft+openmp")
    depends_on("elpa~openmp", when="+elpa~openmp")
    depends_on("elpa+openmp", when="+elpa+openmp")

    conflicts("%intel@:16.0.4", msg="ifort version <16.0 will most probably not work correctly")
    conflicts("%gcc@:6.3.0", msg="gfortran is known to work with versions newer than v6.3")
    conflicts("~scalapack", when="+elpa", msg="ELPA requires scalapack support")
    conflicts("@:5.0", when="fft=fftw", msg="FFTW interface is supported from Fleur v5.0")
    conflicts("@:5.0", when="+wannier90", msg="wannier90 is supported from Fleur v5.0")
    conflicts("@:4.0", when="+spfft", msg="SpFFT is supported from Fleur v4.0")
    conflicts("@:4.0", when="+external_libxc", msg="External libxc is supported from Fleur v4.0")

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define_from_variant("CLI_FLEUR_USE_MPI", "mpi"),
            self.define_from_variant("CLI_FLEUR_USE_HDF5", "hdf5"),
            self.define_from_variant("CLI_FLEUR_USE_SCALAPACK", "scalapack"),
            self.define_from_variant("CLI_FLEUR_USE_WANNIER", "wannier90"),
            self.define_from_variant("CLI_FLEUR_USE_LIBXC", "external_libxc"),
            self.define_from_variant("CLI_FLEUR_USE_MAGMA", "magma"),
        ]
        if spec.satisfies("+elpa"):
            args.append(self.define("CLI_FLEUR_USE_ELPA", "external"))
        if spec.satisfies("+mpi"):
            args += [
                self.define("CMAKE_C_COMPILER", spec["mpi"].mpicc),
                self.define("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx),
                self.define("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc),
            ]
        return args
