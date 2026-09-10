# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class CabanaPd(CMakePackage, CudaPackage, ROCmPackage):
    """Peridynamics with the Cabana library"""

    homepage = "https://github.com/ORNL/CabanaPD"
    url = "https://github.com/ORNL/CabanaPD/archive/refs/tags/0.4.0.tar.gz"

    maintainers("streeve")
    license("BSD 3-Clause", checked_by="cmelone")

    version("0.4.0", sha256="a8971284d3c3d0b5f0bf7ee64e893a2b1e2d094cc0ba62b3c04b1f2fda476bca")

    variant("hdf5", default=False, description="Enable HDF5 support")
    variant("silo", default=False, description="Enable SILO support")
    variant("tests", default=False, description="Enable unit tests")

    depends_on("cmake@3.11:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")

    # cannot simultaneously use hipcc and another c++ compiler
    requires("%cxx=rocmcc", when="+rocm")

    depends_on("cabana+grid@0.7.0:")
    depends_on("nlohmann-json@3.10.0:")
    depends_on("cabana+hdf5", when="+hdf5")
    depends_on("cabana+silo", when="+silo")
    depends_on("googletest", when="+tests")

    for arch in CudaPackage.cuda_arch_values:
        cuda_dep = f"+cuda cuda_arch={arch}"
        depends_on(f"cabana {cuda_dep}", when=cuda_dep)

    for arch in ROCmPackage.amdgpu_targets:
        rocm_dep = f"+rocm amdgpu_target={arch}"
        depends_on(f"cabana {rocm_dep}", when=rocm_dep)

    def cmake_args(self):
        args = []

        args.append(self.define_from_variant("CabanaPD_ENABLE_TESTING", "tests"))

        # use hipcc as the cxx compiler if we are compiling for rocm
        # keeps the wrapper instead of changing CMAKE_CXX_COMPILER
        if self.spec.satisfies("+rocm"):
            env["SPACK_CXX"] = self.spec["hip"].hipcc

        return args
