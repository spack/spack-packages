# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Specfem3d(AutotoolsPackage, CudaPackage, ROCmPackage):
    """SPECFEM3D Cartesian simulates seismic wave propagation in 3D
    regional or local geological structures."""

    homepage = "https://specfem.org"
    url = "https://github.com/SPECFEM/specfem3d/archive/refs/tags/v4.1.1.tar.gz"
    git = "https://github.com/SPECFEM/specfem3d.git"

    maintainers("CISSSCO")

    license("GPL-3.0-only")

    version("4.1.1", sha256="cc950d76aa5f9deea72a263adbce6c4e77b6500f7c41eef5036f4dc882967e5f")
    version("4.1.0", sha256="c1de1be0776a1302b98c22bd2651bc263c331018292deae12ee778829cf9302d")
    version("4.0.0", sha256="54abcef328393f2248531a62ebc30d9c5a317b7540d191f58a823743a542e5c7")

    variant("mpi", default=True, description="Build parallel version with MPI")
    variant("openmp", default=False, description="Build with OpenMP support")
    variant("double-precision", default=False, description="Treat REAL as double precision")
    variant("hdf5", default=False, description="Enable HDF5 support for file I/O")
    variant("adios2", default=False, description="Enable ADIOS2 support")
    variant("scotch", default=True, description="Enable Scotch support")
    variant("debug", default=False, description="Build with debugging options")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("hdf5+fortran", when="+hdf5")
    depends_on("hdf5+mpi", when="+hdf5+mpi")
    depends_on("adios2+fortran", when="+adios2")
    depends_on("adios2+mpi", when="+adios2+mpi")
    depends_on("scotch", when="+scotch")

    conflicts("+cuda", when="+rocm", msg="CUDA and ROCm GPU backends are mutually exclusive")
    conflicts("+adios2", when="~mpi", msg="ADIOS2 requires MPI")

    build_targets = ("all",)

    def configure_args(self):
        spec = self.spec
        args = []

        if "+mpi" in spec:
            args.append("--with-mpi")
            args.append(f"MPI_INC={spec['mpi'].prefix.include}")
            args.append(f"MPIFC={spec['mpi'].mpifc}")
            args.append(f"MPICC={spec['mpi'].mpicc}")
        else:
            args.append("--without-mpi")

        if "+cuda" in spec:
            cuda_version = spec["cuda"].version[0]
            args.append(f"--with-cuda=cuda{cuda_version}")
            args.append(f"CUDA_LIB={spec['cuda'].libs.directories[0]}")
            args.append(f"CUDA_INC={spec['cuda'].prefix.include}")
            if "+mpi" in spec:
                args.append(f"MPI_INC={spec['mpi'].prefix.include}")

        if "+rocm" in spec:
            args.append("--with-hip")
            args.append(f"HIP_LIB={spec['hip'].libs.directories[0]}")
            args.append(f"HIP_INC={spec['hip'].prefix.include}")

        if "+hdf5" in spec:
            args.append("--with-hdf5")
            args.append(f"HDF5_INC={spec['hdf5:fortran'].prefix.include}")
            args.append(f"HDF5_LIBS={spec['hdf5:fortran'].libs.link_flags}")
        else:
            args.append("--without-hdf5")

        if "+adios2" in spec:
            args.append("--with-adios2")
            args.append(f"ADIOS2_CONFIG={spec['adios2'].prefix.bin.adios2_config}")
        else:
            args.append("--without-adios2")

        if "+scotch" in spec:
            args.append(f"--with-scotch-dir={spec['scotch'].prefix}")

        args.extend(self.enable_or_disable("openmp"))
        args.extend(self.enable_or_disable("double-precision"))
        args.extend(self.enable_or_disable("debug"))

        return args

    def install(self, spec, prefix):
        install_tree(".", prefix)
