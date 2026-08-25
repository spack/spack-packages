# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Abacus(CMakePackage):
    """ABACUS (Atomic-orbital Based Ab-initio Computation at UStc)
    is an open-source computer code package aiming
    for large-scale electronic-structure simulations
    from first principles"""

    homepage = "http://abacus.ustc.edu.cn/"
    url = "https://github.com/abacusmodeling/abacus-develop/archive/refs/tags/v3.9.0.19.tar.gz"
    git = "https://github.com/abacusmodeling/abacus-develop.git"

    maintainers("bitllion")

    license("LGPL-3.0-or-later")

    version("develop", branch="develop")
    version("3.10.1", sha256="06873eba8a4e0bc085177a6580455b28e4b62ea8a18f8afe71a02105756d91a0")
    version("3.9.0.19", sha256="c985af3d8ac6edb5767b7a094ac2fd2e0ea70b46cf353cd5a4b60096b289939d")

    variant("openmp", default=True, description="Enable OpenMP support")
    variant("lcao", default=True, description="Enable LCAO algorithm")
    variant("elpa", default=True, description="Enable ELPA support")
    variant("libxc", default=True, description="Enable LibXC support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("mpi")
    depends_on("cereal")
    depends_on("fftw+openmp", when="+openmp")
    depends_on("fftw~openmp", when="~openmp")
    depends_on("elpa", when="+elpa")
    depends_on("libxc", when="+libxc")
    depends_on("openblas")

    def cmake_args(self):
        args = [
            self.define("ENABLE_MPI", True),
            self.define("GIT_SUBMODULE", False),
            self.define_from_variant("USE_OPENMP", "openmp"),
            self.define_from_variant("ENABLE_LCAO", "lcao"),
            self.define_from_variant("USE_ELPA", "elpa"),
            self.define_from_variant("ENABLE_LIBXC", "libxc"),
        ]
        return args
