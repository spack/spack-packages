# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Koliop(CMakePackage):
    """A KOkkos based colLIsion OPerator (KoLiOp) that computes the evolution of the distribution
    function due to collisions."""

    homepage = "https://gitlab.com/cines/code.gysela/libkoliop"
    git = "https://gitlab.com/cines/code.gysela/libkoliop.git"
    url = "https://gitlab.com/cines/code.gysela/libkoliop/-/archive/v0.1.0/libkoliop-v0.1.0.tar.gz"

    maintainers("etiennemlb", "tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("master", branch="master", no_cache=True)
    version("0.1.2", sha256="7581e8313b7ebc09b291ac486d7f6d03b55d7e0ce2e8ebf62863177bbb080fd1")
    version("0.1.1", sha256="abf5a7187067a452a6a5e45dcd6502ef077f77a591839adf8d21ed4e8b9987f7")
    version("0.1.0", sha256="511df587fba11c16e728d1ccdc68c9004dcb0cc87c548e955599d69bf68e6642")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:4", type="build")

    depends_on("kokkos@4.1:4")
    depends_on("kokkos-kernels@4.1:4")

    def cmake_args(self):
        args = [
            self.define("koliop_ASSERT_ENABLED", True),
            self.define("koliop_ASSUME_INPUT_BUFFERS_ARE_DEVICE_COMPATIBLE", True),
            self.define("koliop_BUILD_FORTRAN_INTERFACE", False),
            self.define("koliop_BUILD_TESTING", False),
            self.define("koliop_CONSTANT_MEMORY_USAGE", False),
            self.define("koliop_ENABLE_Kokkos", "SYSTEM"),
            self.define("koliop_ENABLE_KokkosKernels", "SYSTEM"),
            self.define("koliop_ENABLE_LTO", False),
            self.define("koliop_FENCE_ON_OPERATOR_EXIT", False),
            self.define("koliop_UTILITY_FLATTEN_EXPECT_POW2_EXTENTS", False),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
