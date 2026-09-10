# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class ClaudeCode(Package):
    """Claude Code is an agentic coding tool that lives in your terminal,
    understands your codebase, and helps you code faster by executing routine
    tasks, explaining complex code, and handling git workflows -- all through
    natural language commands."""

    homepage = "https://github.com/anthropics/claude-code"
    url = "https://registry.npmjs.org/@anthropic-ai/claude-code/-/claude-code-2.0.36.tgz"
    git = "https://github.com/anthropics/claude-code.git"

    maintainers("wdconinc")
    license("Anthropic-Claude")

    version("2.1.50", sha256="4d7ab6b04c666ebf2c966a9d22e5b8f57706c0d5a5941523b9b02af9f84e45d5")
    version("2.0.36", sha256="42095aacc8e39d8b7d5c0162fb44d873a1cc39430681269bac492c004cfd0e13")

    depends_on("node-js@18:", type=("build", "run"))
    depends_on("npm", type="build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        # Set AUTHORIZED to true per package.json:scripts:prepare
        with set_env(AUTHORIZED="true"):
            npm("install", "--global", f"--prefix={prefix}")
