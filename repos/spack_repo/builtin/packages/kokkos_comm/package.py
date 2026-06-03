# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class KokkosComm(CMakePackage):
    """Kokkos Comm is an experimental performance portable explicit communication interface for the Kokkos ecosystem."""

    homepage = "https://github.com/kokkos/kokkos-comm"
    url = "https://github.com/kokkos/kokkos-comm/archive/refs/tags/v0.1.0.tar.gz"

    maintainers("cedricchevalier19", "dssgabriel", "cwpearson")

    license("Apache-2.0 WITH LLVM-exception", checked_by="cedricchevalier19")

    version("0.1.0", sha256="59f4b953a795adb62f306e0861c7e69ee60c8cd2a6f1bd58eb4623b9ab774d45")

    variant("mpi", description="Enable MPI backend", default=True)
    variant("nccl", description="Enable NCCL backend", default=False)

    # Mandatory dependencies
    depends_on("cxx")
    depends_on("c", when="+mpi")
    depends_on("cmake@3.22:3", type="build")

    depends_on("kokkos@4.7:")

    # MPI-backend dependencies
    depends_on("mpi@3:", when="+mpi")

    # NCCL-backend dependencies
    depends_on("kokkos +cuda", when="+nccl")
    depends_on("cuda", when="+nccl")
    depends_on("nccl@2.20:", when="+nccl")

    def cmake_args(self):
        args = [
            self.define("KokkosComm_ENABLE_MPI", "mpi"),
            self.define("KokkosComm_ENABLE_NCCL", "nccl"),
            self.define("KokkosComm_ENABLE_TESTS", True),
        ]

        if self.spec.satisfies("^kokkos+rocm") and not (
            self.spec.satisfies("^kokkos %cxx=clang") or self.spec.satisfies("^kokkos %cxx=rocmcc")
        ):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
