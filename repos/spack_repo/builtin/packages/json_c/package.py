# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class JsonC(CMakePackage):
    """A JSON implementation in C."""

    homepage = "https://github.com/json-c/json-c/wiki"
    url = "https://s3.amazonaws.com/json-c_releases/releases/json-c-0.15.tar.gz"

    license("MIT")

    version("0.18", sha256="876ab046479166b869afc6896d288183bbc0e5843f141200c677b3e8dfb11724")
    version("0.16", sha256="8e45ac8f96ec7791eaf3bb7ee50e9c2100bbbc87b8d0f1d030c5ba8a0288d96b")
    version("0.15", sha256="b8d80a1ddb718b3ba7492916237bbf86609e9709fb007e7f7d4322f02341a4c6")
    version("0.14", sha256="b377de08c9b23ca3b37d9a9828107dff1de5ce208ff4ebb35005a794f30c6870")

    depends_on("c", type="build")

    depends_on("cmake@3.9:", when="@0.17:", type="build")

    def cmake_args(self):
        return [self.define("DISABLE_WERROR", True)]
