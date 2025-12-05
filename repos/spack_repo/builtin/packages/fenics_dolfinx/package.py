# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class FenicsDolfinx(CMakePackage):
    """Next generation FEniCS problem solving environment."""

    homepage = "https://github.com/FEniCS/dolfinx"
    git = "https://github.com/FEniCS/dolfinx.git"
    url = "https://github.com/FEniCS/dolfinx/archive/v0.1.0.tar.gz"
    maintainers("chrisrichardson", "garth-wells", "nate-sime", "jhale")
    license("LGPL-3.0-or-later")

    version("main", branch="main", no_cache=True)
    version("0.10.0.post4", sha256="3f827a88ab52843fbd7a5cc7814ecba165bdec65fd10df05eb031c286e8cd605")
    version(
        "0.10.0.post2", sha256="eae83794fee8141c80c59c03a2f4ac208af2b62c8f36e5d19c93e0d279029f52"
    )
    version("0.9.0", sha256="b266c74360c2590c5745d74768c04568c965b44739becca4cd6b5aa58cdbbbd1")
    version("0.8.0", sha256="acf3104d9ecc0380677a6faf69eabfafc58d0cce43f7777e1307b95701c7cad9")
    with default_args(deprecated=True):
        version("0.7.2", sha256="7d9ce1338ce66580593b376327f23ac464a4ce89ef63c105efc1a38e5eae5c0b")
        version("0.6.0", sha256="eb8ac2bb2f032b0d393977993e1ab6b4101a84d54023a67206e3eac1a8d79b80")

    patch("0.8-boost-filesystem.patch", when="@0.8")

    # CMake build types
    variant(
        "build_type",
        default="RelWithDebInfo",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel", "Developer"),
    )

    # Graph partitioner variants
    variant(
        "partitioners",
        description="Graph partioning",
        default="parmetis",
        values=("kahip", "parmetis", "scotch"),
        multi=True,
    )

    depends_on("c", type="build")  # HDF5 dependency requires C in CMake config
    depends_on("cxx", type="build")

    conflicts("%gcc@:12", when="@0.10:")

    # Graph partitioner dependencies
    depends_on("kahip@3.12:", when="partitioners=kahip")
    depends_on("parmetis", when="partitioners=parmetis")
    depends_on("scotch+mpi", when="partitioners=scotch")

    variant("slepc", default=False, description="SLEPc support")
    variant("adios2", default=False, description="ADIOS2 support")
    variant("petsc", default=False, description="PETSc support")

    conflicts("~petsc", when="+slepc", msg="+slepc requires +petsc")

    depends_on("cmake@3.21:", when="@0.9:", type="build")
    depends_on("cmake@3.19:", when="@:0.8", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("mpi")
    depends_on("hdf5+mpi")
    depends_on("boost@1.70:")
    depends_on("boost@1.70:+timer", when="@:0.9")
    depends_on("pugixml")
    depends_on("spdlog", when="@0.9:")

    depends_on("petsc+mpi+shared", when="+petsc")
    with when("+slepc"):
        depends_on("petsc+mpi+shared")
        depends_on("slepc")

    depends_on("adios2@:2.10", when="@:0.9 +adios2")
    depends_on("adios2@2.8.1:", when="@0.9: +adios2")
    depends_on("adios2+mpi", when="+adios2")

    for ver in ("main", "0.10", "0.9", "0.8", "0.7", "0.6"):
        depends_on(f"fenics-ufcx@{ver}", when=f"@{ver}")
        depends_on(f"fenics-basix@{ver}", when=f"@{ver}")
        depends_on(f"py-fenics-ffcx@{ver}", when=f"@{ver}", type="test")
    depends_on("catch2", type="test")

    root_cmakelists_dir = "cpp"

    def cmake_args(self):
        return [
            self.define_from_variant("CMAKE_BUILD_TYPE", "build_type"),
            self.define("DOLFINX_SKIP_BUILD_TESTS", True),
            self.define_from_variant("DOLFINX_ENABLE_PETSC", "petsc"),
            self.define_from_variant("DOLFINX_ENABLE_SLEPC", "slepc"),
            self.define_from_variant("DOLFINX_ENABLE_ADIOS2", "adios2"),
            self.define("DOLFINX_UFCX_PYTHON", False),
            self.define("DOLFINX_ENABLE_KAHIP", "partitioners=kahip" in self.spec),
            self.define("DOLFINX_ENABLE_PARMETIS", "partitioners=parmetis" in self.spec),
            self.define("DOLFINX_ENABLE_SCOTCH", "partitioners=scotch" in self.spec),
        ]
