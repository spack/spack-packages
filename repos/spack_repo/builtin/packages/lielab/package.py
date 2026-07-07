# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lielab(CMakePackage):
    """Lielab is a C++ library for numerical Lie-theory: Lie groups, Lie algebras, homogeneous
    manifolds, and various functions and algorithms on these spaces."""

    homepage = "https://github.com/sandialabs/Lielab"
    url = "https://github.com/sandialabs/Lielab/archive/refs/tags/v0.5.2.tar.gz"

    maintainers("msparapa")

    license("MIT")

    version("0.5.2", sha256="d98ddf93fa317165891b69944c5ffab48c3955fd7c1c9428b06a0452f8fca453")
    version("0.5.1", sha256="5a7545a675f630418634d9827e8db5035949bf8ae165f17600c03bf5a6da35af")

    variant("pic", default=True, description="Position independent code (-fPIC)")
    variant(
        "cxxstd",
        default="20",
        values=("20", "23", "26"),
        multi=False,
        sticky=True,
        description="C++ standard",
    )
    variant("with_assertions", default=True, description="Build with assertions included.")

    depends_on("cxx", type="build")
    depends_on("cmake@3.23:", type="build")
    depends_on("eigen@5.0.0:6.0.0", type="build")
    depends_on("fmt@12.1.0:", type="build", when="@0.5.2:")

    conflicts("%gcc@:10.2")  # Fails on 8.5, works on 10.3.

    def cmake_args(self):
        args = []
        args.append(self.define("LIELAB_INSTALL_LIBRARY", True))
        args.append(self.define("LIELAB_BUILD_TESTS", False))
        args.append(self.define("LIELAB_BUILD_PYTHON", False))

        args.append(self.define_from_variant("LIELAB_WITH_ASSERTIONS", "with_assertions"))

        args.append(self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"))
        args.append(self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"))
        return args
