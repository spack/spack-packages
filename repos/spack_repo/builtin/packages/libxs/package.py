# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libxs(CMakePackage):
    """LIBXS is a portable C library providing building blocks for memory
    operations, numerics, synchronization, and more -- with a focus on
    performance and minimal dependencies. Targets x86-64, AArch64, and RISC-V;
    requires only a C89 compiler. Originally developed as part of LIBXSMM.
    """

    maintainers("hfp", "mkrack", "mtaillefumier")

    homepage = "hhttps://libxs.readthedocs.io/en/latest"
    url = "https://github.com/hfp/libxs/archive/refs/tags/1.0.tar.gz"
    git = "https://github.com/hfp/libxs.git"

    license("BSD-3-Clause", checked_by="mkrack")

    version("main", branch="main")
    version("1.0.0", sha256="b26654a9d7d41e7281a785d3674626c2484c92e7fc698e166639c8e78b2b18ee")

    variant("fortran", default=True, description="Build Fortran module interface")
    variant("pic", default=True, description="Build position independent code")
    variant("shared", default=False, description="Build shared libraries (otherwise static)")
    variant("libxsmm", default=False, description="Enable libxsmm dependency")

    depends_on("cmake@3.13:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("libxsmm")

    def cmake_args(self):
        args = [
            self.define_from_variant("LIBXS_FORTRAN", "fortran"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define_from_variant("LIBXS_SHARED", "shared"),
        ]
        return args
