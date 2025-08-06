# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Shred(MakefilePackage):
    """Stochastic and Hybrid Representation Electronic structure by Density
    functional theory (SHRED). SHRED is a plane-wave DFT code similar to
    ABINIT, VASP and Quantum Espresso."""

    url = "https://github.com/alwhite-LANL/SHRED/"
    git = "git@github.com:alwhite-LANL/SHRED.git"

    maintainers("finkeljos", "alwhite")

    license("GPL-3.0-or-later")

    version("develop", branch="new_develop")

    depends_on("fortran", type="build")
    depends_on("c", type="build")

    # Necessary package dependencies
    depends_on("gmake", type="build")

    depends_on("blas")
    depends_on("fftw+mpi+openmp")
    depends_on("lapack")
    # need libxc version to be less than 6
    depends_on("libxc@:5")
    depends_on("mpi")
    depends_on("scalapack")

    build_system("makefile", default="makefile")

    def setup_build_environment(self, env):
        spec = self.spec

        # Set env variables which are then used by Makefile
        env.set("MPI_DIR", spec["mpi"].prefix)
        env.set("FFTW_DIR", spec["fftw"].prefix)
        env.set("XC_DIR", spec["libxc"].prefix)
        env.set("LA_DIR", spec["lapack"].prefix)
        env.set("PLA_DIR", spec["scalapack"].prefix)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("shred", prefix.bin)
