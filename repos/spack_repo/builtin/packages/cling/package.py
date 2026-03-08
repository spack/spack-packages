# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cling(CMakePackage):
    """Cling is an interactive C++ interpreter, built on the top of LLVM
    and Clang libraries. Its advantages over the standard interpreters
    are that it has command line prompt and uses just-in-time (JIT)
    compiler for compilation."""

    homepage = "https://root.cern/cling/"
    url = "https://github.com/root-project/cling/archive/refs/tags/v1.2.tar.gz"
    git = "https://github.com/root-project/cling.git"

    maintainers("wdconinc")

    license("LGPL-2.1 OR NCSA", checked_by="wdconinc")

    version("master", branch="master")
    version("1.3", sha256="ca81f3bc952338beffba178633d77f5b3e1f1f180cbe2bb9f2713c06f410fd18")
    version("1.2", sha256="beee8e461424d267ee2dec88b3de57326bc8e3470b4ceae2744de7d3d3aba1eb")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.10:", type="build")
    depends_on("llvm+clang")

    def cmake_args(self):
        args = []
        return args
