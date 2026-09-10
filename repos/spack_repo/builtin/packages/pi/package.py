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
    url = "https://github.com/earendil-works/pi/releases/download/v0.84.3/pi-0.84.3-source.tar.gz"
    supplier = "earendil"

    maintainers("alecbcs")

    license("MIT", checked_by="alecbcs")

    sanity_check_is_file = ["bin/pi"]

    version("0.84.3", sha256="056f84c467450fb5700ad4df9c8cc669bf7f6046976eed7a19eadbc7553b6500")
    version("0.84.2", sha256="96a9efad258fa6fa89f661bbf830c356dd3baf6cd06c6543ce4e8253c143460e")

    depends_on("node-js@22.19.0:", type=("build", "link", "run"))
    depends_on("npm", type=("build", "run"))

    phases = ["build", "install"]

    def build(self, spec, prefix):
        npm = which("npm", required=True)

        npm("install", "--ignore-scripts")
        npm("run", "build:offline")

    def install(self, spec, prefix):
        npm = which("npm", required=True)

        npm(
            "install",
            "--global",
            f"--prefix={prefix}",
            "--ignore-scripts",
            "./packages/coding-agent",
        )
