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

    maintainers("grospelliergilles")
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
    elif platform.system() == "Darwin" and platform.machine() == "x86_64":
        version(
            "8.0.21",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.121/dotnet-sdk-8.0.121-osx-x64.tar.gz",
            sha256="7ac6d6356300947e5c926fb6eb03bcda10d6d886d063de17ed63ae23b70e4756",
            preferred=True,
        )
    elif platform.system() == "Darwin" and platform.machine() == "aarch64":
        version(
            "8.0.21",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.121/dotnet-sdk-8.0.121-osx-arm64.tar.gz",
            sha256="2cc5724a8470c3cd6db9f3d3c4970f5cd019a5186546a7acb0edd1703c6b8a09",
            preferred=True,
        )
    elif platform.system() == "Windows" and platform.machine() == "x86_64":
        version(
            "8.0.21",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.121/dotnet-sdk-8.0.121-win-x64.zip",
            sha256="f5bbabfaaad0a07e19a641516a0a3d32160d5a05d2431d1bc67a1fcd47a0ca76",
            preferred=True,
        )
    elif platform.system() == "Windows" and platform.machine() == "aarch64":
        version(
            "8.0.21",
            url="https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.121/dotnet-sdk-8.0.121-win-arm64.zip",
            sha256="9ef78ec827d453bdfe774b7ebf2c504b0257e9d5116698accf60b06291ee8b4b",
            preferred=True,
        )

    variant("telemetry", default=False, description="allow collection of telemetry data")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("~telemetry"):
            env.set("DOTNET_CLI_TELEMETRY_OPTOUT", "1")

    def install(self, spec, prefix):
        mkdirp("bin")
        symlink("../dotnet", "bin/dotnet")
        install_tree(".", prefix)
