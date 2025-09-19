# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class DotnetCoreSdk(Package):
    """The .NET Core SDK is a powerful development environment to write
    applications for all types of infrastructure."""

    homepage = "https://www.microsoft.com/net/"

    license("MIT")

    if platform.system() == "Linux" and platform.machine() == "x86_64":
        version(
            "8.0.17",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.411/dotnet-sdk-8.0.411-linux-x64.tar.gz",
            sha256="2212ace90b536bd99910baf485e925024a37fc08e31fc8c1014fe4392b8d4967",
            preferred=True,
        )
        version(
            "6.0.36",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/6.0.428/dotnet-sdk-6.0.428-linux-x64.tar.gz",
            sha256="9b2f9b91e28677b58e47d34a1d9e2a88f597af1f6acd44764a3abc2f1bacdc8a",
        )
    elif platform.system() == "Linux" and platform.machine() == "aarch64":
        version(
            "8.0.17",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.411/dotnet-sdk-8.0.411-linux-arm64.tar.gz",
            sha256="7e28342741de05af2c4244c7384230bf51a3ffe6f314f26a25d1b57222c27751",
            preferred=True,
        )
        version(
            "6.0.36",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/6.0.428/dotnet-sdk-6.0.428-linux-arm64.tar.gz",
            sha256="b5956b0d9ab3063c2886ec74adc953394e81a1aa3f5075c6b41b3e4f1d7a53f9",
        )

    variant("telemetry", default=False, description="allow collection of telemetry data")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("~telemetry"):
            env.set("DOTNET_CLI_TELEMETRY_OPTOUT", "1")

    def install(self, spec, prefix):
        mkdirp("bin")
        symlink("../dotnet", "bin/dotnet")
        install_tree(".", prefix)
