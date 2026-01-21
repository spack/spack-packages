# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.cached_cmake import CachedCMakePackage, cmake_cache_option


class Adiak(CachedCMakePackage):
    """Adiak collects metadata about HPC application runs and provides it
    to tools."""

    homepage = "https://github.com/LLNL/Adiak"
    url = "https://github.com/LLNL/Adiak/releases/download/v0.1/adiak-v0.1.1.tar.gz"
    git = "https://github.com/LLNL/Adiak"

    maintainers("daboehme", "mplegendre")

    variant("mpi", default=True, description="Build with MPI support")
    variant("shared", default=True, description="Build dynamic libraries")

    license("MIT")
    version(
        "0.5.0", commit="f08c8375c613e13e9b9c6a1db271cbf8f0d3f3e3", submodules=True, preferred=True
    )
    version(
        "0.4.1", commit="7ac997111785bee6d9391664b1d18ebc2b3c557b", submodules=True, preferred=True
    )
    version("0.4.0", commit="7e8b7233f8a148b402128ed46b2f0c643e3b397e", submodules=True)
    version("0.2.2", commit="3aedd494c81c01df1183af28bc09bade2fabfcd3", submodules=True)
    version("0.2.1", commit="950e3bfb91519ecb7b7ee7fa3063bfab23c0e2c9", submodules=True)
    version("0.1.1", sha256="438e4652e15e206cd0019423d829fd4f2329323ff0c8861d9586bae051d9624b")

    depends_on("blt", type="build")
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi", when="+mpi")

    def initconfig_mpi_entries(self):
        spec = self.spec

        entries = super().initconfig_mpi_entries()
        entries.append(cmake_cache_option("ENABLE_MPI", spec.satisfies("+mpi")))
        return entries

    def cmake_args(self):
        args = []

        if self.spec.satisfies("+mpi"):
            args.append("-DENABLE_PYTHON_BINDINGS=ON")
        if self.spec.satisfies("+shared"):
            args.append("-DBUILD_SHARED_LIBS=ON")
        else:
            args.append("-DBUILD_SHARED_LIBS=OFF")

        return args
