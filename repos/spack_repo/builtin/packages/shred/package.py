# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Shred(MakefilePackage):
    """Stochastic and Hybrid Representation Electronic structure by Density functional theory (SHRED). 
       SHRED is a plane-wave DFT code similar to ABINIT, VASP and Quantum Espresso. """

    url = "https://github.com/alwhite-LANL/SHRED/"
    git = "git@github.com:alwhite-LANL/SHRED.git"

    maintainers("finkeljos", "alwhite")

    license("GPL-3.0-or-later")

    version("develop",branch="new_develop")

    depends_on("fortran", type="build") 
    depends_on("c", type="build")  

    # Necessary package dependencies
    depends_on("mpi")
    depends_on("libxc")
    depends_on("fftw+mpi+openmp")
    depends_on("scalapack")
    depends_on("lapack")
    depends_on("blas")

    # Need libxc version less than 6.0.0
    conflicts('^libxc', when="@:6.0.0",msg='libxc version must be <6.0.0')

    build_system("makefile", default="makefile")

    # Makefile uses GNU extensions
    depends_on("gmake", type="build")

    def setup_build_environment(self, env):
        spec = self.spec

        # Set env variables which are then used by Makefile
        env.set('MPI_DIR', "%s" % spec["mpi"].prefix)
        env.set('FFTW_DIR', "%s" % spec["fftw"].prefix)
        env.set('XC_DIR', "%s" % spec["libxc"].prefix)
        env.set('LA_DIR', "%s" % spec["lapack"].prefix)
        env.set('PLA_DIR', "%s" % spec["scalapack"].prefix)

    def install(self, spec, prefix):

        # install to the spack view 
        mkdirp(prefix.bin)
        install("shred", prefix.bin)

