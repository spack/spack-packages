# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Lazygit(GoPackage):
    """A simple terminal UI for git commands"""

    homepage = "https://github.com/jesseduffield/lazygit"
    url = "https://github.com/jesseduffield/lazygit/archive/refs/tags/v0.40.2.tar.gz"

    maintainers("trws", "Chrismarsh")

    license("MIT", checked_by="mcmehrtens", when="@0.1:")

    version("0.62.2", sha256="0bd1cdbaf1a584d2eb2fd14f068a8eaaeaeb80d3e2713c72005de9e4feaf6844")
    version("0.62.1", sha256="198602c75c0d971b56088d6d364aaf9b2fd52bcadcb0e6a8548df0ed43e4dac2")
    version("0.62.0", sha256="15f20b97c98a799998bc2d32a9a68674a7ddee8b73735d6d4758fafc854a00cb")
    version("0.61.1", sha256="2a550c9b609c5eb0e1c2640e8114ac05b94c671803f77e08a9dcdbd66372e2c4")
    version("0.61.0", sha256="24b0ce4f98834f2b2df0a015a13d6846d2711eba8ae2c0e5612c84dbc55b4c10")
    version("0.60.0", sha256="c0cb64f7861e439ef13fa06845e7ab6b219364b7b083c7ff10d851e764e6b16b")
    version("0.59.0", sha256="f78fca0ddbff18f7a5a8d04ba582354b98f2e42d181421090638e4ecfcdfd33c")
    version("0.58.1", sha256="e4f0d4f3cebc70a802f95c52265e34ee879265103ebb70b5dd449ae791d0cbbb")
    version("0.52.0", sha256="2d6b045105cca36fb4a9ea9fa8834bab70f99a71dcb6f7a1aea11184ac1f66f8")
    version("0.44.1", sha256="02b67d38e07ae89b0ddd3b4917bd0cfcdfb5e158ed771566d3eb81f97f78cc26")
    version("0.41.0", sha256="f2176fa253588fe4b7118bf83f4316ae3ecb914ae1e99aad8c474e23cea49fb8")
    version("0.40.2", sha256="146bd63995fcf2f2373bbc2143b3565b7a2be49a1d4e385496265ac0f69e4128")

    # the go version is noted at
    # https://github.com/jesseduffield/lazygit/blob/master/go.mod#L3
    depends_on("go@1.25:", type="build", when="@0.58.1:")
    depends_on("go@1.24:", type="build", when="@0.52:")
    depends_on("go@1.22:", type="build", when="@0.42:")
    depends_on("go@1.21:", type="build", when="@0.41:")
    depends_on("go@1.20:", type="build", when="@0.40:")

    # https://github.com/jesseduffield/lazygit/blob/master/pkg/app/app.go#L143
    depends_on("git@2.32:", type="run", when="@0.58.1:")

    # https://github.com/jesseduffield/lazygit/blob/v0.52.0/pkg/app/app.go#L151
    depends_on("git@2.22:", type="run", when="@0.52.0")
    depends_on("git@2.20:", type="run", when="@:0.44.1")

    @property
    def ldflags(self):
        # any buildSource other than "binaryRelease" disables lazygit's
        # built-in self-updater, which Spack-managed installs shouldn't use
        return [f"-X main.version={self.spec.version}", "-X main.buildSource=spack"]
