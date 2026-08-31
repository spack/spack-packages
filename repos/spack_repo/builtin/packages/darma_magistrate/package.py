# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DarmaMagistrate(CMakePackage):
    """Serialization and checkpointing library"""

    homepage = "https://github.com/DARMA-tasking/magistrate"
    git = "https://github.com/DARMA-tasking/magistrate.git"

    license("BSD-3-Clause")

    version("develop", branch="develop")
    version("1.7.0", tag="1.7.0")
    version("1.6.0", tag="1.6.0")

    variant("kokkos", default=False, description="Enable Kokkos support")

    sanity_check_is_dir = ["include/checkpoint"]
    sanity_check_is_file = [
        "cmake/magistrateConfig.cmake",
        "cmake/magistrateTargets.cmake",
        "lib/libmagistrate.a",
    ]

    depends_on("kokkos", when="+kokkos")
    depends_on("googletest", type=("test"))
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        args = [
            self.define("magistrate_tests_enabled", self.run_tests),
            self.define("magistrate_examples_enabled", self.run_tests),
        ]

        if "+kokkos" in self.spec:
            args.append(self.define("Kokkos_ROOT", self.spec["kokkos"].prefix))

        return args
