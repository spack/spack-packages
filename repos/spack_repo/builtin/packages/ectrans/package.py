# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ectrans(CMakePackage):
    """ecTrans is a library for performing efficient and scalable spectral transformations. It is
    used for transforming fields from a grid point space on the sphere (e.g. latitude-longitude) to
    a spectral space based on spherical harmonics (for global transformations) or bifourier
    harmonics (for limited area transformations), which constitutes a direct transform. A
    corresponding inverse transform can also be performed. A transform consists of a Fourier
    transform in the longitudinal direction and either a Legendre transform (global) or another
    Fourier transform (limited area) in the latitudinal direction. ecTrans can also operate on
    fields which are distributed across separate MPI tasks and performs the necessary communication
    to ensure all data needed for a particular transform are resident on a local task."""

    homepage = "https://github.com/ecmwf-ifs/ectrans"
    git = "https://github.com/ecmwf-ifs/ectrans.git"
    url = "https://github.com/ecmwf-ifs/ectrans/archive/1.1.0.tar.gz"

    maintainers("climbfuji", "samhatfield")

    license("Apache-2.0")

    version("develop", branch="develop", no_cache=True)
    version("main", branch="main", no_cache=True)
    version("1.7.0", sha256="224893a8edeaaf76140842340eb30ad4f9ab772591a55aab4e4493a978e086c7")
    version("1.6.2", sha256="63e01a5106fb4eee70a4e544b84300b104507a3fbeb9b7374964c8c48e06acda")
    version("1.5.0", sha256="8b2b24d1988b92dc3793b29142946614fca9e9c70163ee207d2a123494430fde")
    version("1.4.0", sha256="1364827511a2eb11716aaee85062c3ab0e6b5d5dca7a7b9c364e1c43482b8691")
    version("1.2.0", sha256="2ee6dccc8bbfcc23faada1d957d141f24e41bb077c1821a7bc2b812148dd336c")
    version("1.1.0", sha256="3c9848bb65033fbe6d791084ee347b3adf71d5dfe6d3c11385000017b6469a3e")

    variant(
        "build_type",
        default="RelWithDebInfo",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo"),
    )

    variant("mpi", default=True, description="Use MPI")
    variant("openmp", default=True, description="Use OpenMP")

    variant("double_precision", default=True, description="Support for double precision")
    variant("single_precision", default=True, description="Support for single precision")

    variant("mkl", default=False, description="Use MKL")
    variant("fftw", default=True, description="Use FFTW")

    variant(
        "etrans",
        default=False,
        when="@1.6.0:",
        description="Compile limited-area-model transform library etrans",
    )
    variant("transi", default=True, description="Compile TransI C-interface to trans")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # Add explicit dependency on newer cmake versions in order to apply patch
    # "find_lapack.patch", see below and https://github.com/ecmwf-ifs/ectrans/issues/316
    # Newer versions of ectrans (1.7.0+) also require cmake@3.25: by default.
    depends_on("cmake@3.25:", type="build")

    depends_on("ecbuild", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("blas")
    depends_on("lapack")
    # ectrans distinguishes between mkl and fftw
    depends_on("fftw-api", when="+fftw")
    depends_on("mkl", when="+mkl")
    conflicts("+mkl", when="+fftw")

    depends_on("fiat~mpi", when="~mpi")
    depends_on("fiat+mpi", when="+mpi")

    # https://github.com/ecmwf-ifs/ectrans/issues/194
    patch(
        "https://github.com/ecmwf-ifs/ectrans/commit/98f0d505d5b0866cab68a15e86e1a495bafd93d2.patch?full_index=1",
        sha256="17999486a320a5c6a1a442adcdf2c341b49d005f45d09ad0e525594d50bdc39c",
        when="@1.3.1:1.5.1",
    )

    # https://github.com/ecmwf-ifs/ectrans/issues/316
    patch("find_lapack.patch", when="@1.5:")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_MPI", "mpi"),
            self.define_from_variant("ENABLE_OMP", "openmp"),
            self.define_from_variant("ENABLE_DOUBLE_PRECISION", "double_precision"),
            self.define_from_variant("ENABLE_SINGLE_PRECISION", "single_precision"),
            self.define_from_variant("ENABLE_FFTW", "fftw"),
            self.define_from_variant("ENABLE_MKL", "mkl"),
            self.define_from_variant("ENABLE_ETRANS", "etrans"),
            self.define_from_variant("ENABLE_TRANSI", "transi"),
            # Turn off use of contiguous keyword in Fortran because a number
            # of compilers have issues with it, and the hardcoded list of "bad"
            # compilers in ectrans is incomplete and isn't kept up to date
            # https://github.com/JCSDA/spack-stack/issues/1522
            "-DECTRANS_HAVE_CONTIGUOUS_ISSUE=ON",
        ]
        return args
