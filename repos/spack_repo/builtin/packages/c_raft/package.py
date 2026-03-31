# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class CRaft(AutotoolsPackage):
    """C implementation of the Raft consensus protocol."""

    homepage = "https://raft.readthedocs.io/en/latest/"
    git = "https://github.com/cowsql/raft.git"
    url = "https://github.com/cowsql/raft/archive/refs/tags/v0.17.1.tar.gz"

    maintainers("mdorier")

    version("main", branch="main")
    version("0.22.1", sha256="385f91a0b542ebe8b81c8f8500310dcd575fd028ea0cd2ede8807fa920dcf604")
    version("0.22.0", sha256="1534146ea40ca0c29abd5369037bc14927f7acd001b61486739ba6b49a28bdff")
    version("0.21.0", sha256="131385e50ed964eed5b5ebac2a8f2789493969b3de3ffb871c009ff2515fab0e")
    version("0.20.0", sha256="adb110fd4f3982f26d1ff2644b25c623e6794aa159bf85c3ae4824e91ceb249a")
    version("0.19.1", sha256="fb75ec93c4f8c161f73e08a4d0273f36817a20c91b89035abe793ca9b3dd6fba")
    version("0.19.0", sha256="60d5af9a9ade3b290819b936754eeeacfc66769bc49c9f9dd7be89054e98907f")
    version("0.18.3", sha256="8709bd4fda9e871bf54b929d32265ce54f304fce94527566d2c44f723753838b")
    version("0.18.2", sha256="cc3e12877150cb9cdfa82486a9bfe39e4050dba8a6e8a55aa27c86b7d21237b9")
    version("0.18.1", sha256="f863f395c0fefe9aa8491f1d1dd87686fa53f7fe2c2fd223e9a03b3141a08597")
    version("0.17.7", sha256="7d0249953c2e2b112e9006cbefa32b8449def3b6ed79ca8e80ddb0937fca9c72")
    version(
        "0.17.1",
        sha256="e31c7fafbdd5f94913161c5d64341a203364e512524b47295c97a91e83c4198b",
        url="https://github.com/canonical/raft/archive/refs/tags/v0.17.1.tar.gz",
    )

    variant("uv", default=True, description="Enable libuv support")
    variant("lz4", default=True, when="+uv", description="Enable lz4 support")
    variant("legacy", default=False, when="@0.22.2:", description="Enable legacy API")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("libuv@1.18.0:", when="+uv")
    depends_on("lz4", when="+lz4")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        args = []
        args += self.enable_or_disable("lz4")
        args += self.enable_or_disable("uv")
        if "+legacy" in self.spec:
            args += ["--enable-v0"]
        else:
            args += ["--disable-v0", "--disable-fixture"]
        return args
