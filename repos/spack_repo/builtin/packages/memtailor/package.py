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
    url = "https://github.com/Macaulay2/memtailor/releases/download/v1.1/memtailor-1.1.tar.gz"
    git = "https://github.com/Macaulay2/memtailor"

    maintainers("d-torrance")

    license("BSD-3-Clause", checked_by="d-torrance")

    version("1.4", sha256="4d5baebf701b04b44201b75831f451305b572a5bc39235a94567ad4e59ad6cdc")
    version("1.3", sha256="10f0c016e67912be1711a54b18c54d7024c8bfcaf0f279e11187402994150a20")
    version("1.2", sha256="86cd8f888d23f53256937b47cebe8430daeb8146ca9816c4d3aef0fc5ebc702b")
    version("1.1", sha256="ce0dc2e5befd1e1f65c99510bc68ddc5b60f13066eac12ec5ce4e1da822e44eb")
    version("1.0.2025.05.13", commit="07c84a6852212495182ec32c3bdb589579e342b5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    # googletest 1.17.0 requires C++17 support, which wasn't added until 1.2
    depends_on("googletest@:1.16.0", when="@:1.1")
    depends_on("googletest", when="@1.2:")

    def configure_args(self):
        return ["--enable-shared"]
