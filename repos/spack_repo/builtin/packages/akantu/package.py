# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Akantu(CMakePackage):
    """
    Akantu means a little element in Kinyarwanda, a Bantu language. From now
    on it is also an opensource object-oriented Finite Element library which
    has the ambition to be generic and efficient.

    """

    homepage = "https://akantu.ch"
    url = "https://gitlab.com/akantu/akantu/-/archive/v5.0.6/akantu-v5.0.6.tar.gz"
    git = "https://gitlab.com/akantu/akantu.git"

    maintainers("nrichart")

    license("LGPL-3.0-or-later")

    version("master", branch="master")
    version("5.0.6", sha256="ee197f6239e7c4c143edfc27a50c76512bd84c3eb0e11914b18e5782ed011c37")
    version(
        "3.0.0",
        sha256="7e8f64e25956eba44def1b2d891f6db8ba824e4a82ff0d51d6b585b60ab465db",
        deprecated=True,
    )

    variant(
        "external_solvers",
        values=any_combination_of("mumps", "petsc"),
        description="Activates the implicit solver",
    )
    variant("mpi", default=True, description="Activates parallel capabilities")
    variant("python", default=False, description="Activates python bindings")
    variant("cgal", default=False, description="Enable CGAL geometry support", when="@5:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("boost")

    with when("@5"):
        depends_on("eigen@3.3.7:", type="build")
        depends_on("cmake@3.16.3:", type="build")
        depends_on("cgal", when="+cgal")

    with when("@3"):
        depends_on("boost@:1.66")
        depends_on("lapack")
        depends_on("cmake@3.5.1:", type="build")

    with when("+python"):
        extends("python")
        depends_on("python", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))
        depends_on("py-scipy", type=("build", "run"))
        depends_on("py-pybind11", when="@3.1:", type=("build", "run"))

    with when("+mpi"):
        depends_on("mpi")
        depends_on("scotch")

    with when("external_solvers=mumps"):
        depends_on("mumps", when="~mpi")
        depends_on("mumps+mpi", when="+mpi")
        depends_on("netlib-scalapack", when="+mpi")

    with when("external_solvers=petsc"):
        depends_on("petsc+double", when="~mpi")
        depends_on("petsc+double+mpi", when="+mpi")

    conflicts("%gcc@:5.3")
    conflicts("@:3.0 external_solvers=petsc")
    conflicts("@:3.0 +python")

    def cmake_args(self):
        args = [
            self.define("AKANTU_VERSION", self.spec.version),
            self.define("AKANTU_COHESIVE_ELEMENT", True),
            self.define("AKANTU_DAMAGE_NON_LOCAL", True),
            self.define("AKANTU_SOLID_MECHANICS", True),
            self.define("AKANTU_STRUCTURAL_MECHANICS", self.spec.satisfies("@5:")),
            self.define_from_variant("AKANTU_PARALLEL", "mpi"),
            self.define_from_variant("AKANTU_PYTHON_INTERFACE", "python"),
        ]

        if self.spec.satisfies("@5:"):
            args += [
                self.define("AKANTU_DIFFUSION", True),
                self.define_from_variant("AKANTU_EMBEDDED", "cgal"),
            ]
        else:
            args.append(self.define("AKANTU_HEAT_TRANSFER", True))

        if self.spec.satisfies("@:3.0"):
            args.append(self.define("CMAKE_CXX_FLAGS", "-Wno-class-memaccess"))

        solvers = []
        if self.spec.satisfies("external_solvers=mumps"):
            solvers.append("Mumps")
            args.append(self.define("MUMPS_DIR", self.spec["mumps"].prefix))
        if self.spec.satisfies("external_solvers=petsc"):
            solvers.append("PETSc")

        if solvers:
            args += [
                self.define("AKANTU_IMPLICIT_SOLVER", "+".join(solvers)),
                self.define("AKANTU_IMPLICIT", True),
            ]
        else:
            args += [
                self.define("AKANTU_IMPLICIT_SOLVER", "Eigen"),
                self.define("AKANTU_IMPLICIT", False),
            ]

        return args
