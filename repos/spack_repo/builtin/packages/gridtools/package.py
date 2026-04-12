# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Gridtools(CMakePackage):
    """Libraries and utilities to develop performance portable applications for
    weather and climate"""

    homepage = "https://gridtools.github.io"
    url = "https://github.com/GridTools/gridtools/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/GridTools/gridtools.git"

    maintainers("msimberg")

    license("BSD-3-Clause", checked_by="msimberg")

    version("master", branch="master")
    version("2.3.9", sha256="463bd29c4cee7027e99ad0ba5a9f121be481efbc75c604af4256927c5670fd7c")

    depends_on("cxx", type="build")

    generator("ninja")

    depends_on("ninja", type="build")

    def cmake_args(self):
        args = [self.define("BUILD_TESTING", False), self.define("GT_INSTALL_EXAMPLES", False)]
        return args
