# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Alpscore(CMakePackage):
    """The ALPS (Algorithms and Libraries for Physics Simulations) Core libraries aim to provide
    a set of well tested, robust, and standardized components for numerical simulations of
    condensed matter systems, in particular systems with strongly correlated electrons.
    Note that this package provides only the core libraries of ALPS.
    """

    # Homepage and source
    homepage = "https://alpscore.org"
    url = "https://github.com/ALPSCore/ALPSCore/archive/refs/tags/v2.3.2.tar.gz"

    # Maintainers and License info
    maintainers("egull")
    license("MIT", checked_by="egull")

    # Versions and checksums
    version("2.3.2", sha256="bd9b5af0a33acc825ffedfaa0bf794a420ab2b9b50f6a4e634ecbde43ae9cc24")

    # Build system dependencies
    depends_on("cmake@3.1:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Other dependencies
    depends_on("mpi")
    depends_on("hdf5@1.8: ~mpi+hl")
    depends_on("boost@1.56.0: +chrono +date_time +filesystem +iostreams +mpi")
    depends_on("eigen@3.3.4:")

    # Conflicts in dependencies
    conflicts("^cmake@3.6", when="platform=darwin", msg="CMake 3.6 has a known issue on macOS")
    conflicts("^hdf5@1.10 ~mpi+hl", msg="HDF5 1.10 has a known issue")

    def cmake_args(self):
        args = []
        mpi = self.spec["mpi"]
        args.append(self.define("CMAKE_C_COMPILER", mpi.mpicc))
        args.append(self.define("CMAKE_CXX_COMPILER", mpi.mpicxx))
        return args

    def setup_run_environment(self, env):
        # Set environment variable for ALPSCore
        env.set("ALPSCore_DIR", self.prefix)
