# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Yasm(AutotoolsPackage, CMakePackage):
    """Yasm is a complete rewrite of the NASM-2.11.06 assembler. It
    supports the x86 and AMD64 instruction sets, accepts NASM and
    GAS assembler syntaxes and outputs binary, ELF32 and ELF64
    object formats."""

    homepage = "https://yasm.tortall.net"
    url = "https://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz"
    git = "https://github.com/yasm/yasm.git"

    license("BSD-2-Clause")

    version("develop", branch="master")
    version("1.3.0", sha256="3dce6601b495f5b3d45b59f7d2492a340ee7e84b5beca17e48f862502bd5603f")

    build_system("autotools", "cmake", default="autotools")

    requires("build_system=cmake", when="platform=windows")

    # cmake: support CMake 4.0 and cross building
    patch(
        "https://github.com/yasm/yasm/commit/7a7762c3378b277c90c7868e2361644d80083740.patch?full_index=1",
        sha256="535ccd6ccca1ec927a5a8a30f6dba51e8a11eda305e6a45bb0d5a2701723f31b",
        when="@1.3.0 build_system=cmake",
    )

    # Ensure C23 compliance in boolean enum
    # https://github.com/yasm/yasm/pull/287
    patch("libyasm_bitvect_c23_bool.patch")

    depends_on("c", type="build")
    depends_on("cxx", type="build", when="build_system=cmake")

    with when("build_system=autotools"):
        depends_on("autoconf", when="@develop")
        depends_on("automake", when="@develop")
        depends_on("libtool", when="@develop")
        depends_on("m4", when="@develop")
