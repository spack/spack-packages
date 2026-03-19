# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Gridtools(CMakePackage):
    """Libraries and utilities to develop performance portable applications for weather and climate."""

    homepage = "https://gridtools.github.io"
    url = "https://github.com/GridTools/gridtools/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/GridTools/gridtools.git"

    maintainers("msimberg")

    license("BSD-3-Clause", checked_by="msimberg")

    version("master", branch="master")
    version("2.3.9", sha256="463bd29c4cee7027e99ad0ba5a9f121be481efbc75c604af4256927c5670fd7c")
    # TODO: Keep any of these?
    # version("2.3.8", sha256="4a5e9171db65b4c4b4ea7a79cec19200ab2614ed0c320d1a15f98ba61f099fcd")
    # version("2.3.7", sha256="2f1bb0f876e0bcea3c5695e6e186ed37fddf3bd71936a30a2f8e01d9d86544d7")
    # version("2.3.6", sha256="e5b003afce041c7d56a2222f351cc3baf29e25fb616136b11bbe598127762056")
    # version("2.3.5", sha256="028342c48e6c8a484cadecbef2cb955901a9402f704f6c719923c2f26eb464c8")
    # version("2.3.4", sha256="ff151435ffe26f1f9508d8a07c7cb594878b90f22b9f7f9435fb2bc4d7e6f124")
    # version("2.3.2", sha256="5271a92df69f492e254622d387cfa12d746b0538aeb2ff918296455f2fd58cda")
    # version("2.3.1", sha256="54b62bfba45afc56561f0a7d14d34038a5c5b22a80aee67096ba60effe9f764e")
    # version("2.3.0", sha256="56ec2612b04af89162462485adf8efc9c2958b27feb265a0645358c0eb187e93")
    # version("2.0.1", sha256="de627980d5cd3403e5f802b0206320b1bfc3d0c94a3834b671469873c1325d27")

    depends_on("cxx", type="build")

    generator("ninja")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", False),
            self.define("GT_INSTALL_EXAMPLES", False),
        ]
        return args
