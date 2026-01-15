# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Adiak(CMakePackage):
    """Adiak collects metadata about HPC application runs and provides it
    to tools."""

    homepage = "https://github.com/LLNL/Adiak"
    url = "https://github.com/LLNL/Adiak/releases/download/v0.1/adiak-v0.1.1.tar.gz"
    git = "https://github.com/LLNL/Adiak"

    maintainers("daboehme", "mplegendre")

    variant("mpi", default=True, description="Build with MPI support")
    variant("shared", default=True, description="Build dynamic libraries")
    variant("python", default=False, when="@0.5.0:", description="Build Python bindings")

    license("MIT")

    version("master", branch="master")
    version(
        "0.5.0", commit="f08c8375c613e13e9b9c6a1db271cbf8f0d3f3e3", submodules=True, preferred=True
    )
    version("0.4.1", commit="7ac997111785bee6d9391664b1d18ebc2b3c557b", submodules=True)
    version("0.4.0", commit="7e8b7233f8a148b402128ed46b2f0c643e3b397e", submodules=True)
    version("0.2.2", commit="3aedd494c81c01df1183af28bc09bade2fabfcd3", submodules=True)
    version("0.2.1", commit="950e3bfb91519ecb7b7ee7fa3063bfab23c0e2c9", submodules=True)
    version("0.1.1", sha256="438e4652e15e206cd0019423d829fd4f2329323ff0c8861d9586bae051d9624b")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi", when="+mpi")

    with when("+python"):
        extends("python")
        depends_on("python@3:", type=("build", "link", "run"))
        depends_on("py-pybind11@3.0.0:", type=("build", "link", "run"))

    def cmake_args(self):
        args = []
        if self.spec.satisfies("+mpi"):
            args.append(f"-DMPI_CXX_COMPILER={self.spec['mpi'].mpicxx}")
            args.append(f"-DMPI_C_COMPILER={self.spec['mpi'].mpicc}")
            args.append("-DENABLE_MPI=ON")
        else:
            args.append("-DENABLE_MPI=OFF")

        if self.spec.satisfies("+shared"):
            args.append("-DBUILD_SHARED_LIBS=ON")
        else:
            args.append("-DBUILD_SHARED_LIBS=OFF")

        if self.spec.satisfies("+python"):
            args.append("-DENABLE_PYTHON_BINDINGS=ON")
            pybind11_cmake = os.path.join(
                self.spec["py-pybind11"].prefix, "pybind11", "share", "cmake", "pybind11"
            )
            args.append(f"-Dpybind11_DIR={pybind11_cmake}")

        args.append("-DENABLE_TESTS=OFF")
        return args
