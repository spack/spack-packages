# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class RcclTests(ROCmLibrary, CMakePackage):
    """These tests check both the performance and the correctness of RCCL
    operations. They can be compiled against RCCL."""

    homepage = "https://github.com/ROCm/rocm-systems/tree/develop/projects/rccl-tests"
    git = "https://github.com/ROCm/rocm-systems.git"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel", "bvanessen")

    license("BSD-3-Clause")

    rocm_url_map = [
        (None, "https://github.com/ROCm/rocm-systems/archive/refs/tags/therock-{1}.{2}.tar.gz"),
    ]

    version("10.1.0", sha256="31dc4296cb15c3eada729743731d236ee4a52e4a2a301b9da9075b94c012be19")
    version("10.0.0", sha256="f30517ed6d9e18cde104eb487f173e62fed0175083a9498ca383f8136a9f4eec")
    version("7.14.0", sha256="8cadf0d5c0f53f334b7b940a78619d1746c913b26ae719e2a09e20a6f7128330")

    variant("mpi", default=True, description="with MPI support")

    depends_on("cxx", type="build")
    requires("%cxx=llvm-amdgpu", msg="rccl-tests builds only with llvm-amdgpu")

    for ver in ["7.14.0", "10.0.0", "10.1.0"]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rccl@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")

    depends_on("mpi", when="+mpi")
    depends_on("googletest@1.14:", when="@10.1:")

    root_cmakelists_dir = "projects/rccl-tests"

    def cmake_args(self):
        return [
            self.define("EXPLICIT_ROCM_VERSION", self.spec["hip"].version),
            self.define("ROCM_PATH", self.spec["hip"].prefix),
            self.define("RCCL_ROOT", self.spec["rccl"].prefix),
            self.define_from_variant("USE_MPI", "mpi"),
        ]
