# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Pdsh(AutotoolsPackage):
    """
    PDSH: a high performance, parallel remote shell utility
    """

    homepage = "https://github.com/chaos/pdsh"
    url = "https://github.com/chaos/pdsh/archive/refs/tags/pdsh-2.31.tar.gz"
    git = "https://github.com/chaos/pdsh.git"

    license("GPL-2.0")

    version("2.35", tag="pdsh-2.35", commit="64a7d3771e0298bbfa1edc25364700a680c183cd")
    version("2.34", tag="pdsh-2.34", commit="3f7e40f5d287cff388031388071c87b52d3ebe44")
    version("2.33", tag="pdsh-2.33", commit="79aa5a45475abce5ec88d7566b39a4a2d87d2f64")
    version("2.32", tag="pdsh-2.32", commit="84472b845c9c3bbdb2421d98dda22978ed424ff8")
    # get commit has of tag via 'git rev-list -n 1 tags/$TAG' in chaos/pdsh repo
    # configure.ac update in source repo: now uses 'git describe --always' to get the version
    version("2.31", sha256="0ee066ce395703285cf4f6cf00b54b7097d12457a4b1c146bc6f33d8ba73caa7")

    patch(
        "https://github.com/chaos/pdsh/commit/01b1a2150e5d2c1a065aeb05a504f1f92b2cc147.patch?full_index=1",
        sha256="3effcc73c7b5efbe73d12579eb09982c160a116edf86f0bdb315daeebce0802e",
        when="@2.33:",
        # when="@8c173e645dfc5cb6619c4d0647f3fe495ad4ce7f:",
    )  # first commit after 2924dd8ff07b31a81c4a81254ae1e1f81b39595e (shortly after pdsh-2.32)

    # ## conflict when patch cannot be applied before and at
    # ## commit 2924dd8ff07b31a81c4a81254ae1e1f81b39595e
    conflicts("%gcc@15:", when="@:2.32")

    variant("ssh", default=True, description="Build with ssh module")
    variant("static_modules", default=True, description="Build with static modules")

    depends_on("c", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        args = []
        if "+ssh" in self.spec:
            args.append("--with-ssh")
        if "+static_modules" in self.spec:
            args.append("--enable-static-modules")
        return args
