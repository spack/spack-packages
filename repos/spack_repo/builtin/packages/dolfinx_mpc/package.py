# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DolfinxMpc(CMakePackage):
    """Extension of fenics-dolfinx for multipoint constraints."""

    homepage = "https://www.jsdokken.com/dolfinx_mpc"
    url = "https://github.com/jorgensd/dolfinx_mpc/archive/v0.9.3.tar.gz"
    git = "https://github.com/jorgensd/dolfinx_mpc.git"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.9.3", sha256="efa312cc498e428aab44acccc9bb0c74c200eda005742de7778c8e68fa84e8df")
    version("0.8.1", sha256="e0254b4a1c9c1456583c1415821946b11b0b2e48dbfee6558da2bbedfe78b461")

    # HDF5 dependency requires C in CMake
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("fenics-dolfinx@main+petsc", when="@main")
    depends_on("fenics-dolfinx@0.9+petsc", when="@0.9")
    depends_on("fenics-dolfinx@0.8+petsc", when="@0.8")
    depends_on("boost@1.70:+timer+filesystem", when="@:0.9")
    depends_on("cmake@3.21:", when="@0.9:", type="build")
    depends_on("cmake@3.19:", when="@:0.8", type="build")

    conflicts("%gcc@:9.10", msg="fenics-dolfinx requires GCC-10 or newer for C++20 support")
    conflicts("%clang@:9.10", msg="fenics-dolfinx requires Clang-10 or newer for C++20 support")

    root_cmakelists_dir = "cpp"
