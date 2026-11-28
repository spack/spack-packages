# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Svmultiphysics(CMakePackage):
    """Parallel finite-element solver for fluid, structural, fluid-structure
    interaction (FSI), and Coupled-Momentum Method (CMM) problems."""

    homepage = "https://github.com/SimVascular/svMultiPhysics"
    git = "https://github.com/SimVascular/svMultiPhysics.git"

    license("BSD-3-Clause")

    maintainers("failed33")

    version(
        "1.0.0.2",
        tag="v1.0.0.2",
        commit="fba504ea45cb9f8b06d85201df79d1b21a016840",
        preferred=True,
    )
    version(
        "1.0.0.3",
        tag="v1.0.0.3",
        commit="88f85b97608aac4e1e76204c44ad4c0a1a34a312",
    )
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.22:", type="build")
    depends_on("mpi")
    depends_on("vtk@9.3:9")
    depends_on("blas")
    depends_on("lapack")
    # The solver passes int arguments to the Fortran LAPACK interface.
    requires("^openblas~ilp64", when="^[virtuals=blas,lapack] openblas")

    variant(
        "trilinos",
        default=False,
        description="Enable the Trilinos linear algebra backend",
    )
    variant(
        "petsc",
        default=False,
        description="Enable the PETSc linear algebra backend",
    )
    depends_on(
        "trilinos@16: +mpi +amesos2 +belos +ifpack2 +kokkos +muelu +tpetra "
        "+zoltan +zoltan2 gotype=int",
        when="+trilinos",
    )
    # The PETSc interface passes int indices and double solution arrays directly.
    depends_on("petsc+mpi+double+shared~complex~int64", when="+petsc")

    def cmake_args(self):
        mpi = self.spec["mpi"]
        # FSILS uses MPI_LIBRARY, which FindMPI extracts from the wrappers.
        solver_args = [
            self.define("MPI_C_COMPILER", mpi.mpicc),
            self.define("MPI_CXX_COMPILER", mpi.mpicxx),
        ]
        if self.spec.satisfies("+trilinos"):
            # Upstream otherwise falls back to FSILS if Trilinos discovery fails.
            solver_args.extend(
                [
                    self.define("Trilinos_ROOT", self.spec["trilinos"].prefix),
                    self.define("CMAKE_REQUIRE_FIND_PACKAGE_Trilinos", True),
                ]
            )
        args = [
            self.define("SV_LOCAL_VTK_PATH", self.spec["vtk"].prefix),
            self.define_from_variant("SV_USE_TRILINOS", "trilinos"),
            self.define("SV_ADDITIONAL_CMAKE_ARGS", solver_args),
        ]
        if self.spec.satisfies("+petsc"):
            args.append(self.define("SV_PETSC_DIR", self.spec["petsc"].prefix))
        return args

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        executable = join_path(
            self.build_directory, "svMultiPhysics-build", "bin", "svmultiphysics"
        )
        install(executable, prefix.bin)
