# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackConfigsFacilities(CMakePackage):
    """Spack configs for DOE facilities."""

    git = "https://github.com/e4s-project/facility-external-spack-configs.git"

    maintainers("eugeneswalker", "kwryankrattiger", "qtpowell", "vicentebolea")

    license("UNKNOWN")

    version("main", branch="master")

    variant(
        "facility",
        default="all",
        description="Facility configs to install",
        values=("all", "frontier", "perlmutter"),
    )

    def cmake_args(self):
        args = [self.define_from_variant("FACILITY", "facility")]
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("SPACK_CONFIG_FACILITY_DIR", self.prefix.spack.configs.facilities)
