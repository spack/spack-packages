# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Exacmech(CMakePackage, CudaPackage, ROCmPackage):
    """GPU-friendly materials library with a focus on crystal plasticity methods"""

    homepage = "https://github.com/llnl/ExaCMech"
    url = "https://github.com/llnl/ExaCMech/archive/refs/tags/v0.4.3.tar.gz"
    git = "https://github.com/llnl/ExaCMech.git"

    maintainers("rcarson3")

    version("develop", branch="develop")
    version("0.4.3", sha256="0740d0eb6b8eb4036dd3b50a9e3061f0986a09c5398ad62b892d3ed221493152")
    version("0.4.2", sha256="66d88d9c19271a43cb511479e00a399f14b11952fe10720eb276dd7db467721c")
    version("0.4.1", sha256="ff0e748bcc7172fc99700974cc2e64f169d7369706a803d110061fccfa3d99a9")
    version("0.4.0", sha256="18f4790552333a6e15487ef277be7fe6476f838b51a11fb0da3b0244b5edd5aa")
    version("0.3.4", sha256="76448be985ed2869298b899dd92f48da1ff6113523e13c1b0e611a434cfb7bd2")
    version("0.3.0", sha256="c879c18c0947f6a6c921b6784ebf436ed75b2af061be428b6eaf60f30b26697d")
    version("0.2.0", sha256="3a2b229b493cfb3490c4a4cbe280c32de8f361f0aa4b9a2a84412dcbfa7e5db6")

    variant("openmp", default=False, description="Enable OpenMP support")
    variant("shared", default=False, description="Enables the build of shared libraries")
    variant("tests", default=False, description="Build with tests enabled")
    variant("batch_solver", default=True, description="enable snls batch solver")
    variant(
        "cxxstd",
        default="17",
        values=("17", "20"),
        description="C++ standard to build with",
    )

    with default_args(type="build"):
        depends_on("blt")
        depends_on("cmake@3.20:")
        depends_on("c", when="+rocm +tests")
        depends_on("cxx")

    depends_on("raja")
    with when("+batch_solver"):
        depends_on("snls+batch_solver")
        depends_on("camp")
        depends_on("chai")
        depends_on("umpire")
    with when("~batch_solver"):
        depends_on("snls+use_raja_only")

    # variant dependent dependencies
    depends_on("raja+openmp", when="+openmp")
    depends_on("cub", when="+cuda")

    def cmake_args(self):
        args = [
            self.define("RAJA_DIR", join_path(self.spec["raja"].prefix, "lib/cmake/raja")),
            self.define("SNLS_DIR", self.spec["snls"].prefix),
            self.define("CAMP_DIR", self.spec["camp"].prefix),
            self.define("CHAI_DIR", self.spec["chai"].prefix),
            self.define("UMPIRE_DIR", self.spec["umpire"].prefix),
            self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix),
            self.define("BLT_CXX_STD", f"c++{self.spec.variants.get('cxxstd').value}"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("ENABLE_GTEST", "tests"),
            self.define("ENABLE_MINIAPPS", "OFF"),
            self.define_from_variant("ENABLE_OPENMP", "openmp"),
            self.define_from_variant("CMAKE_CUDA_SEPARABLE_COMPILATION", "cuda"),
            self.define_from_variant("ENABLE_CUDA", "cuda"),
            self.define_from_variant("ENABLE_HIP", "rocm"),
            self.define_from_variant("ENABLE_TESTS", "tests"),
        ]

        if self.spec.satisfies("@:0.3.5"):
            args.append(self.define("ENABLE_SNLS_V03", "ON"))
        return args
