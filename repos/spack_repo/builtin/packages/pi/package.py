# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Pi(Package):
    """
    Pi is a coding agent CLI with read, bash, edit, and write tools for AI-assisted development.
    """

    homepage = "https://pi.dev"
    url = "https://github.com/earendil-works/pi/archive/refs/tags/v0.79.1.tar.gz"
    supplier = "earendil"

    maintainers("alecbcs")

    license("MIT", checked_by="alecbcs")

    version("0.79.2", sha256="e3e28b40ca6db9f53bcb9ee07b56c789ce535e7ba4e4442ed2fce5d66b3623f3")

    depends_on("node-js@22.19.0:", type=("build", "link", "run"))
    depends_on("npm", type=("build", "run"))

    phases = ["build", "install"]

    def build(self, spec, prefix):
        npm = which("npm", required=True)

        npm("install", "--ignore-scripts")
        npm("run", "build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)

        npm(
            "install",
            "--global",
            f"--prefix={prefix}",
            "--ignore-scripts",
            "./packages/coding-agent",
        )
