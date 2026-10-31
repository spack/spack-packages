# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Koliop(CMakePackage):
    """A KOkkos based colLIsion OPerator (KoLiOp) that computes the evolution of the distribution
    function due to collisions."""

    homepage = "https://github.com/gyselax/gysela-collisions"
    git = "https://github.com/gyselax/gysela-collisions.git"
    url = "https://github.com/gyselax/gysela-collisions/archive/refs/tags/v1.0.0.tar.gz"

    maintainers("etiennemlb", "tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("master", branch="master", no_cache=True)
    version("1.0.0", sha256="e9d2a18b69c9c023fa6d0bbfd6bab3d2600a3d5ef5349ade947a483ae3dfd764")
    version("0.2.1", sha256="18d6efc146704f47057e6ce4175ef1aa930605c5ffb778885cafe3f1cd5083fd")
    version("0.2.0", sha256="9217d52d153e4d4a309fc1635f573c56f5fd44a99f58a1afbf6fe603c503104f")
    version("0.1.3", sha256="873045019db6fef4f91e5824de2ae1bb93823583ebe54c7637589575f46fd964")
    version("0.1.2", sha256="35c203e574d3615803947d84ee908990dd5839e85cb6796045e849ee52a4977f")
    version("0.1.1", sha256="5c039043d77d67addb9a295ef3fd4bdea83f250630a0a6e2d48d773c523301f9")
    version("0.1.0", sha256="564cf5acc3c2411b8c50cf1429d942541ef9ac53ebf1c4005330a2338db6b3db")

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:4", type="build")

    depends_on("kokkos@4.1:")
    depends_on("kokkos@:5")
    depends_on("kokkos@:4", when="@:0.1")

    depends_on("kokkos-kernels@4.1:")
    depends_on("kokkos-kernels@:5")
    depends_on("kokkos-kernels@:4", when="@:0.1")

    def cmake_args(self):
        args = [
            self.define("koliop_ASSERT_ENABLED", True),
            self.define("koliop_BUILD_TESTING", self.run_tests),
            self.define("koliop_CONSTANT_MEMORY_USAGE", False),
            self.define("koliop_ENABLE_Kokkos", "SYSTEM"),
            self.define("koliop_ENABLE_KokkosKernels", "SYSTEM"),
            self.define("koliop_ENABLE_LTO", False),
            self.define("koliop_RUN_DEMONSTRATION_AS_TEST", False),
            self.define("koliop_UTILITY_FLATTEN_EXPECT_POW2_EXTENTS", False),
        ]
        if self.spec.satisfies("@0"):
            args.append(self.define("koliop_ASSUME_INPUT_BUFFERS_ARE_DEVICE_COMPATIBLE", True))
            args.append(self.define("koliop_BUILD_FORTRAN_INTERFACE", False))
            args.append(self.define("koliop_FENCE_ON_OPERATOR_EXIT", False))

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
