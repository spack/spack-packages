# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class CpuFeatures(CMakePackage):
    """A cross platform C99 library to get cpu features at runtime."""

    homepage = "https://github.com/google/cpu_features"
    git = "https://github.com/google/cpu_features.git"
    url = "https://github.com/google/cpu_features/archive/refs/tags/v0.7.0.tar.gz"

    license("Apache-2.0")

    version("main", branch="main")
    version("0.10.1", sha256="52639b380fced11d738f8b151dbfee63fb94957731d07f1966c812e5b90cbad4")
    version("0.9.0", sha256="bdb3484de8297c49b59955c3b22dba834401bc2df984ef5cfc17acbe69c5018e")
    version("0.7.0", sha256="df80d9439abf741c7d2fdcdfd2d26528b136e6c52976be8bd0cd5e45a27262c0")

    variant("shared", description="Build shared libraries", default=False)

    depends_on("c", type="build")
    depends_on("cxx", type="test")
    depends_on("googletest", type="test")

    depends_on("cmake@3:", type="build")
    depends_on("cmake@3.13:", type="build", when="@0.9:")

    def cmake_args(self):
        return [
            self.define("BUILD_TESTING", self.run_tests),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]
