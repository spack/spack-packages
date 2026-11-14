# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Specfem2d(AutotoolsPackage, CudaPackage):
    """SPECFEM2D simulates 2D and 2.5D seismic wave propagation in
    complex media using the spectral-element method (SEM)."""

    homepage = "https://specfem.org"
    url = "https://github.com/SPECFEM/specfem2d/archive/refs/tags/v8.1.0.tar.gz"
    git = "https://github.com/SPECFEM/specfem2d.git"

    maintainers("CISSSCO")

    license("GPL-3.0-only")

    version("8.1.0", sha256="49c437b382488cd9bdb509cb79a67d6952ab28e3e1178b6a2558b543f0b4d474")
    version("8.0.0", sha256="63b39e266ad54167ca8f71a6c63b73f982e43ea50d12f92bed86386eea098ce3")

    variant("mpi", default=True, description="Build parallel version with MPI")
    variant("openmp", default=False, description="Build with OpenMP support")
    variant("double-precision", default=False, description="Treat REAL as double precision")
    variant("scotch", default=True, description="Enable Scotch support")
    variant("debug", default=False, description="Build with debugging options")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("mpi", when="+mpi")
    depends_on("scotch", when="+scotch")

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

        if "+scotch" in spec:
            args.append(f"--with-scotch-dir={spec['scotch'].prefix}")

        args.extend(self.enable_or_disable("openmp"))
        args.extend(self.enable_or_disable("double-precision"))
        args.extend(self.enable_or_disable("debug"))

        return args

    def install(self, spec, prefix):
        install_tree(".", prefix)
