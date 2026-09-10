# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Taskflow(CMakePackage):
    """Taskflow helps you quickly write parallel tasks programs in modern C++."""

    homepage = "https://github.com/taskflow/taskflow"
    url = "https://github.com/taskflow/taskflow/archive/v2.7.0.tar.gz"
    git = "https://github.com/taskflow/taskflow.git"

    license("MIT")

    version("master", branch="master")
    version("4.1.0", sha256="2107f90e315e48a676922010b036357ff2b0c6b9160ce17fa9396e5860b1d715")
    version("4.0.0", sha256="a9d27ad29caffc95e394976c6a362debb94194f9b3fbb7f25e34aaf54272f497")
    version("3.11.0", sha256="5e45a7ee032cae136843c76824519acbc0306f02d682f7e69fb1d53f69173dcb")
    version("3.7.0", sha256="788b88093fb3788329ebbf7c7ee05d1f8960d974985a301798df01e77e04233b")
    version("3.6.0", sha256="5a1cd9cf89f93a97fcace58fd73ed2fc8ee2053bcb43e047acb6bc121c3edf4c")
    version("2.7.0", sha256="bc2227dcabec86abeba1fee56bb357d9d3c0ef0184f7c2275d7008e8758dfc3e")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # Compiler must offer C++17 support
    conflicts("%gcc@:4.8")
    conflicts("%clang@:3.5")
    conflicts("%apple-clang@:8.0.0")

    def cmake_args(self):
        args = []
        # Taskflow 3.x uses C++17 features (std::is_trivial_v, inline constexpr, etc.)
        # but its CMakeLists.txt doesn't enforce CMAKE_CXX_STANDARD.
        # Taskflow 4.x sets C++20 itself, so no override needed.
        if self.spec.satisfies("@3"):
            args.append("-DCMAKE_CXX_STANDARD=17")
        return args
