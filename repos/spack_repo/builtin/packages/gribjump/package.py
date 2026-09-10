# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gribjump(CMakePackage):
    """GribJump is a C++ library for extracting subsets of data from GRIB files,
    particularly data archived in the FDB
    """

    homepage = "https://github.com/ecmwf/gribjump"
    url = "https://github.com/ecmwf/gribjump/archive/refs/tags/0.10.0.tar.gz"
    git = "https://github.com/ecmwf/gribjump.git"
    list_url = "https://github.com/ecmwf/gribjump/tags"

    maintainers("cosunae")

    license("Apache-2.0")

    version("0.10.3", sha256="8001f8a0e4b03664134ea42612d22d6499e098d2063b12182030986895689f6c")
    version("0.10.2", sha256="c1635c1f902daa244592b60c9b1a81375b467409635bd2cbfc6993d32554bd3d")
    version("0.10.0", sha256="04a6c7322e585acb7e432e74d68f073ab584a42af9dcb2b4b97f17aebf17d07f")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.12:", type="build")
    depends_on("ecbuild", type="build")
    depends_on("eckit")
    depends_on("eccodes")
    depends_on("fdb")
    depends_on("metkit")
    depends_on("libaec@1.1.1:")

    def cmake_args(self):
        args = [
            self.define("ENABLE_MEMFS", True),
            self.define("ENABLE_ECCODES_THREADS", True),
            self.define("ENABLE_AEC", True),
        ]
        return args
