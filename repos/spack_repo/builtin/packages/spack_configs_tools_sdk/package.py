# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackConfigsToolsSdk(CMakePackage):
    """Spack configs for the TOOLS SDK."""

    homepage = "https://tools-integration.github.io/"
    git = "https://github.com/tools-integration/tools-sdk.git"

    maintainers("kwryankrattiger", "qtpowell", "vicentebolea")

    license("Apache-2.0")

    version("main", branch="main")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("SPACK_CONFIG_TOOLS_SDK_DIR", self.prefix.spack.configs.toolssdk)
        env.set("SPACK_CONFIG_TOOLS_SDK_ENVIRONMENTS_DIR", self.prefix.spack.environments.toolssdk)
