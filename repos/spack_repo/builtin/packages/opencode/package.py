# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Opencode(Package):
    """
    opencode is an open-source AI coding agent for the terminal, running as a TUI or as a
    headless CLI against MCP servers and LLM providers.
    """

    homepage = "https://opencode.ai"
    url = "https://github.com/anomalyco/opencode/archive/refs/tags/v1.18.3.tar.gz"
    supplier = "Organization: Anomaly Innovations"

    maintainers("aprozo")

    license("MIT", checked_by="aprozo")

    sanity_check_is_file = ["bin/opencode"]

    version("2.2.5", sha256="04621edf6c47c2c7a36982ef39914d482c16977708fbd7b779f49f928bdc4fba")
    version("1.18.3", sha256="494041aedd7407079f91fd694de355f4ff022ba6bf876e09ff30983bbdc70ae1")

    depends_on("bun@1.4.4:1", type="build", when="@2:")
    depends_on("bun@1.3.14:1.3", type="build", when="@:1")
    depends_on("node-js@22.12:", type="build")
    depends_on("ripgrep", type="run")

    phases = ["build", "install"]

    def setup_build_environment(self, env):
        # the build scripts read both from git, which a release archive has not
        env.set("OPENCODE_VERSION", self.spec.version.string)
        env.set("OPENCODE_CHANNEL", "stable")
        env.set("HOME", self.stage.path)
        env.set("BUN_INSTALL_CACHE_DIR", join_path(self.stage.path, "bun-cache"))

    @property
    def cli_dir(self):
        # 2.0 moved the command line app from packages/opencode to packages/cli
        return join_path("packages", "cli" if self.spec.satisfies("@2:") else "opencode")

    def build(self, spec, prefix):
        bun = which("bun", required=True)

        workspaces = ["./", "./packages/app", f"./{self.cli_dir}"]
        if spec.satisfies("@:1"):
            workspaces += ["./packages/desktop", "./packages/shared"]

        filters = []
        for workspace in workspaces:
            filters += ["--filter", workspace]

        bun(
            "install",
            "--cpu=*",
            "--os=*",
            "--frozen-lockfile",
            "--ignore-scripts",
            "--no-progress",
            *filters,
        )

        with working_dir(self.cli_dir):
            bun("--bun", "./script/build.ts", "--single", "--skip-install")

    def install(self, spec, prefix):
        (binary,) = glob.glob(join_path(self.cli_dir, "dist", "*", "bin", "opencode"))

        mkdirp(prefix.bin)
        install(binary, prefix.bin)
        set_executable(join_path(prefix.bin, "opencode"))

    def setup_run_environment(self, env):
        env.set("OPENCODE_DISABLE_AUTOUPDATE", "true")
