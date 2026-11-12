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

    version("1.18.3", sha256="494041aedd7407079f91fd694de355f4ff022ba6bf876e09ff30983bbdc70ae1")

    depends_on("bun@1.3.14:1", type="build")
    depends_on("node-js@22.12:", type="build")
    depends_on("ripgrep", type="run")

    phases = ["build", "install"]

    def setup_build_environment(self, env):
        # the build scripts read both from git, which a release archive has not
        env.set("OPENCODE_VERSION", self.spec.version.string)
        env.set("OPENCODE_CHANNEL", "stable")
        env.set("HOME", self.stage.path)
        env.set("BUN_INSTALL_CACHE_DIR", join_path(self.stage.path, "bun-cache"))

    def build(self, spec, prefix):
        bun = which("bun", required=True)

        bun(
            "install",
            "--cpu=*",
            "--os=*",
            "--frozen-lockfile",
            "--ignore-scripts",
            "--no-progress",
            "--filter",
            "./",
            "--filter",
            "./packages/app",
            "--filter",
            "./packages/desktop",
            "--filter",
            "./packages/opencode",
            "--filter",
            "./packages/shared",
        )

        with working_dir(join_path("packages", "opencode")):
            bun("--bun", "./script/build.ts", "--single", "--skip-install")

    def install(self, spec, prefix):
        (binary,) = glob.glob(join_path("packages", "opencode", "dist", "*", "bin", "opencode"))

        mkdirp(prefix.bin)
        install(binary, prefix.bin)
        set_executable(join_path(prefix.bin, "opencode"))

    def setup_run_environment(self, env):
        env.set("OPENCODE_DISABLE_AUTOUPDATE", "true")
