# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

#: runtime version: its SDK, and checksums by .NET runtime identifier
RELEASES = {
    "10.0.14": {
        "sdk": "10.0.403",
        "sha256": {
            "linux-x64": "cd7224fe8e8ba57c15f1601439ff8785a1a72b54ae5c89dd5302a32dcfbddf18",
            "linux-arm64": "21fe1a0963984206bfaeb19968da07e7a61d30c9bc4621b7372a762a30c88679",
            "osx-x64": "cccca37f1ce3a69f99982b80c9546019d149dd2ad26c4ecc01b3b3ab87abeb0e",
            "osx-arm64": "826d7ff91fa83b16bccd7edd7822581fe32b5228a4501aabe61d864168129d73",
            "win-x64": "f398979a9cac2dba760771c4e01f16e431dcd6bcfb2213e3e8f5b3d354095cc0",
            "win-arm64": "c8d5a6714ae9561c2c41f00325a8f9b34f80f520263059921a36a141cddf2ca8",
        },
    },
    "8.0.21": {
        "sdk": "8.0.121",
        "sha256": {
            "osx-x64": "7ac6d6356300947e5c926fb6eb03bcda10d6d886d063de17ed63ae23b70e4756",
            "osx-arm64": "2cc5724a8470c3cd6db9f3d3c4970f5cd019a5186546a7acb0edd1703c6b8a09",
            "win-x64": "f5bbabfaaad0a07e19a641516a0a3d32160d5a05d2431d1bc67a1fcd47a0ca76",
            "win-arm64": "9ef78ec827d453bdfe774b7ebf2c504b0257e9d5116698accf60b06291ee8b4b",
        },
    },
    "8.0.17": {
        "sdk": "8.0.411",
        "sha256": {
            "linux-x64": "2212ace90b536bd99910baf485e925024a37fc08e31fc8c1014fe4392b8d4967",
            "linux-arm64": "7e28342741de05af2c4244c7384230bf51a3ffe6f314f26a25d1b57222c27751",
        },
    },
    "6.0.36": {
        "sdk": "6.0.428",
        "sha256": {
            "linux-x64": "9b2f9b91e28677b58e47d34a1d9e2a88f597af1f6acd44764a3abc2f1bacdc8a",
            "linux-arm64": "b5956b0d9ab3063c2886ec74adc953394e81a1aa3f5075c6b41b3e4f1d7a53f9",
        },
    },
}


class DotnetCoreSdk(Package):
    """The .NET Core SDK is a powerful development environment to write
    applications for all types of infrastructure."""

    homepage = "https://www.microsoft.com/net/"

    maintainers("grospelliergilles")
    license("MIT")

    # binaries for the host; platform.machine() is "arm64" on macOS, "AMD64"/"ARM64" on Windows
    _os = {"Linux": "linux", "Darwin": "osx", "Windows": "win"}.get(platform.system())
    _arch = {"x86_64": "x64", "amd64": "x64", "aarch64": "arm64", "arm64": "arm64"}.get(
        platform.machine().lower()
    )
    _rid = f"{_os}-{_arch}"
    _ext = "zip" if _os == "win" else "tar.gz"

    for _ver, _release in RELEASES.items():
        if _rid in _release["sha256"]:
            _sdk = _release["sdk"]
            version(
                _ver,
                url=f"https://builds.dotnet.microsoft.com/dotnet/Sdk/{_sdk}/dotnet-sdk-{_sdk}-{_rid}.{_ext}",
                sha256=_release["sha256"][_rid],
            )

    variant("telemetry", default=False, description="allow collection of telemetry data")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # for apps built with this SDK to find the runtime
        env.set("DOTNET_ROOT", self.prefix)
        if self.spec.satisfies("platform=windows"):
            env.prepend_path("PATH", self.prefix)
        if self.spec.satisfies("~telemetry"):
            env.set("DOTNET_CLI_TELEMETRY_OPTOUT", "1")

    def install(self, spec, prefix):
        # dotnet.exe finds the SDK next to it, so on Windows there is no bin/
        if not spec.satisfies("platform=windows"):
            mkdirp("bin")
            symlink("../dotnet", "bin/dotnet")
        install_tree(".", prefix)
