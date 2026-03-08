# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class GithubCopilot(Package):
    """GitHub Copilot CLI brings AI-powered coding assistance directly
    to your command line, enabling you to build, debug, and understand
    code through natural language conversations. Powered by the same
    agentic harness as GitHub's Copilot coding agent, it provides
    intelligent assistance while staying deeply integrated with your
    GitHub workflow."""

    homepage = "https://github.com/github/copilot-cli"
    url = "https://registry.npmjs.org/@github/copilot/-/copilot-0.0.354.tgz"
    git = "https://github.com/github/copilot-cli.git"

    maintainers("wdconinc")
    license("GitHub-Pre-Release")

    version("0.0.414", sha256="f268a57fbaf19be20ad985c860c59e9b259edd23a81c3d8416af6ffa7e8d7c62")
    version("0.0.354", sha256="cc61ad9201c75b0ba3442d32861ddba876cd7cd780c94fc64e5fab50c51c0bcb")

    depends_on("node-js@22:", type=("build", "run"))
    depends_on("npm@10:", type="build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        npm("install", "--global", f"--prefix={prefix}")
