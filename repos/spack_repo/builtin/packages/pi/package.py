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

    version("0.79.1", sha256="6e3a0c61dca8ec8a07cc027b6213fd1e0530e64411cae1e2cac550e9fa8cfac5")

    depends_on("node-js@22.19.0:", type=("build", "link", "run"))
    depends_on("npm", type="build")

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
