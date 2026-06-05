# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Hashcat(MakefilePackage):
    """hashcat is the world's fastest and most advanced password recovery
    utility, supporting five unique modes of attack for over 300 highly
    optimized hashing algorithms. hashcat currently supports CPUs, GPUs,
    and other hardware accelerators on Linux, Windows, and macOS,and has
    facilities to help enable distributed password cracking."""

    homepage = "https://hashcat.net/hashcat/"
    url = "https://github.com/hashcat/hashcat/archive/v7.1.2.tar.gz"

    license("MIT")

    version("7.1.2", sha256="9546a6326d747530b44fcc079babad40304a87f32d3c9080016d58b39cfc8b96")
    version("7.1.1", sha256="1cdf6db3058088d7e3883f63519b5d345dbda0184ec8e1e1cb984e1255e297f0")
    version("7.1.0", sha256="cf2d73d36b85dfc5a36d20bf2d7516858173d5ef780df2055bc926c6f902da77")
    version("7.0.0", sha256="842b71d0d34b02000588247aae9fec9a0fc13277f2cd3a6a4925b0f09b33bf75")
    version("6.2.6", sha256="b25e1077bcf34908cc8f18c1a69a2ec98b047b2cbcf0f51144dcf3ba1e0b7b2a")
    version("6.1.1", sha256="39c140bbb3c0bdb1564bfa9b9a1cff49115a42f4c9c19e9b066b617aea309f80")
    version("6.1.0", sha256="916f92434e3b36a126be1d1247a95cd3b32b4d814604960a2ca325d4cc0542d1")
    version("6.0.0", sha256="e8e70f2a5a608a4e224ccf847ad2b8e4d68286900296afe00eb514d8c9ec1285")
    version("5.1.0", sha256="283beaa68e1eab41de080a58bb92349c8e47a2bb1b93d10f36ea30f418f1e338")
    version("5.0.0", sha256="7092d98cf0d8b29bd6efe2cf94802442dd8d7283982e9439eafbdef62b0db08f")

    variant("python", default=False, description="Enable optional Python support")
    variant("rust", default=False, description="Enable Rust plugin support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("python@3.12:", type=("build", "run"), when="+python")
    depends_on("rust", type="build", when="+rust")

    def build(self, spec, prefix):
        make("SHARED=1")

    def install(self, spec, prefix):
        make("PREFIX={0}".format(prefix), "install")
