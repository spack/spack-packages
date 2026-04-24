# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform
from os.path import split

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "26.1.1-3": {
        "Linux-x86_64": ("b25b828b702df4dd2a6d24d4eb56cfa912471dd8e3342cde2c3d86fe3dc2d870",),
        "Linux-aarch64": ("83280e4ee71a5bd547d6b318f96e9ababe1054911ff6cc2b8801ce5493fe67e5",),
    },
    "25.3.0-3": {
        "Linux-x86_64": ("1b57f8cb991982063f79b56176881093abb1dc76d73fda32102afde60585b5a1",),
        "Linux-aarch64": ("ac89f17b0eec4e98d38a53d1ae688e0f22c77d8ea5b5f008c2455e90ef095339",),
    },
    "24.3.0-0": {
        "Linux-x86_64": ("23367676b610de826f50f7ddc91139a816d4b59bd4c69cc9b6082d9b2e7fe8a3",)
    },
    "24.1.2-0": {
        "Linux-x86_64": ("dbadb808edf4da00af35d888d3eeebbfdce71972b60bf4b16dbacaee2ab57f28",)
    },
    "4.8.3-4": {
        "Linux-x86_64": ("24951262a126582f5f2e1cf82c9cd0fa20e936ef3309fdb8397175f29e647646",),
        "Linux-aarch64": ("52a8dde14ecfb633800a2de26543a78315058e30f5883701da1ad2f2d5ba9ed8",),
    },
    "4.8.3-2": {
        "Linux-x86_64": ("c8e5b894fe91ce0f86e61065d2247346af107f8d53de0ad89ec848701c4ec1f9",),
        "Linux-aarch64": ("bfefc0ede6354568978b4198607edd7f17c2f50ca4c6a47e9f22f8c257c8230a",),
        "MacOSX-x86_64": ("25ca082ab00a776db356f9bbc660edf6d24659e2aec1cbec5fd4ce992d4d193d"),
    },
}


def _should_deprecate_version(version: str) -> bool:
    major_version_to_deprecate = 20
    major_version = int(version.split(".")[0])
    return major_version < major_version_to_deprecate


class Miniforge3(Package):
    """Miniforge3 is a minimal installer for conda and mamba specific to conda-forge."""

    homepage = "https://github.com/conda-forge/miniforge"

    maintainers("ChristopherChristofi")

    license("BSD-3-Clause")

    for ver, packages in _versions.items():
        key = f"{platform.system()}-{platform.machine()}"
        pkg = packages.get(key)
        if pkg:
            version(ver, sha256=pkg[0], expand=False, deprecated=_should_deprecate_version(ver))

    variant("mamba", default=True, description="Enable mamba support.")

    conflicts("+mamba", when="@:22.3.1-0")

    def url_for_version(self, version):
        script = f"Miniforge3-{version}-{platform.system()}-{platform.machine()}.sh"
        return f"https://github.com/conda-forge/miniforge/releases/download/{version}/{script}"

    def install(self, spec, prefix):
        dir, script = split(self.stage.archive_file)
        bash = which("bash", required=True)
        bash(script, "-b", "-f", "-p", self.prefix)

    @run_after("install")
    def patch_sbang(self):
        # Conda replaces the full path to the Python executable with `/usr/bin/env python`
        # if the full path exceeds 127 characters. This does however break `conda deactivate`
        # because the wrong Python interpreter is used after activating an environment.
        # The 127 character limit is not relevant in Spack as Spack will automatically
        # use the `sbang` script to deal with the overly long sbang line.
        filter_file(
            r"#!/usr/bin/env python", rf"#!{self.prefix.bin.python}", self.prefix.bin.conda
        )
        if "+mamba" in self.spec:
            filter_file(
                r"#!/usr/bin/env python", rf"#!{self.prefix.bin.python}", self.prefix.bin.mamba
            )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        filename = self.prefix.etc.join("profile.d").join("conda.sh")
        env.extend(EnvironmentModifications.from_sourcing_file(filename))

        if "+mamba" in self.spec:
            filename = self.prefix.etc.join("profile.d").join("mamba.sh")
            env.extend(EnvironmentModifications.from_sourcing_file(filename))

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        """Check the spack install of miniforge3."""

        with working_dir(self.stage.source_path):
            conda = Executable(self.prefix.bin.conda)
            output = conda("--version", output=str.split)
            assert "conda " in output

            if "+mamba" in self.spec:
                mamba = Executable(self.prefix.bin.mamba)
                mamba("--version")
