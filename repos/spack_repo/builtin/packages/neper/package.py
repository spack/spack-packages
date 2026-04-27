# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Neper(CMakePackage):
    """Neper is a software package for polycrystal generation and meshing.
    The polycrystals can be 2D or 3D."""

    homepage = "https://neper.info/"
    url = "https://github.com/neperfepx/neper/archive/refs/tags/v4.10.1.tar.gz"

    maintainers("jcortial-safran")

    license("GPL-3.0-only", checked_by="jcortial-safran")

    version("4.10.1", sha256="73aeb29658a73fa5fd1deec74daacc1d43fcf0f771da4157a00fb3736dbdc37e")

    variant("gsl", default=True, description="Enable GNU scientific library")
    variant("openmp", default=True, description="Enable OpenMP")
    variant(
        "nlopt",
        default="external",
        description="Enable NlOpt, using either the vendored or an external package",
        values=("none", "internal", "external"),
        multi=False,
    )
    variant(
        "scotch",
        default="external",
        description="Enable SCOTCH, using either the vendored or an external package",
        values=("none", "internal", "external"),
        multi=False,
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("gsl", when="+gsl")
    depends_on("nlopt", when="nlopt=external")
    depends_on("scotch", when="scotch=external")

    depends_on("cmake@3:", type="build")

    root_cmakelists_dir = "src"

    def cmake_args(self):
        args = [
            self.define("CMAKE_INSTALL_COMPLETION_PREFIX", self.prefix),
            self.define_from_variant("HAVE_GSL", "gsl"),
            self.define_from_variant("HAVE_OPENMP", "openmp"),
            self.define("HAVE_NLOPT", not self.spec.satisfies("nlopt=none")),
            self.define("FORCE_BUILTIN_NLOPT", self.spec.satisfies("nlopt=internal")),
            self.define("HAVE_LIBSCOTCH", not self.spec.satisfies("scotch=none")),
            self.define("FORCE_BUILTIN_LIBSCOTCH", self.spec.satisfies("scotch=internal")),
        ]
        return args
