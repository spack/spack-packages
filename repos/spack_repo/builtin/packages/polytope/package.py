# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Polytope(CMakePackage, CudaPackage, ROCmPackage):
    """C++ library for generating polygonal and polyhedral meshes"""

    homepage = "https://github.com/llnl/polytope"
    url = "https://github.com/llnl/polytope/archive/refs/tags/v0.7.5.tar.gz"
    git = "https://github.com/llnl/polytope.git"

    maintainers("jmikeowen")
    license("BSD-2-Clause")

    version(
        "0.7.5",
        sha256="ee249cfbb38632a704d177bb3269124ab7b227d29a6c36c9857e822cf4df0430"
    )
    
    variant("mpi", default=True, description="Enable MPI support")
    variant("shared", default=False, description="Enable share lib build")
    variant("boost", default=False, description="Enable Boost support")

    with default_args(type="build"):
        depends_on("blt")
        depends_on("cmake@3.1.0:")
        depends_on("c")
        depends_on("cxx")

    depends_on("boost", when="+boost")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        args = [
            self.define("TESTING", "OFF"),
            self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix),
            self.define_from_variant("ENABLE_MPI", "mpi"),
            self.define_from_variant("USE_BOOST", "boost"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]
        return args
