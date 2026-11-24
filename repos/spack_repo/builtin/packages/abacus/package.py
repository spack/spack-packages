# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems import cmake
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Abacus(CMakePackage):
    """ABACUS (Atomic-orbital Based Ab-initio Computation at UStc)
    is an open-source computer code package aiming
    for large-scale electronic-structure simulations
    from first principles"""

    homepage = "https://abacus.deepmodeling.com/"
    url = "https://github.com/deepmodeling/abacus-develop/archive/refs/tags/v3.9.0.27.tar.gz"
    git = "https://github.com/deepmodeling/abacus-develop.git"

    maintainers("bitllion")

    license("LGPL-3.0-or-later")

    version("develop", branch="develop")
    # Version 3.10.1 is an "LTS" release that predates 3.9.0.19. Unfortunately,
    # the LTS branch is now less robust than development branch due to lack of
    # backport mechanism, so 3.9.0.27 is currently choosen as preferred.
    version("3.10.1", sha256="06873eba8a4e0bc085177a6580455b28e4b62ea8a18f8afe71a02105756d91a0")
    version(
        "3.9.0.27",
        sha256="066128d48517373b7b6d4d841f6bf2d8ceff94ae8c175ab089ff482b40789008",
        preferred=True,
    )
    version("3.9.0.19", sha256="c985af3d8ac6edb5767b7a094ac2fd2e0ea70b46cf353cd5a4b60096b289939d")

    build_system("cmake")

    variant("mpi", default=True, description="Enable MPI support")
    variant("openmp", default=True, description="Enable OpenMP support")
    variant("lcao", default=True, description="Enable LCAO algorithm")
    variant("elpa", default=True, description="Enable ELPA support", when="+mpi")
    variant("libxc", default=True, description="Enable LibXC support")
    variant("libri", default=False, description="Enable LibRI support", when="+mpi +lcao")
    variant("dftd4", default=False, description="Enable DFT-D4 support", when="@3.11:")
    variant("plumed", default=False, description="Enable PLUMED support", when="@3.11:")
    variant("pexsi", default=False, description="Enable PEXSI support", when="+mpi +lcao")
    variant("json", default=False, description="Enable JSON output support", when="@3.11:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.16:", type="build")

    depends_on("blas")
    depends_on("lapack")

    depends_on("mpi", when="+mpi")
    depends_on("scalapack", when="+mpi")

    depends_on("fftw precision=float,double +openmp", when="+openmp")
    depends_on("fftw precision=float,double ~openmp", when="~openmp")
    depends_on("elpa +mpi +openmp", when="+elpa +openmp")
    depends_on("elpa +mpi ~openmp", when="+elpa ~openmp")

    depends_on("libxc@5.1.7:", when="+libxc")
    depends_on("dftd4@4.3: build_system=cmake", when="+dftd4")
    depends_on("plumed@2:", when="+plumed")
    depends_on("libri", when="+libri")
    depends_on("libcomm", when="+libri")
    # Older releases require Cereal for LCAO builds
    # Current versions use it only with LibRI
    depends_on("cereal", when="@:3.10 +lcao")
    depends_on("cereal", when="@3.11: +libri")
    depends_on("pexsi@2.0:", when="+pexsi")
    depends_on("nlohmann-json@3.12:", when="+json")


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("GIT_SUBMODULE", False),
            self.define("ENABLE_FLOAT_FFTW", True),
            self.define_from_variant("ENABLE_MPI", "mpi"),
            self.define_from_variant("ENABLE_LCAO", "lcao"),
            self.define_from_variant("ENABLE_PEXSI", "pexsi"),
            self.define_from_variant("ENABLE_LIBXC", "libxc"),
            self.define_from_variant("ENABLE_LIBRI", "libri"),
        ]

        if spec.satisfies("@3.11:"):
            args += [
                self.define_from_variant("ENABLE_OPENMP", "openmp"),
                self.define_from_variant("ENABLE_ELPA", "elpa"),
                self.define_from_variant("ENABLE_DFTD4", "dftd4"),
                self.define_from_variant("ENABLE_PLUMED", "plumed"),
                self.define_from_variant("ENABLE_JSON", "json"),
            ]

        if spec.satisfies("+libri"):
            args += [
                self.define("LIBRI_DIR", spec["libri"].prefix),
                self.define("LIBCOMM_DIR", spec["libcomm"].prefix),
            ]

        if spec.satisfies("@:3.10"):
            args += [
                self.define_from_variant("USE_OPENMP", "openmp"),
                self.define_from_variant("USE_ELPA", "elpa"),
            ]
        return args
