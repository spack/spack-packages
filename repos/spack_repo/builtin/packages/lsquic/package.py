# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lsquic(CMakePackage):
    """LiteSpeed QUIC Library (LSQUIC) is an open-source implementation of QUIC and HTTP/3 for
    servers and clients."""

    homepage = "https://github.com/litespeedtech/lsquic"
    git = "https://github.com/litespeedtech/lsquic.git"

    patch("fix_find_library_name_and_path.patch")

    maintainers("ta7mid")

    license("MIT", checked_by="ta7mid")

    version("master", branch="master", submodules=True)
    version("4.2.0", commit="7686d8fcef284cda07a951ad74a5e90c69a9dfb1", submodules=True)
    version("4.1.0", commit="59157330b518e7dc4612d03247890ef184365c80", submodules=True)

    variant("shared", default=False, description="Build shared libraries")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("perl", type="build")  # required for source code generation

    depends_on("boringssl~shared", when="~shared")
    depends_on("boringssl+shared", when="+shared")
    depends_on("zlib")

    def cmake_args(self):
        return [
            self.define_from_variant("LSQUIC_SHARED_LIB", "shared"),
            self.define("BORINGSSL_DIR", self.spec["boringssl"].prefix),
            self.define("LSQUIC_BIN", False),
            self.define("LSQUIC_TESTS", False),
        ]
