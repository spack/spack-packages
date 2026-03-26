# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Megahit(CMakePackage):
    """Ultra-fast and memory-efficient (meta-)genome assembler"""

    homepage = "https://github.com/voutcn/megahit/tree/master"
    url = "https://github.com/voutcn/megahit/archive/refs/tags/v1.2.9.tar.gz"

    license("GPL-3.0")

    version("1.2.9", sha256="09026eb07cc4e2d24f58b0a13f7a826ae8bb73da735a47cb1cbe6e4693118852")
    
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    
    depends_on("zlib-api")
    depends_on("cmake@2.8:", type="build")
    depends_on("gcc@4.8.4:", type="build")
    depends_on("gzip", type="run")
    depends_on("bzip2", type="run")
