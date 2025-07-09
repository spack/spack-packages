# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Lazygit(GoPackage):
    """A simple terminal UI for git commands"""

    homepage = "https://github.com/jesseduffield/lazygit"
    url = "https://github.com/jesseduffield/lazygit/archive/refs/tags/v0.40.2.tar.gz"

    maintainers("twrs")

    license("MIT")

    version("0.52.0", sha256="2d6b045105cca36fb4a9ea9fa8834bab70f99a71dcb6f7a1aea11184ac1f66f8")
    version("0.44.1", sha256="02b67d38e07ae89b0ddd3b4917bd0cfcdfb5e158ed771566d3eb81f97f78cc26")
    version("0.41.0", sha256="f2176fa253588fe4b7118bf83f4316ae3ecb914ae1e99aad8c474e23cea49fb8")
    version("0.40.2", sha256="146bd63995fcf2f2373bbc2143b3565b7a2be49a1d4e385496265ac0f69e4128")

    # the go version is noted at
    # https://github.com/jesseduffield/lazygit/blob/master/go.mod#L3
    depends_on("go@1.20:", type="build", when="@0.40:")
    depends_on("go@1.21:", type="build", when="@0.41:")
    depends_on("go@1.22:", type="build", when="@0.42:")
    depends_on("go@1.24:", type="build", when="@0.52:")
