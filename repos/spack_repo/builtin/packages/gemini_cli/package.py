# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class GeminiCli(Package):
    """ """

    homepage = "https://github.com/anthropics/claude-code"
    url = "https://registry.npmjs.org/@google/gemini-cli/-/gemini-cli-0.20.2.tgz"
    git = "https://github.com/google-gemini/gemini-clu.git"

    maintainers("wdconinc")
    license("Apache-2.0")

    version("0.20.2", sha256="4d9da964f0380907d8c839ea8bd80589e5015d308ae802b7a05818f017d29ccb")

    depends_on("node-js@18:", type=("build", "run"))
    depends_on("npm", type="build")

    def install(self, spec, prefix):
        npm = which("npm", required=True)
        # Set AUTHORIZED to true per package.json:scripts:prepare
        with set_env(AUTHORIZED="true"):
            npm("install", "--global", f"--prefix={prefix}")
