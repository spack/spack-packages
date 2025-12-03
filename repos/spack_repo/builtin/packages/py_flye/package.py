# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFlye(PythonPackage):
    """Fast and accurate de novo assembler for single molecule sequencing
    reads"""

    homepage = "https://github.com/fenderglass/Flye"
    url = "https://github.com/fenderglass/Flye/archive/2.6.tar.gz"

    license("BSD-3-Clause")

    version("2.9.6", sha256="f05a3889b1c7aafed4cc0ed1adc1f19c22618c1c7b97ab5f80d388c8192bd32a")
    version("2.9.5", sha256="7b384266d83b1e66bcaf82d49d35ac6c587bad9146e8f3b752a220291f6b1a6f")
    version("2.9.4", sha256="197a2dfe39fc324a39d8e1901af4f539609159c4a64a578ec8e60f73f5ea4696")
    version("2.9.3", sha256="09580390ed0558c131ca0b836a2374d3cc7993cba2a6500024c2ee1d96666edc")
    version("2.9.2", sha256="4b9534b912c805d44b83d497b40102bed807678b82be62667129bf1641676402")
    version("2.9.1", sha256="25a2375cd9ba6b2285f930951ad0fde81628baa97d8709172aa59e931a96678e")
    version("2.9", sha256="158ea620d4aa92a53dae1832b09fd605e17552e45b83eecbf28e41a4516a6957")
    version("2.8.3", sha256="070f9fbee28eef8e8f87aaecc048053f50a8102a3715e71b16c9c46819a4e07c")
    version("2.8.2", sha256="f1284bd2a777356fbf808d89052bc0f9bf5602560dde7cf722d7974d9a94d03b")
    version("2.8.1", sha256="436ebe884e5000c023d78c098596d22c235c916f91e6c29a79b88a21e611fcb4")
    version("2.7", sha256="4d595f53bd68c820b43509ce6ee7284847237e70a3b4bc16c57170bb538d3947")
    version("2.7.1", sha256="0e826261c81537a7fa8fd37dc583edd75535eee0f30429d6bdb55f37b5722dbb")
    version("2.6", sha256="5bdc44b84712794fa4264eed690d8c65c0d72f495c7bbf2cd15b634254809131")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # https://github.com/fenderglass/Flye/blob/flye/docs/INSTALL.md
    depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("gmake", type="build")
    depends_on("zlib-api")

    msg = "C++ compiler with C++11 support required"
    conflicts("%gcc@:4.7", msg=msg)
    conflicts("%clang@:3.2", msg=msg)
    conflicts("%apple-clang@:4.9", msg=msg)

    patch("dir_fix.patch", when="@:2.8,=2.9")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.target.family == "aarch64":
            env.set("arm_neon", "1")
            env.set("aarch64", "1")
