# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Samurai(CMakePackage):
    """Intervals coupled with algebra of set to handle adaptive
    mesh refinement and operators on it"""

    homepage = "https://github.com/hpc-maths/samurai"
    url = "https://github.com/hpc-maths/samurai/archive/refs/tags/v0.27.1.tar.gz"
    git = "https://github.com/hpc-maths/samurai.git"

    maintainers("gouarin", "sbstndb")

    license("BSD-3-Clause")

    version("master", branch="master")
    version("0.28.0", sha256="94a50fc30714b652157e27ac7870dc8487e1045289d87cb83b28d2c7f6834b94")
    version("0.27.1", sha256="5cb1ffb87a6a3defbde45037bd80e8277c31d577e20559c6cb2853b82bc989ba")
    version("0.27.0", sha256="23d3e6475fbc674a887af84333b49ff6ac68fa8326e9edfdb49fa47491c28f4f")
    version("0.26.1", sha256="07971b2c5359cc33f5e3fb3f4f7d156b6aed91441139a1ae133378ba25e46d7a")
    version("0.26.0", sha256="66d94b787c701cb9287a63dffeff7bb129d9465bef7ec6513362b987bf3fbcd3")
    version("0.25.1", sha256="6eb053138161d4823ad4e2d400add581b0a70402d59513fd855af6b625f48bfe")
    version("0.25.0", sha256="b09ca316c099f8e60fdc7d0c94d884bd1777aab174547eead6e87bed3c2b1039")
    version("0.24.0", sha256="73c2596f14f83f9c116d4e5755b369b440c2e95e152de42699fff27c398f9c47")
    version("0.23.0", sha256="7f0c626b5f5671e40dc2d35c520db69c30444083b247eba1a5dc026a519b4ce3")
    version("0.22.0", sha256="65a087ba0eb461f75b3ee4cf7725432d8c92f2a1af42220d6b233279a432429b")
    version("0.21.1", sha256="f052ee47a4f533fb805f3d3c9c9d5462e2b041855c9e4322d902860ec572d747")

    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    # variants for a future release
    # variant("demos", default=False, description="Build Demos")
    # variant("benchmarks", default=False,description="Build benchmarks")
    variant("tests", default=False, description="Build tests")
    variant("check_nan", default=False, description="Check for Nan in computations")

    # optional dependency for a future release
    depends_on("xtensor@0.26:", when="@0.27.1:")
    depends_on("xtensor@0.25", when="@0.23:0.27.0")
    depends_on("highfive@3", when="@0.27.1:")
    depends_on("highfive@2", when="@0.21:0.27.0")
    depends_on("pugixml")
    depends_on("fmt")
    depends_on("cli11")
    depends_on("petsc")

    depends_on("petsc +mpi", when="+mpi")
    depends_on("highfive +mpi", when="+mpi")
    depends_on("boost +serialization +mpi", when="+mpi")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        include_path = self.spec.prefix.include
        env.append_path("CXXFLAGS", f"-I{include_path}")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("CPATH", self.spec.prefix.include)

    def cmake_args(self):
        spec = self.spec
        options = []

        options.append(self.define_from_variant("SAMURAI_CHECK_NAN", "check_nan"))

        # MPI support
        if spec.satisfies("+mpi"):
            options.append(self.define_from_variant("WITH_MPI", "mpi"))
            options.append(self.define("HDF5_IS_PARALLEL", True))

        # OpenMP support
        if spec.satisfies("+openmp"):
            options.append(self.define_from_variant("WITH_OPENMP", "openmp"))

        return options
