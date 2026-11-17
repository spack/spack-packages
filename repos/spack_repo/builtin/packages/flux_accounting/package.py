# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class FluxAccounting(AutotoolsPackage):
    """Bank/accounting interface for the Flux resource manager"""

    homepage = "https://github.com/flux-framework/flux-accounting"
    url = "https://github.com/flux-framework/flux-accounting/releases/download/v0.1.0/flux-accounting-0.1.0.tar.gz"
    git = "https://github.com/flux-framework/flux-accounting.git"

    maintainers("sam-maloney")

    license("LGPL-3.0-only")

    version("master", branch="master")
    version("0.61.0", sha256="e542871141ed7f63c513bbec6ee7e1f3521cb82f8cb796cf022c5d60f41a3c36")

    variant("docs", default=False, description="Build flux manpages and docs")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("pkgconfig", type="build")

    # Need autotools when building on master:
    depends_on("autoconf", type="build", when="@master")
    depends_on("automake", type="build", when="@master")
    depends_on("libtool", type="build", when="@master")

    depends_on("flux-core +security")
    depends_on("flux-core@0.81: +security", when="@0.54.0:")
    depends_on("jansson@2.10:")
    depends_on("sqlite")

    depends_on("py-docutils@0.11.0:", type="build", when="+docs")
    depends_on("py-sphinx@1.6.7:", type="build", when="+docs")
    depends_on("py-sphinx-rtd-theme", type="build", when="+docs")

    # Testing Dependencies
    depends_on("jq", type="test")
    depends_on("lua", type="test")
    depends_on("valgrind", type="test")
    depends_on("which", type="test")

    def setup(self):
        pass

    @when("@master")
    def setup(self):
        with working_dir(self.stage.source_path):
            # Allow git-describe to get last tag so flux-version works:
            git = which("git", required=True)
            # When using spack develop, this will already be unshallow
            try:
                git("fetch", "--unshallow")
                git("config", "remote.origin.fetch", "+refs/heads/*:refs/remotes/origin/*")
                git("fetch", "origin")
            except ProcessError:
                git("fetch")

    def autoreconf(self, spec, prefix):
        self.setup()
        if not os.path.exists("configure"):
            # Bootstrap with autotools
            bash = which("bash", required=True)
            bash("./autogen.sh")

    def configure_args(self):
        return self.enable_or_disable("docs")
