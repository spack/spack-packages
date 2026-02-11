# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.python import PythonPackage


class PyFenicsDolfinx(PythonPackage):
    """Python interface to the next generation FEniCS problem solving
    environment."""

    homepage = "https://github.com/FEniCS/dolfinx"
    url = "https://github.com/FEniCS/dolfinx/archive/v0.1.0.tar.gz"
    git = "https://github.com/FEniCS/dolfinx.git"
    maintainers("chrisrichardson", "garth-wells", "nate-sime", "jhale")

    license("LGPL-3.0-or-later")

    version("main", branch="main", no_cache=True)
    version(
        "0.10.0.post4", sha256="3f827a88ab52843fbd7a5cc7814ecba165bdec65fd10df05eb031c286e8cd605"
    )
    version("0.9.0", sha256="b266c74360c2590c5745d74768c04568c965b44739becca4cd6b5aa58cdbbbd1")
    version("0.8.0", sha256="acf3104d9ecc0380677a6faf69eabfafc58d0cce43f7777e1307b95701c7cad9")
    with default_args(deprecated=True):
        version("0.7.2", sha256="7d9ce1338ce66580593b376327f23ac464a4ce89ef63c105efc1a38e5eae5c0b")
        version("0.6.0", sha256="eb8ac2bb2f032b0d393977993e1ab6b4101a84d54023a67206e3eac1a8d79b80")

    # CMake build type
    variant(
        "build_type",
        default="RelWithDebInfo",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel", "Developer"),
    )

    variant("petsc4py", default=False, description="petsc4py support")
    variant("slepc4py", default=False, description="slepc4py support")

    # py-fenics-dolfinx does not require a C compiler, but does depend
    # on DOLFINXConfig.cmake which in turn includes hdf5-config.cmake.
    # When HDF5 has MPI support, hdf5-config.cmake calls
    # enable_language(c).
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", when="@0.9:", type="build")
    depends_on("cmake@3.19:", when="@:0.8", type="build")
    depends_on("hdf5", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("python@3.10:", when="@0.10:", type=("build", "run"))
    depends_on("python@3.9:", when="@0.8:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.7", type=("build", "run"))
    depends_on("python@3.8:3.10", when="@0.6.0", type=("build", "run"))

    for ver in ["main", "0.10.0.post4", "0.9.0", "0.8.0", "0.7.2", "0.6.0"]:
        depends_on(f"fenics-dolfinx@{ver}", when=f"@{ver}")

    for ver in ["main", "0.10", "0.9", "0.8", "0.7", "0.6"]:
        depends_on(f"fenics-basix@{ver}", type=("build", "link"), when=f"@{ver}")
        depends_on(f"py-fenics-basix@{ver} +ufl", type=("build", "run"), when=f"@{ver}")
        depends_on(f"py-fenics-ffcx@{ver}", type=("build", "run"), when=f"@{ver}")

    for ufl_ver, ver in [
        ("main", "main"),
        ("2025.2", "0.10"),
        ("2024.2", "0.9"),
        ("2024.1", "0.8"),
        ("2023.2", "0.7"),
        ("2023.1", "0.6"),
    ]:
        depends_on(f"py-fenics-ufl@{ufl_ver}", type=("build", "run"), when=f"@{ver}")

    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))

    conflicts("~petsc4py", when="@:0.8", msg="+petsc4py is required for versions 0.8 and lower")
    conflicts("~petsc4py", when="+slepc4py", msg="+slepc4py requires +petsc4py")
    with when("+petsc4py"):
        depends_on("fenics-dolfinx +petsc")
        depends_on("py-petsc4py", type=("build", "run"))
    with when("+slepc4py"):
        depends_on("fenics-dolfinx +petsc +slepc")
        depends_on("py-petsc4py", type=("build", "run"))
        depends_on("py-slepc4py", type=("build", "run"))

    depends_on("py-cffi", type=("build", "run"))

    depends_on("py-nanobind@2.5:", when="@0.10:", type="build")
    depends_on("py-nanobind@2:", when="@0.9:", type="build")
    depends_on("py-nanobind@1.8:1.9", when="@0.8", type="build")
    depends_on("py-scikit-build-core@0.10: +pyproject", when="@0.9:", type="build")
    depends_on("py-scikit-build-core@0.5: +pyproject", when="@0.8:0.9", type="build")

    depends_on("py-pybind11@2.7.0:", when="@:0.7", type=("build", "run"))
    depends_on("py-setuptools@42:", when="@:0.7", type="build")

    def config_settings(self, spec, prefix):
        return {
            "build.tool-args": f"-j{make_jobs}",
            "build.verbose": "true",
            "cmake.build-type": spec.variants["build_type"].value,
        }

    build_directory = "python"
