# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Memtailor(AutotoolsPackage):
    """Memtailor is a C++ library of special-purpose memory
    allocators, including an arena allocator and a memory pool,
    designed for better and more predictable performance than
    new/delete. The memory pool is useful for many fixed-size
    allocations, such as linked list nodes, while the arena allocator
    is fast, works like stack allocation, stays within the C++
    standard, and allows multiple independent arenas."""

    homepage = "https://github.com/Macaulay2/memtailor"
    git = "https://github.com/Macaulay2/memtailor"

    maintainers("d-torrance")

    license("BSD-3-Clause", checked_by="d-torrance")

    version("1.0.2025.05.13", commit="07c84a6852212495182ec32c3bdb589579e342b5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("googletest@:1.16.0")  # 1.17.0 requires c++17

    def configure_args(self):
        return ["--enable-shared"]
