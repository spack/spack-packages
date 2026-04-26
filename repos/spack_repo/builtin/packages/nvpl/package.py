# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Nvpl(Package):
    """The NVIDIA Performance Libraries (NVPL) are a collection of high
    performance mathematical libraries optimized for the NVIDIA aarch64 CPUs.
    It provides BLAS, LAPACK, FFT, RAND, ScaLAPACK, Sparse and Tensor
    libraries."""

    homepage = "https://docs.nvidia.com/nvpl/latest/"
    url = "https://developer.download.nvidia.com/compute/nvpl/25.11/local_installers/nvpl-linux-sbsa-25.11.tar.gz"

    maintainers("rbberger")

    license("UNKNOWN")

    version("25.11", sha256="2b4588ff0bd5bd7d2db9dc86e03195a2e15521e7fbc7616d4df97d1b2e8c2d65")

    variant("ilp64", default=False, description="Force 64-bit Fortran native integers")
    variant("mpi", default=True, description="Install libraries with MPI support")

    provides("blas")
    provides("lapack")
    provides("fftw-api@3")
    provides("scalapack", when="+mpi")

    variant(
        "threads",
        default="none",
        description="Multithreading support",
        values=("openmp", "none"),
        multi=False,
    )

    depends_on("c", type="build")  # for enforcing compiler restrictions
    depends_on("mpi", when="+mpi")

    requires("target=armv8.2a:", msg="Any CPU with Arm-v8.2a+ microarch")
    requires("platform=linux", msg="Precompiled binary requires Linux")

    conflicts("%gcc@:7")
    conflicts("%clang@:13")

    def url_for_version(self, version):
        return f"https://developer.download.nvidia.com/compute/nvpl/{version}/local_installers/nvpl-linux-sbsa-{version}.tar.gz"

    @property
    def blas_headers(self):
        return find_all_headers(self.spec.prefix.include)

    @property
    def blas_libs(self):
        spec = self.spec

        if "+ilp64" in spec:
            int_type = "ilp64"
        else:
            int_type = "lp64"

        if spec.satisfies("threads=openmp"):
            threading_type = "gomp"
        else:
            # threads=none
            threading_type = "seq"

        name = ["libnvpl_blas_core", f"libnvpl_blas_{int_type}_{threading_type}"]
        return find_libraries(name, spec.prefix.lib, shared=True, recursive=True)

    @property
    def lapack_headers(self):
        return find_all_headers(self.spec.prefix.include)

    @property
    def lapack_libs(self):
        spec = self.spec

        if "+ilp64" in spec:
            int_type = "ilp64"
        else:
            int_type = "lp64"

        if spec.satisfies("threads=openmp"):
            threading_type = "gomp"

        if spec.satisfies("threads=openmp"):
            threading_type = "gomp"
        else:
            # threads=none
            threading_type = "seq"

        name = ["libnvpl_lapack_core", f"libnvpl_lapack_{int_type}_{threading_type}"]
        return find_libraries(name, spec.prefix.lib, shared=True, recursive=True)

    @property
    def headers(self):
        return find_all_headers(self.spec.prefix.include)

    @property
    def libs(self):
        return find_libraries("libnvpl_fftw", self.spec.prefix.lib, shared=True, recursive=True)

    @property
    def scalapack_headers(self):
        return find_all_headers(self.spec.prefix.include)

    @property
    def scalapack_libs(self):
        spec = self.spec

        int_type = "ilp64" if spec.satisfies("+ilp64") else "lp64"

        if any(
            spec.satisfies(f"^[virtuals=mpi] {mpi_library}")
            for mpi_library in ["mpich", "cray-mpich", "mvapich", "mvapich2"]
        ):
            mpi_type = "mpich"
        elif spec.satisfies("^[virtuals=mpi] openmpi"):
            mpi_type = "openmpi" + spec["openmpi"].version.up_to(1)
        else:
            raise InstallError(
                f"Unsupported MPI library {spec['mpi']}.\n"
                "Add support to the Spack package, if needed."
            )

        name = [f"libnvpl_blacs_{int_type}_{mpi_type}", f"libnvpl_scalapack_{int_type}"]

        return find_libraries(name, spec.prefix.lib, shared=True, recursive=True)

    def install(self, spec, prefix):
        install_tree(".", prefix)
