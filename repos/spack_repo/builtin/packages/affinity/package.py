# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Affinity(CMakePackage, CudaPackage, ROCmPackage):
    """Simple applications for determining Linux thread and gpu affinity."""

    homepage = "https://github.com/bcumming/affinity"
    git = "https://github.com/bcumming/affinity.git"
    version("master", branch="master")

    maintainers("bcumming", "nhanford")

    license("BSD-3-Clause", checked_by="nhanford")

    variant("mpi", default=False, description="Build MPI support")

    conflicts("+rocm", when="+cuda")
    conflicts("+cuda", when="+rocm")

    depends_on("cmake@3.21:", type="build")
    depends_on("mpi", when="+mpi")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [self.define_from_variant("AFFINITY_MPI", "mpi")]
        args += [
            self.define("AFFINITY_GPU_BACKEND", v)
            for v in ["cuda", "rocm"]
            if self.spec.satisfies(f"+{v}")
        ]
        return args
