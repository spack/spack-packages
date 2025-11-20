# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lielab(CMakePackage):
    """Lielab is a C++ library for numerical Lie-theory: Lie groups, Lie algebras, homogeneous
    manifolds, and various functions and algorithms on these spaces."""

    homepage = "https://github.com/sandialabs/Lielab"
    maintainers("msparapa")
    license("MIT")

    version("0.5.1", sha256="5a7545a675f630418634d9827e8db5035949bf8ae165f17600c03bf5a6da35af")

    def url_for_version(self, version):
        return f"https://github.com/sandialabs/Lielab/archive/refs/tags/v{version}.tar.gz"

    depends_on("cxx", type="build")
    depends_on("cmake@3.23:", type="build")
    depends_on("eigen@5.0.0:6.0.0", type="build")

    variant("pic", default=True, description="Position independent code (-fPIC)")
    variant(
        "cxxstd",
        default="20",
        values=("20", "23", "26"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )

    def cmake_args(self):
        args = []
        args.append("-DLIELAB_INSTALL_LIBRARY=TRUE")
        args.append("-DLIELAB_BUILD_TESTS=FALSE")
        args.append("-DLIELAB_BUILD_PYTHON=FALSE")

        args.append(self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"))
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        return args
