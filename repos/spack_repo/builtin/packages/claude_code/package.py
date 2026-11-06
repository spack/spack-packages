# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class ClaudeCode(Package):
    """Claude Code is an agentic coding tool that lives in your terminal,
    understands your codebase, and helps you code faster by executing routine
    tasks, explaining complex code, and handling git workflows -- all through
    natural language commands."""

    homepage = "https://github.com/anthropics/claude-code"
    url = "https://github.com/anthropics/claude-code/releases/download/v2.1.296/claude-linux-x64.tar.gz"

    maintainers("wdconinc")
    license("Anthropic-Claude")

    sanity_check_is_file = ["bin/claude"]

    # Checksums from SHASUMS256.txt of each release
    claude_versions = {
        "2.1.296": {
            "linux": {
                "x86_64": "45fe2b33f5cbdd114309618970bcd90b8b163e34252d66cf100d7e068d9b831d",
                "aarch64": "c644ad3e5ca3367e75d198194189d13180f33c491304c2d19557f7c1e8d5e0a6",
            },
            "darwin": {
                "x86_64": "3851a1f6a6a28870615e2b76bc0e85af020b9ac7d6b71c9e6f2b35817a012451",
                "arm64": "60f97cde7f7e078b424138e34ecf1ad620bd81ac3866984fb8996623a36a052e",
            },
        }
    }

    archive_name = {
        "linux": {"x86_64": "linux-x64", "aarch64": "linux-arm64"},
        "darwin": {"x86_64": "darwin-x64", "arm64": "darwin-arm64"},
    }

    system = platform.system().lower()
    machine = platform.machine().lower()

    for ver in claude_versions:
        if system in claude_versions[ver] and machine in claude_versions[ver][system]:
            version(ver, sha256=claude_versions[ver][system][machine])

    def url_for_version(self, version):
        target = self.archive_name.get(self.system, {}).get(self.machine)

        if target is None:
            return None

        return f"{self.homepage}/releases/download/v{version}/claude-{target}.tar.gz"

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("claude", prefix.bin)
        set_executable(prefix.bin.claude)

    def setup_run_environment(self, env):
        env.set("DISABLE_AUTOUPDATER", "1")
