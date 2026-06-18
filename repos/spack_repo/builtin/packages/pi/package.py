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
    url = "https://github.com/earendil-works/pi/archive/refs/tags/v0.79.2.tar.gz"
    supplier = "earendil"

    maintainers("alecbcs")

    license("MIT", checked_by="alecbcs")

    sanity_check_is_file = ["bin/pi"]

    version("0.79.6", sha256="60d255bd9465a7e5ef461ab6ac8529a9d7ad837dca0fafd50af18f1824928772")

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
