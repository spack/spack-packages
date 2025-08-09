# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackConfigsDavSdk(CMakePackage):
    """Spack configs for the Data & Vis SDK."""

    homepage = "https://dav-sdk.github.io/"
    git = "https://github.com/dav-sdk/davsdk.git"

    maintainers("kwryankrattiger", "qtpowell", "vicentebolea")

    license("Apache-2.0")

    version("main", branch="main")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("SPACK_CONFIG_DAV_SDK_DIR", self.prefix.spack.configs.davsdk)
        env.set("SPACK_CONFIG_DAV_SDK_ENVIRONMENTS_DIR", self.prefix.spack.environments.davsdk)
